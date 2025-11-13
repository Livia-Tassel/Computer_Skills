<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">KV Cache 压缩</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

# ExCP: Extreme LLM Checkpoint Compression via Weight-Momentum Joint Shrinking
论文：https://arxiv.org/abs/2406.11257
代码：https://github.com/Gaffey/ExCP
年份：2024.6.17
核心：checkpoint 的存储压缩
## 名词解释
- 检查点（Checkpoint）：LLM 训练途中定期保存参数、优化器状态等信息，避免意外情况导致模型从头训练。
- 优化器（Optimizer）：优化器本质上是一种算法，根据 LLM 的损失值与梯度得出参数优化的方向与步长。常见的优化器如 “Adam” 的检查点除上述信息外，还会保存 “动量状态”（几乎和 LLM 参数一样大），为此 ExCP 论文中尝试利用联合权重和动量剪枝来对 LLM checkpoint 进行压缩。
- 动量（Momentum）：动量是 Adam 等优化器的 “核心组件”，作用是记住之前的参数更新方向（一阶矩 ($v_{t}$)）与步长（二阶矩 ($m_{t}$)），让参数更新稳定、更快。
- 量化（Quantization）：论文中采用非均匀量化，即对于核心参数高精度存储（FP16/FP32），而非核心参数整型存储。
- 残差（Residual）：即相邻两个参数之间的差异，LLM 大部分参数残差具有稀疏性，也正因此非常适合压缩。
- 近无损恢复（Nearly Lossless Recovery）：从压缩后的 checkpoint 恢复训练时，得到的 LLM 几乎没有性能损失。

## 核心方法
![alt text](kvcache.assets/1.png)
### 残差检查点（Residual Checkpoint）
- **输入**：当前训练轮次的模型权重 $W_t$、上一轮次的模型权重 $W_{t-1}$，以及优化器状态 $\mathcal{O}_t$。 
- **操作**：**权重残差** $\Delta W_t = W_t - W_{t-1}$。
- **原理**：LLM 训练中，相邻轮次的权重是 “渐进微调” 的，因此 $\Delta W_t$ 会包含大量接近0的稀疏值。

### 权重-动量联合剪枝（Weights-momentum Joint-pruning）
- **权重剪枝（M2W pruning）**：
  - 针对残差权重 $\Delta W_t$，以**二阶矩 $m_t$** 为指标，设置阈值 $\tau_w = 1.8$（示例值），将低于阈值的残差权重设为0，得到剪枝掩码 $\mathcal{M}_w$。
  - 原理：低于阈值的残差对模型性能影响极小，可安全剪枝。

下面以**实际矩阵示例**来拆解，$W$指的是**权重残差矩阵**（即$\Delta W_t = W_t - W_{t-1}$）。
\[
W = \begin{pmatrix}
2.2 & 1.4 & 1.3 \\
3.2 & 1.2 & 1.5 \\
0.1 & 2.4 & 3.8 \\
\end{pmatrix}
\]

取得残差矩阵的中位数 $\text{median}(W) = 1.5$，假设超参数 $\alpha = 5e-5$，二阶矩 $m_t = 0.0004$，代入公式计算剪枝阈值 $r_w$，：
\[
r_w = \frac{\alpha}{\sqrt{m_t}} \times \text{median}(W) = \frac{5e-5}{0.02} \times 1.5 = 0.00375
\]

剪枝掩码 $\mathcal{M}_w(i) = \mathcal{I}_{w(i) > r_w}$，即原残差矩阵 $W$ 中小于 0.00375 的将被剪枝。

- **动量剪枝（W2M pruning）**：
  - 针对优化器的一阶动量 $v_t$，以**一阶矩 $v_t$** 为指标，根据权重剪枝的掩码 $\mathcal{M}_w$，仅保留权重未被剪枝位置的动量，得到剪枝掩码 $\mathcal{M}_o$。
  - 原理：动量与权重强关联，权重被剪枝的位置，其动量对后续训练的作用也可忽略，因此同步剪枝可进一步减少冗余。

### 非均匀量化（Non-uniform quantization）
- **操作**：对剪枝后的残差权重和动量，用**K-means聚类**将数值分为若干“聚类中心”（如示例中的 $0, 2.3, 3.5$ 等），然后存储 “聚类中心 $C_t$” 和 “聚类索引 $\mathcal{I}_t$”。
- **原理**：多个相似的数值可以共享同一个聚类中心，只存储索引即可还原原始数值。

经过上述三步处理后，再用压缩算法（如7zip）打包，得到**体积极小的压缩检查点（Compressed Checkpoints）**，同时能保证模型训练的 “近无损恢复”。


# CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving
论文：https://arxiv.org/abs/2310.07240
代码：https://github.com/UChi-JCL/CacheGen
年份：2024.7.19
核心：长上下文 KV 缓存网络传输延迟高
## 名词解释
- 张量（Tensor）：高维向量，CacheGen 核心在于通过编码技术，将大张量转化为小的 “比特流”，传输后再解码恢复为张量。
- Delta 编码（Delta Coding）：即残差编码，使得量化和算术编码压缩效率更高。
- 通道（Channel）：即不同 K/V 向量的同一位置，由于相邻 token 语义的相似性，相邻向量同一通道的值也具有相似性，[详细](https://www.zhihu.com/question/362131975/answer/3491521854)见解。

## 核心方法
### 差值张量计算（Delta Tensors）
- **操作**：将上下文按 10 个 token 分组，每组选首个 token 为 “锚定 token”，以高精度存储，其余 token 以低精度存储与锚定 token 的 KV 差值（即 delta 张量）。
- **原理**：**token 级局部性（Token-wise Locality）**，即同一层的同一通道内，相邻 token 的 KV 值差异远小于原始值，即**差值（delta）的方差比原始值的方差低**。
![alt text](kvcache.assets/4.png)

### 分层量化（Layer-wise Quantization）
- **操作**：将 Transformer 分为 3 组（前 1/3、中 1/3、后 1/3），对不同组采用不同精度的**向量量化**，从前到后精度依次下降。
- **原理**：**层间损失敏感性（Layer-wise Sensitivity to Loss）**,即浅表 KV 抽象的是原始信息，其值损失对 LLM 性能影响较大。
![alt text](kvcache.assets/5.png)

### 算术编码（Arithmetic Coding）
- **操作**：离线为所有 “Layer+Channel” 组合量化符号的概率分布，使用 GPU 加速的算术编码库，对量化后的 delta 张量和锚定张量进行**无损压缩**。
- **原理**：**维度分布差异（Distribution along Layers, Channels, and Tokens）**，即由于语义的相似性，同通道的 KV 值分布更集中，为此按 “Layer+Channel” 分组的 KV 值信息增益（熵降低）远高于按 token 位置分组。而熵越低，值的 “可预测性” 越强，压缩算法（如算术编码）能更高效地减少比特流大小。
![alt text](kvcache.assets/3.png)

下面以 $2\ Layer、3\ Token、3\ Channel$ 来直观体验熵减与算术编码的魅力：
\[
\text{Layer 1 V} = \begin{pmatrix} 
0.6 & 0.3 & 0.1 \\
0.2 & 0.8 & 0.0 \\
0.5 & 0.2 & 0.3
\end{pmatrix}
\]

\[
\text{Layer 2 V} = \begin{pmatrix} 
0.8 & 0.2 & 0.1 \\
0.9 & 0.3 & 0.05 \\
0.7 & 0.1 & 0.15
\end{pmatrix}
\]

熵 $H = -\sum p_i \log_2 p_i$（$p_i$ 为某值的出现概率），将所有 V 值量化为 3 种符号（$A\in[0.0,0.3],\ B\in[0.4,0.6],\ C\in[0.7,0.9]$），统计概率后得到熵：

#### No grouping 组：
\[
[0.6(\text{B}), 0.3(\text{A}), 0.1(\text{A}),\ 0.2(\text{A}), 0.8(\text{C}), 0.0(\text{A}),\ 0.5(\text{B}), 0.2(\text{A}), 0.3(\text{A})\ ...]
\]
- 符号统计：A 出现 11 次，B 出现 2 次，C 出现 5 次；
- 概率：$p_A=11/18≈0.61$，$p_B=2/18≈0.11$，$p_C=5/18≈0.28$；
- 熵：$H = -0.61\log_20.61 -0.11\log_20.11 -0.28\log_20.28 ≈ 1.45$。

#### By token 组：
将相同位置（行）的 Token 的 V 值归为一组，共 3 组：
- Token1组：符号=[B, A, A, C, A, A] → A=4, B=1, C=1 → 熵≈1.46；
- Token2组：符号=[A, C, A, C, A, A] → A=4, C=2 → 熵≈1.0；
- Token3组：符号=[B, A, A, C, A, A] → A=4, B=1, C=1 → 熵≈1.46；
- 平均熵：$(1.46+1.0+1.46)/3 ≈ 1.31$。

#### By channel 组：
将相同通道（列）的 V 值归为一组，共 3 组：
- 通道 0 组：符号=[B, A, B, C, C, C] → B=2, C=3, A=1 → 熵≈1.46；
- 通道 1 组：符号=[A, C, A, A, A, A] → A=5, C=1 → 熵≈0.65；
- 通道 2 组：符号=[A, A, A, A, A, A] → A=6 → 熵=0；
- 平均熵：$(1.46+0.65+0)/3 ≈ 0.70$。

#### By layer 组：
将每层的所有通道、Token V值归为一组，共2组（第1层、第2层）：
- **第1层组**：符号=[B, A, A, A, C, A, B, A, A] → A=5, B=2, C=1 → 熵≈1.36；
- **第2层组**：符号=[C, A, A, C, A, A, C, A, A] → A=5, C=3 → 熵≈1.29；
- 平均熵：$(1.36+1.29)/2 ≈ 1.33$ 比特/元素（虽有降低，但不如按通道分组显著）。

分组后各通道的符号 “集中”，熵自然大幅降低，算术编码能为高频符号分配极短比特，最终实现高压缩比。

### 自适应流传输（Adaptive Streaming）
- **操作**：根据实时带宽动态适应传输内容，在 CacheGen 中将上下文拆分为多个上下文块（论文中以 1.5k token 作为默认块长），每个块都压缩不同精度的版本，传输时根据实时带宽选择最合适版本，如带宽极差时，则直接传输原始上下文予 CPU 重新计算。
- **原理**：压缩方法即张量量化 → 聚类（存储索引）→ 按 “Layer + Channel” 分组得到序列，如 [1, 2, 0, 1] → [转比特流](https://zhuanlan.zhihu.com/p/390684936)。
