<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">一生一芯入门</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

---

# 数字逻辑电路基础
## 晶体管与门电路
### 晶体管数量分析
<table>
<tr align="center">
    <td><img src="digital electronics.assets/1.png" width="300"></td>
    <td><img src="digital electronics.assets/2.png" width="300"></td>
</tr>
<tr align="center">
    <td><em>Logic Gates</em></td>
    <td><em>Transistors</em></td>
</tr>
</table>

已知非门晶体管数量为 2，与非门晶体管数量为 4，为此得到与门晶体管数量为 6；所以上述三输入与非门中在门电路层面搭建耗费的晶体管数为 $\#T(nandn)=(n-2)\#T(and)+\#T(nand)=10$，而右侧全定制的三输入与非门在晶体管层面搭建的耗费数为 $\#T(nandn)=2n=6,\#T(andn)=\#T(nandn)+\#T(not)=2(n+1)=8$

以下是全定制的异或门，仅需 6 个晶体管，而用门电路来搭建需要整整 22 个晶体管：
![alt text](<digital electronics.assets/3.png>)

## 时序逻辑电路
### D 触发器
正常的带使能信号的主从式 D 触发器的实现如下：
![alt text](<digital electronics.assets/4.png>)

然而，我似乎发现一种更为“邪修”的方法，只要将 EN 信号与上 clk 信号，随便输入一个 D 锁存器的 WE 信号中，就能实现控制使能的效果，因为只要 EN 为 0，那么必然有一个 D 锁存器的写使能信号为 0，从而做到信号阻断的效果。
![alt text](<digital electronics.assets/5.png>)

## 存储器
存储器是一段可寻址的存储单元的集合，可以看成一个由比特构成的矩阵，每一行是一个存储单元，地址即为行的编号，行的数量即为存储器的深度 $(depth)$。

因此，地址的位宽为 $log_{2}(depth)$，每一行又可以存储多位数据，一行的位宽称为存储器的宽度 $(width)$。以下即为深度为 2，宽度为 3 的存储器。
![alt text](<digital electronics.assets/6.png>)

存储器又分只读存储器 $(ROM)$ 和随机访问存储器 $(RAM)$，后者可读可写。以下是用 D 触发器实现最基础的读、写寄存器的操作。
<table>
<tr align="center">
    <td><img src="digital electronics.assets/7.png" width="300"></td>
    <td><img src="digital electronics.assets/8.png" width="300"></td>
    <td><img src="digital electronics.assets/9.png" width="300"></td>
</tr>
<tr align="center">
    <td><em>Read</em></td>
    <td><em>Write</em></td>
    <td><em>Read and Write</em></td>
</tr>
</table>

以上结构中带使能端的 D 触发器的晶体管数量占总数的大部分，所以可以使用全定制的 SRAM 单元，单个仅需 6 个晶体管。
![alt text](<digital electronics.assets/10.png>)

不过 SRAM 由于没有时序，所以存储阵列前面还得再额外加一层 D 触发器来赋予其时序功能，此时晶体管数量依旧远远小于直接使用带使能端 D 触发器搭建的触发器，但会造成一个周期的延迟，所以带使能端的 D 触发器通常用于搭建寄存器堆，而 SRAM 通常用于搭建高速缓存。

