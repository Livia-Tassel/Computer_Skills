<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">Digital Electronic 入门</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

---

# 晶体管与门电路
## 晶体管数量分析
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

# 时序逻辑电路
## D 触发器
正常的带使能信号的主从式 D 触发器的实现如下：
![alt text](<digital electronics.assets/4.png>)

然而，我似乎发现一种更为“邪修”的方法，只要将 EN 信号与上 clk 信号，随便输入一个 D 锁存器的 WE 信号中，就能实现控制使能的效果，因为只要 EN 为 0，那么必然有一个 D 锁存器的写使能信号为 0，从而做到信号阻断的效果。
![alt text](<digital electronics.assets/5.png>)