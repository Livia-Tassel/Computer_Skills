<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">操作系统入门</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

---

# 系统引导
## QEMU 模拟
![alt text](os.assets/1.png) 

## 内存映射
![alt text](os.assets/2.png)
![alt text](os.assets/3.png)

# 内存管理
## 链接脚本（Linker Script）
链接脚本是用于指导链接器（Linker）如何将程序的不同代码段和数据段组织、布局和放置在最终可执行文件或内存中的配置文件。
![alt text](os.assets/4.png)

而内存管理是利用链接脚本提供的地址信息来划分、分配和保护内存。
![alt text](os.assets/5.png)

## 内存分配和释放（页级别）
### 数组实现
物理内存划分为大小固定的页帧（Page Frames），大小通常是4KB。数组实现的核心在于建立页帧与数组中元素（位图）的一一对应关系。
![alt text](os.assets/6.png)

# 协作式多任务
## 上下文
“上下文”指的是一个进程/线程在任何时间点的完整运行状态，当操作系统停止运行某个程序并切换到另一程序时，它必须保存当前程序的上下文，以便将来能够从它中断的地方恢复执行。

上下文信息通常包括：
1. CPU 寄存器
2. 进程状态信息（进程 ID、进程状态等）
3. 内存管理信息（页表基址寄存器）

## 协作式多任务
操作系统不具备强制抢占正在运行的程序的能力。 只有当当前程序主动放弃控制权后，操作系统才能进行上下文切换，调度下一个任务运行。
![alt text](os.assets/7.png)

# 异常
## 控制流
控制流指的是 CPU 执行程序指令的顺序，在没有特殊指令或事件干扰的情况下，程序按顺序执行；异常控制流（ECF）则是系统对突发事件的响应机制。

## 寄存器
### mtvec
存储发生异常时 CPU 跳转到的地址，必须保证 4 字节对齐。
![alt text](os.assets/8.png)

### mepc
当 $trap$[^1] 发生时，$hart$ 将 $mepc$ 设置为当前指令或下一指令的地址，以便退出 $trap$ 时，将 $mepc$ 中的值恢复到 PC 中。
![alt text](os.assets/9.png)

### mcause
指示 $trap$ 发生的具体原因，最高位 $Interrupt$ 为 1，标识为中断，否则为异常，剩余的 $Exception\ Code$ 标识具体的中断/异常种类。
![alt text](os.assets/10.png)
![alt text](os.assets/11.png)

### mtval
辅助 $mcause$ 指示 $trap$ 更加详细的信息。
![alt text](os.assets/12.png)

### mstatus
- XIE（X=M/S/U，红色部分），分别用于打开（1）或关闭（0）M/S/U 模式下的全局中断，当 $trap$ 发生时，$hart$ 将其自动设置为 0，防止被其他 $trap$ 打断。
- XPIE（X=M/S/U，绿色部分），用于保存 $trap$ 发生前 XIE 的值。 
- XPP（X=M/S，黄色部分），用于保存 $trap$ 发生前的权限级别值。 
- 其余标志位涉及内存访问权限、虚拟内存控制等。
![alt text](os.assets/13.png)

## 异常处理
### 初始化
1.  设置 $mtvec$：内核将异常处理程序的入口地址写入 $mtvec$ 寄存器。
2.  设置 $mstatus$ 和 $mie$：控制全局中断使能和特权级切换。
3.  配置特权级：内核配置 CSRs 以允许从 U-Mode 切换到 S-Mode/M-Mode。

### 上半部（Top Half）
* 将 PC 保存到 $mepc$ 中，同时将 PC 设置为 $mtvec$。
* 将引发 $trap$ 的原因代码写入 $mcause$，并根据实际为 $mtval$ 设置附加信息。
* 将 $trap$ 发生前的全局中断使能状态保存到 $mstatus$ 的 MPIE 中，清除 MIE 标志位，从而使中断禁止。
* 将 $trap$ 发生前的权限模式保存到 $mstatus$ 的 MPP 中，并将 $hart$ 权限模式改为 M。
![alt text](os.assets/15.png)

### 下半部（Bottom Half）
* 利用 $mscratch$ 保存当前控制流的上下文信息。
* 调用 C 程序的 $trap\ handle$ 函数（从 $trap\ handle$ 返回，$mepc$ 的值可能有所修改）。
* 恢复上下文信息，并执行 $mret$ 指令返回到 $trap$ 之前的状态。

### 返回（Return）
#### mret 指令
用于退出 $trap$，不同权限级别退出 $trap$ 有各自的返回指令 XRET(X=M/S/U)。
![alt text](os.assets/16.png)

以 M 模式为例，执行 $mret$ 后，执行以下操作：
```c
hart = mstatus.MPP;
mstatus.MPP = U;
mstatus.MIE = mstatus.MPIE;
mstatus.MPIE = 1;
PC = mepc;
```

# 中断
## 中断分类
中断分为本地中断和全局中断，其中本地中断又分为软中断和定时器中断。
![alt text](os.assets/17.png)

## 寄存器
### mie、mip
- $mie$ 二级控制中断信号，打开（1）或关闭（0）M/S/U 模式下的外部/定时器/软件中断，前面提到的 MIE 是控制全局中断的使能信号，若关闭则所有类型中断均禁止。
![alt text](os.assets/18.png)
- $mip$ 标识当前 M/S/U 模式下外部/定时器/软件中断是否打开。
![alt text](os.assets/19.png)

## PLIC
由于 CPU 的外部中断信号只有一个，而外设种类众多，为此引入中断控制器（PLIC），统一控制外部中断信号。当多个中断同时发生时，根据优先级筛选出一个进行处理。
![alt text](os.assets/20.png)

### 寄存器
- $priority$：每个中断源对应一个寄存器，用于配置该中断源的优先级。
- $pending$：每个 PLIC 包含 2 个 32 位的 $pending$ 寄存器，每一个 $bit$ 对应一个中断源，为 1 即该中断源上发生了中断，有待 $hart$ 处理，否则无中断发生。
- $enable$：每个 $hart$ 有 2 个 $enable$ 寄存器，用于控制该 $hart$ 启动或关闭某路中断源。
- $threshld$：每个 $hart$ 有 1 个 $threshold$ 寄存器用于设置中断优先级的阈值，小于阈值的中断即使发生也不予处理。
- $claim/complete$：每个 $hart$ 有 1 个 $claim/complete$，两者本质上是一个寄存器，$claim$ 获取当前优先级最高的中断源 ID，$claim$ 成功后清除其 $pending$ 位；$complete$ 通知 PLIC 对该路中断的处理已经结束。

### PLIC 流程
![alt text](os.assets/21.png)

# 硬件定时器
## 






















[^1]: 异常和中断统称为 $trap$。
