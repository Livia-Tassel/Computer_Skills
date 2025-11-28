<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">KV Cache 压缩</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

# A Survey on Efficient Inference for Large Language Models
论文：https://arxiv.org/abs/2404.14294
代码：无
年份：2024.7.19
核心：LLM 高效推理综述

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
![alt text](kvcache.assets/2.png)

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

# GEAR: An Efficient KV Cache Compression Recipe for Near-Lossless Generative Inference of LLM
论文：https://arxiv.org/html/2403.05527
代码：https://github.com/HaoKang-Timmy/GEAR
年份：2024.9.30
核心：KV Cache 近无损存储压缩
![alt text](kvcache.assets/8.png)

## 核心方法
GEAR 通过 “量化主干+低秩近似+稀疏修正” 的三级架构，实现 “高压缩比-近无损性能” 平衡，具体流程如下：
$$\min_{\hat{D}, L, S} \|X - \hat{D} - L - S\|_F$$

### 步骤 1：基于异常值过滤的量化主干（$\hat{D}$）
先提取 KV 张量中的极值异常值，再对剩余值进行超低精度量化，避免异常值导致的量化误差放大。

1. 异常值提取：对 Key 张量（按 channel 分组）和 Value 张量（按 token 分组），分别提取每个分组内 $\frac{s}{2}\%$ 的最大值与 $\frac{s}{2}\%$ 的最小值，构成稀疏矩阵 $S \in \mathbb{R}^{n \times d}$：  
    $$S_{ij} = \begin{cases} 
    X_{ij} & \text{if} \ X_{ij} \in \text{top/bottom } \frac{s}{2}\% \ \text{of group} \\
    0 & \text{else}
    \end{cases}$$

    （论文中 $s=2\%$，即仅保留 2% 的异常值，内存开销 \<3%）
2. 分组量化：对过滤后的 $X - S$ 采用 **per-channel Key + per-token Value** 量化（基于 KCVT/KIVI 变体），量化公式为：  
    $$\hat{D}_{\mathcal{G}_i} = \left\lfloor \frac{(X - S)_{\mathcal{G}_i} - \min_{\mathcal{G}_i} (X - S)}{\Delta_i} \right\rceil, \quad \Delta_i = \frac{\max_{\mathcal{G}_i} (X - S) - \min_{\mathcal{G}_i} (X - S)}{2^b - 1}$$  
    其中 $\mathcal{G}_i$ 为分组 $i$，$b$ 为量化位宽（2-bit/4-bit），$\Delta_i$ 为缩放因子。

### 步骤 2：头级别低秩近似（$L$）
量化残差 $R = X - \hat{D} - S$ 存在**相干结构**（即不同 token 共享部分上下文信息），通过低秩矩阵捕捉该结构，修正量化误差。

1. 头级别分解：将残差 $R$ 按注意力头拆分，得到 $H$ 个子矩阵 $R_h \in \mathbb{R}^{n \times d_H}$（$d_H = d/H$ 为单头维度）；
2. 低秩逼近：对每个 $R_h$，通过**幂迭代算法**（高效 SVD 近似）得到 top-$r$ 奇异值与向量，构建低秩矩阵 $L_h = A_h B_h^\top$（$A_h \in \mathbb{R}^{n \times r}$，$B_h \in \mathbb{R}^{d_H \times r}$），最终拼接为 $L = \text{Concat}(L_1, ..., L_H)$；
3. 秩选择：论文中 $r=4$（prefill 阶段）/$r=2$（解码阶段），此时 $L$ 的内存开销仅为原始 $X$ 的 $\frac{r}{d} \approx 3.125\%$（$d=128$ 时）。

### 步骤 3：误差融合与重建
- **最终压缩张量**：$\hat{X} = \hat{D} + L + S$，满足 $\|X - \hat{X}\|_F \ll \|X - \hat{D}\|_F$（量化误差降低 80% 以上）；
- **流缓冲优化**：引入大小为 $n_b=20$ 的缓冲区，每生成 $n_b$ 个 token 批量执行上述压缩，比逐令牌压缩延迟降低 40%。

以下是在不同量化技术的基础上加上 GEAR 获得的效果：
<table>
<tr align="center">
    <td><img src="kvcache.assets/6.png" width="300"></td>
    <td><img src="kvcache.assets/7.png" width="300"></td>
</tr>
</table>

## IDEAL
流版 Bitwise Gear 完全保留原版 Gear “拆分易压/难压部分 → 分模块处理 → 协同重建” 的分治逻辑，但针对 MNN 端侧 **CPU 算力有限、内存/存储资源紧张、精度要求 100% 无损**的特性，将原版 “量化 + SVD 低秩” 的有损算子，改为**位操作 + 流式无损压缩**的硬件友好型算子，最终实现 “Bit-exact 无损压缩” 与 “端侧无感推理” 的双重目标。

### 步骤 1：Base 流提取 —— 高低位拆分
FP16 由 “1 位符号 + 5 位指数 + 10 位尾数” 构成：
- **高 8 位**：在同一 Channel/Attention Head 内，因上下文语义相关性强，分布稳定，熵值极低，属于 “易压部分”，对应原版 Gear 的 “基准部分”；
- **低 8 位**：长序列下存在局部统计规律，属于 “难压部分”，对应原版 Gear 的 “残差部分”。

