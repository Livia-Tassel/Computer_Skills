<center style="font-family: 'Times New Roman', sans-serif; color: orange; font-size: 2em; font-weight: bold">VimTutor</center>
<div style="text-align: right; font-family: 'Times New Roman', serif; font-size: 1em;">Livia Tassel</div>

[TOC]

# 移动
## 光标移动
>左 h 
 下 j
 上 k
 右 l
## 单词移动
>前一单词 w
 后一单词 b
 单词尾部 e
## 字母匹配
>向后匹配字母 f+'char'
 向前匹配字母 t+'char'
## 行
>行首 0
 有效行首 _
 行尾 $
 当前行置为视觉中心 zz
 当前行置为视觉末尾 zb
 当前行置为视觉开头 zt 
## 页
>上半页 Ctrl+u
 下半页 Ctrl+d
 上页 Ctrl+f
 下页 Ctrl+b
## 搜索
>文本搜索 /+"content"
 下一搜索 n
 上一搜索 N
## 跳转
>文本开头 gg
 文本末尾 G
 行跳转 "行数"+G
## 数字
>"数字"+"指令" 效果翻倍

# 编辑
## 插入
>当前位置处插入 i
 当前位置后插入 a
 行开头插入 I
 行末尾插入 A
## 删除（剪切）
>删除单词 d{num}w
 删除字母 d" "
 当前位置删到词尾 de
 删除下行 d{num}j
 删除上行 d{num}k
 删除整行 dd
 删除整行，插入模式（缩进） cc 
 当前位置删到末尾 D
 当前位置删到末尾，插入模式 C
 当前位置删到行首 d0（含空格）
 **d→c**
 **删除并转为插入模式**
## Replace
>当前位置字母 r+'char'
 段落 :"行","行"s/old/new/gc
 全文 :%s/old/new/gc
 选择模式下选中 :s/old/new/gc
 将选中文段中的,→\r
 :s/,/\r/g

## 行
>光标下添加新行并进入编辑模式 o
 光标上添加新行并进入编辑模式 O

# 复制、粘贴
>复制当前行 yy（含换行符）
 向下行粘贴 p
 向上行粘贴 P
 复制当前单词 yw
 复制到行尾 y$（不含换行符）
 复制到开头 y^（不含空格）
 复制到开头 y0（含空格）

# 选择
>选择模式 v+光标移动
 选中当行并进入选择模式 V+光标移动
 Visual Block模式 control+v+光标移动
 Visual Block模式下
 多行开头插入 I（Shift+i）
 多行末尾插入 A（Shift+a）
 多行删除 d
 多行删除+插入 c
 快速选择上次选择的代码块 gv 
 Replace Mode R
 <!-- ############################# -->
 <!-- # This is a comment for us. # -->
 <!-- ############################# -->
 大小写翻转 ~

# 撤销
>undo所有在插入模式下的行为 u
 redo（undo的逆行为） control+r

# 进阶
## 内联
>删除当前光标所在单词并进入插入模式 ciw
 删除当前括内容并进入插入模式 ci'('、ci'{'
 选中当前""中内容 vi'"'
 复制当前光标所在单词 yiw
 选中/剪切/复制当前标签（tag）中内容（常于HTML中） v/d/y+it
## 格式化
>将选中内容格式化 选择模式选中内容+'='
## 搜索
>忽略大小写 :set ic
 取消忽略大小写 :set noic
 搜索高亮 :set hls is
 取消搜索高亮 :nohlsearch
## easyMotion
>ve 进入选择模式
 f+char easyMotion 向右跳转至首个char位置
 F+char easyMotion 向左跳转至首个char位置
 Normal模式下
 d+f+char 向右删除到首个char位置
 d+F+char 向左删除到首个char位置
 c+f+char 向右删除到首个char位置，插入模式
 c+F+char 向左删除到首个char位置，插入模式
 d+/+word 向右删除到首个word位置
 d+/+word 向左删除到首个word位置
 c+/+word 向右删除到首个word位置，插入模式
 c+/+word 向左删除到首个word位置，插入模式
## Dot Command
>记录Insert模式下所有行为，在Normal模式下redo
## 宏
>Normal模式q实行宏录制
 按任意char记录宏名称
 记录此后所有行为直至宏录制over
 Normal模式q退出宏录制
 {num}@宏名称redo宏行为
1. 克服了Dot Command模式只允许在Insert模式下记录的缺陷；
2. 可自定义多个宏行为；
## LeaderF
>

# 代码折
>折选中代码块 zf
 打开折代码块 zo
 再次将打开代码块折 zc
 删除折代码块 zd

# 寄存
>Visual模式选中代码+"+(a-z)+y 存储
 "+(a-z)+p 粘贴

# 窗口
>垂直切分窗口 :sp/Ctrl+w s
 切换窗口 Ctrl+w w
 窗口聚焦 Ctrl+w h/j/k/l 
 交换窗口位置 Ctrl+w x
 退出窗口 :q（;q）
 水平切分窗口 :vsp
 水平切分其他文件窗口 :vsp filename

# 书签
>当前文件书签标记 m+'a-z'
 书签行跳转 '+'a-z'
 书签列跳转 \`+'a-z'
 全局文件书签跳转 m+'A-Z'
 书签删除 :delmarks 'a-z' 'A-Z'
 
# number
>光标右侧首个num+=p {p}Ctrl+a
 光标右侧首个num-=p {p}Ctrl+x
 Visual Block模式下
 自增下标 g Ctrl+a
 字典序排序 :{col1,col2}sort
 
# 缩进
>{num}>> 当前行向下num行右缩进Tab  

# 配置
>显示隐藏文件（NodeTree） I


</file>