将原始 KV 张量 $X \in \text{FP16}^{n \times d}$（$n$ 为序列长度，$d$ 为特征维度）拆分为 Base 流 $\hat{D}$：所有 FP16 的高 8 位，存储为`uint8_t`型，尺寸为 $n \times d$（字节数仅为原始的 1/2）；Residual 流 $R$：所有 FP16 的低 8 位，同样存储为`uint8_t`型，尺寸与 Base 流一致。

通过 NEON 的`vst2q_u8`指令，将拆分后的高低位 “交织” 写入内存，避免朴素循环中 “Base流/Residual流反复切换导致的 Cache Line 颠簸”，内存带宽打满。

### 步骤 2：Residual 流压缩
原版 Gear 用 SVD 低秩分解捕捉残差的“全局相干性”（有损），而 Bitwise Gear 利用 Zstd 压缩的 “字典记忆 + 滑动窗口” 特性，捕捉 Residual 流的“局部序列相关性”（无损）：

**双流并行压缩**：为 Base 流和 Residual 流分别创建独立的 Zstd 流上下文，Base 流压缩比可达 5× 以上；Residual 流压缩比可达 1.2×~1.5×，最后将两个流的压缩结果封装为 “双流压缩块”。

### 步骤3：流式缓冲与无损重建
#### ① 压缩阶段：4KB Page Buffer批量处理
#### ② 解压重建阶段：预取 + NEON 快速拼接

# LoMA: Lossless Compressed Memory Attention
论文：https://ar5iv.labs.arxiv.org/html/2401.09486
代码：无
年份：2024.1.16
核心：KV Cache （近）无损压缩记忆注意力

## 核心方法
LoMA 的核心是 “训练时学习压缩/验证，推理时执行压缩/生成”：
### 训练阶段
训练的核心是 “**阅读区（原始信息）→ 内存区（压缩信息）→ 重复区（验证压缩）**”的闭环。
#### 步骤 1：输入序列的结构化重组
LoMA 将原始训练序列拆分为多个**训练块（Training Chunk）**，每个块强制包含 3 个区域，且引入 2 个 token：  
- $m$（Memory Token）：存储压缩后的信息，放在 “内存区”；  
- $r$（Repetition Token）：验证压缩是否无损，放在 “重复区”。  

![alt text](kvcache.assets/9.png)

为此，训练块的结构公式为：  
$$Training\ Chunk = Reading\ Zones(t_c) + Memory\ Zones(t) + Repetition\ Zones(t_c)$$

其中：  
- $t_c = c × t$（$c$ 为**压缩比**）；  
- 阅读区：原始文本 token（如“今天天气晴朗，适合去公园散步”）；  
- 内存区：$t$ 个 $m$ token（如 $m\ m$）；  
- 重复区：$t_c$ 个 $r$ token（如 $r\ r\ r\ r\ r\ r\ r\ r$）。  

#### 步骤 2：特殊注意力掩码
普通 Transformer 用 “下三角掩码” 实现自回归，但 LoMA 通过**自定义掩码**强制规定三个区域的信息流向，避免模型 “作弊”，三种区域的掩码规则如下：

![alt text](kvcache.assets/11.png)
![alt text](kvcache.assets/12.png)

#### 步骤 3：间接监督损失
LoMA 不为 “内存区的 $m$” 设计标签，而是通过**重复区的损失间接监督<m>的压缩能力**，形成 “压缩质量 → 复现效果 → 损失反馈” 的闭环。  

$$L = L_{Read} + L_{Rep}$$  

其中
- $L_{Read}$：普通 LLM 的自回归损失（如交叉熵）；  
- $L_{Rep}$：核心监督项，要求 “重复区的 $r$ token 必须完全复现原始信息”，损失为<r>的预测结果与原文本的交叉熵。  

注：原论文中特殊位置 ID（保证压缩后上下文连贯性）忽略。

### 推理阶段
训练完成后，模型已具备 “将长 KV Cache 压缩为短 $m$ KV” 的能力，推理时无额外辅助模型，仅通过 3 步即可完成无损压缩，且融入 autoregressive 生成流程。

假设训练好的 Llama-2-7B 模型进行 “问如何煮咖啡” 的长对话推理，设置 $c=4$、$t=2$：  

1. **步骤 1：初始化**  
   模型按标准 autoregressive 方式生成 $t_c=8$ 个 token，如 “问如何煮咖啡，要详细步骤”，同时得到这 8 个 token 对应的 KV Cache（记为 $KV_{Read}$）。  

2. **步骤 2：输入 $m$ token**  
   向模型输入 $t=2$ 个 $m$ token，模型基于步骤 1 的 $KV_{Read}$ 执行一次推理：  
   - 此时模型会将 $KV_{Read}$ 中的所有信息（“问如何煮咖啡，要详细步骤” 的上下文）压缩到 2 个 $m$ 的 KV Cache 中（记为 $KV_{Compressed}$）；  
   - 训练时 $m$ 已学会存储所有必要信息，2 个 $m$ 的 KV 完全等价于 8 个原始 token 的KV。  

3. **步骤 3：驱逐原始 KV**  
   驱逐步骤 1 的 $KV_{Read}$，仅保存 $KV_{Compressed}$，模型基于 $KV_{Compressed}$ 完成回答，回答过程中又得到新的 token，重复步骤 2-3。  

