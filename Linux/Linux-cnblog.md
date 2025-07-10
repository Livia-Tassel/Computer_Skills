[TOC]

## Linux 初识：

### Linux 简介：

![image-20241004104404548](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123011551-1042458251.png)

### 虚拟机：

​		虚拟机（Virtual Machine）指通过软件模拟的具有完整硬件**系统功能**的、运行在完全隔离环境中的完整**计算机系统**。在实体计算机中能够完成的工作在虚拟机中都能够实现。在计算机中创建虚拟机时，需要将实体机的**部分硬盘**和**内存容量**作为虚拟机的硬盘和内存容量。每个虚拟机都有独立的**CMOS**、硬盘和**操作系统**，可以像使用实体机一样对虚拟机进行操作。

### 虚拟机快照：

![PixPin_2024-10-04_17-33-36](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123010917-1971358653.jpg)

### 目录结构：

​		Linux 的目录结构为树型结构；Linux 无盘符概念，只有根目录／，所有文件都在其下面

![image-20241005110244987](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123010464-855773513.png)

### Linux 路径：

在 Linux 系统中，路径之间的层级关系，使用：／来表示
​在 Windows 系统中，路径之间的层级关系，使用：\ 来表示

## Linux 基础命令：

### 基础语法：

`command [-options] [parameter]`


command：命令本身
-options：[可选,非必填] 命令选项，可以通过选项控制命令的行为细节
parameter：[可选,非必填] 命令参数，用于命令的指向目标等

### 路径篇：

#### ls 命令：

```apl
# ls命令本体 ———— 以平铺的形式,陈列当前工作目录下内容
# Linux 系统终端在启动的时候默认会加载当前登录用户的 HOME 目录(Linux 系统的个人账户目录)作为当前工作目录
# 演示陈列 HOME 目录下内容
[tassel@localhost ~]$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
```

---

```apl
语法: ls [-a -l -h] [Linux路径]
-a (all)陈列所有文件(包括隐藏文件/文件夹)
-l (line)以列表的形式竖向排列展示文件
-h 以易于阅读的形式展示文件大小(-h选项需搭配-l使用)

# 语法中的选项允许组合使用
ls -al/-a-l/-la 均表示同时选中-a与-l选项
```

![image-20241005145505144](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123009851-1236704814.png)

#### cd-pwd 命令：

```apl
# cd ———— 更改当前所在工作目录 (Change Directory)
语法: cd [Linux路径]
cd命令无需选项,参数表示即将要切换到的工作目录,若无参数则表示回到用户HOME目录
```

---

```apl
# pwd ———— 查看当前工作目录 (Print Work Directory)
语法: pwd
pwd命令无选项,无参数
```

#### 特殊路径符：

绝对路径：以根目录为起点，路径描述以 / 开头
相对路径：以当前目录为起点，路径描述无需以 / 开头

| 特殊路径符 |                             作用                             |
| :--------: | :----------------------------------------------------------: |
|     .      | 表示当前目录，例如 cd./Desktop 表示切换到当前目录下的Desktop目录内与 cd Desktop 效果一致 |
|     ..     | 表示上一级目录，例如 cd.. 即可切换到上一级目录，cd../.. 切换到上二级目录 |
|     ~      | 表示HOME目录，例如 cd～ 即可切换到HOME目录或 cd～/Desktop 表示切换到HOME内的Desktop目录 |

```apl
# 在当前工作目录的上级目录有test文件夹,文件夹内有文件hello.txt,请描述文件的相对路径
../test/hello.txt
# 在HOME目录内有test文件夹,文件夹内有文件hello.txt,请描述文件的路径,需要使用符号~
~/test/hello.txt
```

### 文件篇：

#### mkdir 命令：

```apl
# mkdir ———— 创建新文件夹(Make Directory)
语法: mkdir [-p] Linux路径
Linux路径 表示要创建文件夹的路径(绝对路径、相对路径、特殊路径符均可)
-p 表示自动创建不存在的父级目录(适用于连续层级目录创建)
```

#### touch-cat-more 命令：

```apl
# touch ————— 创建指定文件
语法: touch Linux路径
Linux路径 表示要创建文件的路径
# cat ———— 查看指定文件内容
语法: cat Linux路径
Linux路径 表示要查看文件的路径
# more ———— 查看指定文件内容(支持翻页查看)
语法: more Linux路径
Linux路径 表示要查看文件的路径
在浏览模式下,空格表示翻页,q表示退出浏览模式
```

![image-20241005165809221](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123009086-1107664643.png)

#### cp-mv-rm 命令：

```apl
# cp ———— 复制文件/文件夹(Copy)
语法: cp [-r] 参数1 参数2
-r 用于复制文件夹使用,表示递归
参数1 Linux路径,表示被复制文件或文件夹路径
参数2 Linux路径,表示即将复制地址
```

![image-20241005171033073](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123008266-1886648034.png)

![image-20241005171302706](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123007520-1392487830.png)

```apl
# mv ———— 移动文件/文件夹(Move)
语法: mv 参数1 参数2
参数1 Linux路径,表示被移动文件或文件夹路径
参数2 Linux路径,表示即将移动到的地址,若目标地址不存在则进行重命名操作
```

![image-20241005171823332](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123007068-497176934.png)

![image-20241005172345238](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123006552-1270284987.png)

```apl
# rm ———— 删除文件/文件夹(Remove)
语法: rm [-r -f] 参数1 参数2 ... 参数n
-r 用于删除文件夹(使用-r选项后文件与文件夹均被删除)
-f (force)表示强制删除(不弹出提示信息)
参数1 参数2 ... 参数n 表示删除文件或文件夹路径
# rm命令支持通配符 *,用于做模糊匹配
rm -r test*  表示删除以test开头的文件/文件夹
rm -r *test  表示删除以test结尾的文件/文件夹
rm -r *test* 表示删除包含test的文件/文件夹
```

![image-20241006105025506](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123006056-671974432.png)

#### which-find 命令：

​		Linux命令本质上就是二进制可执行程序（等同于Windows系统中的.exe文件），通过which命令即可查找一系列命令程序存放的路径

```apl
# which ———— 查找指定命令存放路径
语法: which Linux命令
```

![image-20241006110702422](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123005638-1267912243.png)

```apl
# find ———— 查找指定文件/文件夹存放路径(按名称搜索)
语法: find 起始路径 -name "文件名"
# find命令结合通配符查找
find / -name "test*"  表示从根目录开始查找以test开头的文件/文件夹
```

![image-20241006112454826](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123005217-383018506.png)

```apl
# find ———— 查找指定文件/文件夹存放路径(按大小搜索)
语法: find 起始路径 -size +/-n[kMG]
+/- 表示大于/小于
n 表示数字
k/M/G 分别表示单位kb、MB、GB
# find命令结合通配符查找
find / -name "test*"  表示从根目录开始查找以test开头的文件/文件夹
```

#### grep-wc 命令：

```apl
# grep ———— 从文件中通过关键字过滤文件行
语法: grep [-n] 关键字 文件路径
-n 表示在结果中显示匹配行的行号
关键字 表示过滤的关键字(若关键字中带有空格或其他特殊符号建议使用" "包括)
文件路径 表示待过滤内容的文件路径,可作为内容输入端口
```

![image-20241006114713938](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123004717-1008225959.png)

```apl
# wc ———— 统计文件行数、单词数等
语法: wc [-c -m -l -w] 文件路径
-c 统计bytes数
-m 统计字符数
-l 统计行数
-W 统计单词数
文件路径 表示被统计的文件,可作为内容输入端口
# 若无选项则输出结果为 "行数 单词数 字节数 文件名"
```

#### 管道符：

​		将管道符左侧命令结果作为右侧命令输入（允许嵌套使用）

![image-20241006143241979](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123004142-1314767715.png)

![image-20241006143423087](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123003664-1571155704.png)

### 拓展篇：

#### echo 命令：

```apl
# echo ———— 在命令行内输出指定内容
语法: echo 输出内容(输出内容过于复杂使用" "包括)
```

#### 反引号 `：

```apl
# `` ———— 反引号中的内容将作为命令执行
echo `pwd` 将输出pwd命令的结果,而非字符"pwd"
```

#### 重定向符：

\>   将左侧命令结果**覆盖**写入右侧指定文件中
\>> 将左侧命令结果**追加**写入右侧指定文件中

![image-20241006152629417](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123003135-214914433.png)

![image-20241006153044700](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123002303-1957337386.png)

#### tail 命令：

```apl
# tail ———— 查看文件尾部内容,跟踪文件最新更改
语法: tail [-f -num] Linux路径
Linux路径 表示被跟踪的文件路径
-f 表示持续跟踪
-num 表示查看尾部行数(默认为10)
```

### VIM编辑器：

```apl
# VIM 编辑器
语法: vim 文件路径(若文件不存在,则创建新文件进行编辑)
```
<img src="./Linux.assets/image-20241006154451616.png" alt="image-20241006154451616" style="zoom:67%;" />

#### 工作模式：

|              模式              |                             描述                             |
| :----------------------------: | :----------------------------------------------------------: |
|    命令模式（Command mode）    | 所敲的按键编辑器均理解为命令，以命令驱动执行不同的功能（此模式不能自由进行文本编辑） |
|    输入模式（Insert mode）     |     正常的编辑模式、插入模式（可对文件内容进行自由编辑）     |
| 底线命令模式（Last line mode） |             以"："开始，通常用于文件的保存、退出             |

#### 命令模式快捷键：

|     快捷键     |              作用              |
| :------------: | :----------------------------: |
|       i        |   在当前光标位置进入输入模式   |
|       I        |   在当前行的开头进入输入模式   |
|       a        | 在当前光标位置之后进入输入模式 |
|       A        |   在当前行的结尾进入输入模式   |
|       o        |  在当前光标下一行进入输入模式  |
|       O        |  在当前光标上一行进入输入模式  |
|  pageup(PgUp)  |            向上翻页            |
| pagedown(PgDn) |            向下翻页            |
|       /        |            搜索模式            |
|       n        |            向下搜索            |
|       N        |            向上搜索            |
|       dd       |         删除光标所在行         |
|      ndd       |      删除当前光标向下n行       |
|       yy       |           复制当前行           |
|      nyy       |      复制当前及其下方n行       |
|       p        |              粘贴              |
|       u        |              撤销              |
|    Ctrl + r    |            反向撤销            |
|       dG       |   从当前行开始，向下全部删除   |
|      dgg       |   从当前行开始，向上全部删除   |
|       d$       | 从当前光标开始，删除到本行结尾 |
|       d0       | 从当前光标开始，删除到本行开头 |
|      Esc       |          回到命令模式          |

#### 底线命令模式快捷键：

|   快捷键    |     作用     |
| :---------: | :----------: |
|    ：wq     |  保存并退出  |
|     ：w     |    仅保存    |
|     ：q     |    仅退出    |
|    ：q!     |   强制退出   |
|  ：set nu   |   显示行号   |
| ：set paste | 设置粘贴模式 |

## Linux权限管控：

### root用户：

​		普通用户的权限一般在其 HOME 目录内是不受限的，除 HOME 目录，大多数地方，普通用户仅有只读和执行权限，无修改权限。

### 用户切换：

#### su-exit 命令：

```apl
# su ———— 切换账户(Switch User)
语法: su [-] [用户名]
- 表示是否在切换用户后加载环境变量
用户名 表示要切换的用户(默认为root)
# exit ———— 回退到上用户
或 Ctrl键+d
```

#### sudo 命令：

​		不建议长期使用root用户避免带来系统损坏，可以使用sudo命令，为普通的命令授权，临时以root身份执行。但是并不是所有的用户都有权利使用sudo命令，我们需要为普通用户配置sudo认证

```apl
# sudo ———— 临时授权root权限
语法: sudo 命令
# 配置 sudo权限
1.切换到root用户,执行visudo命令
2.在文件最后添加: 用户名 ALL=(ALL)   NOPASSWD: ALL
3.保存退出即可
```

### 用户与用户组：

|              指令               |                             功能                             |
| :-----------------------------: | :----------------------------------------------------------: |
|            groupadd             |                        创建用户组[^1]                        |
|            groupdel             |                          删除用户组                          |
|     useradd [-g -d] 用户名      | -g 指定用户所在的用户组，不指定 -g，系统会创建同名用户组并将其自动加入，如已存在同名组，必须使用 -g<br />-d 指定用户的 HOME 路径，若不指定，HOME 目录默认：/home/用户名 |
|       userdel [-r] 用户名       | -r 删除指定用户的 HOME 目录，若不使用 -r，仅删除用户而保留 HOME目录 |
|           id [用户名]           |    查看指定用户所属组，若不提供用户名则查看当前用户所属组    |
|    usermod -aG 用户组 用户名    |                      修改指定用户所属组                      |
| getent passwd<br />getent group |   查看当前系统所有用户信息<br />查看当前系统所有用户组信息   |

![image-20241006202953207](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123001804-2117380740.png)

### 权限信息：

![image-20241006205005986](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123001119-1826593740.png)

​																		 序号1，表示文件、文件夹的权限控制信息

![image-20241006205241961](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123000630-464769097.png)

​                                                                       `r 表示读权限 w 表示写权限 x 表示执行权限`

​																		      序号2，表示文件、文件夹所属用户
​																	    	序号3，表示文件、文件夹所属用户组

​                                                                **针对文件、文件夹的不同，rwx 的含义有细微差别**

| 指令 |        文件        |               文件夹               |
| :--: | :----------------: | :--------------------------------: |
|  r   |    查看文件内容    |     查看文件夹内容，类ls 命令      |
|  w   |     修改此文件     | 在文件夹内：创建、删除、改名等操作 |
|  x   | 将文件作为程序执行 | 更改工作目录到此文件夹，即cd 命令  |

### 权限修改：

#### chmod 命令：

​		仅有文件、文件夹所属用户或root用户可以修改对应权限信息

```apl
# chmod ———— 修改用户权限
语法: chmod [-R] 权限 文件/文件夹
-R 表示对文件夹内所有内容应用相同操作
# 演示
chmod u=rwx, g=rx, o=x hello.txt 将文件权限修改为:rwxr-x--x
chmod -R u=rwx, g=rx, o=x test 将文件夹test以及文件夹内全部内容权限设置为：rwxr-x--x
其中u表示user所属用户权限,g表示group组权限,o表示other其它用户权限
```

---

```apl
# 快捷修改
chmod 751 hello.txt
```

<img src="./Linux.assets/image-20241006214737488.png" alt="image-20241006214737488" style="zoom:50%;" />

#### chown 命令：

​		仅有 root 用户可以修改文件/文件夹所属用户或用户组

```apl
# chown ———— 修改文件/文件夹所属用户或用户组
语法: chown [-R] [用户][:][用户组] 文件/文件夹
-R 表示对文件夹内所有内容应用相同操作
: 用于分隔用户与用户组
# 演示
chown root hello.txt 将hello.txt所属用户修改为root
chown :root hello.txt 将hello.txt所属用户组修改为root
chown root:tassel hello.txt 将hello.txt所属用户修改为root,用户组修改为tassel
chown -R root test 将文件夹test的所属用户修改为root并对文件夹内全部内容应用同样规则
```

## linux实用操作：

### 实用快捷键：

|   快捷键    |                  作用                  |
| :---------: | :------------------------------------: |
|  Ctrl键+L   |           清屏（clear命令）            |
|  Ctrl键+C   |              强制终止程序              |
|  Ctrl键+D   | 退出账户登录或退出某些特定程序专属页面 |
|   history   |              查看历史命令              |
| ！命令前缀  |       自动执行首次匹配前缀的命令       |
|  Ctrl键+R   |            搜索历史命令[^2]            |
|  Ctrl键+A   |              跳至命令开头              |
|  Ctrl键+E   |              跳至命令结尾              |
| Ctrl键+左键 |            向左移动单个单词            |
| Ctrl键+右键 |            向右移动单个单词            |

### 软件：

#### yum 命令：

​		yum程序：RPM包软件管理器，用于自动化安装配置Linux软件，并可以自动解决依赖问题

```apl
# yum ———— 软件搜索、安装、卸载
语法: yum [-y] [install | remove | search] 软件名称
-y 表示自动确认,无需手动确认安装或卸载过程
install 安装
remove 卸载
search 搜索
# yum命令需要root权限且需要联网(CentOS 7.9 于2024-6-30停止维护yum程序需自行安裝)
```

#### systemctl 命令：

​		Linux系统很多软件（内置或第三方）均支持使用 systemctl命令 控制：启动、停止、开机自启。能够被systemctl管理的软件通常也称之为：服务

```apl
# systemctl ———— 控制软件启动、停止、开机自启
语法: systemctl start | stop | status | enable | disable 服务名
start   启动
stop    关闭
status  查看状态
enable  开启开机自启
disable 关闭开机自启
# Linux系统内置服务
NetworkManager 主网络服务
network 副网络服务
firewalld 防火墙服务
sshd, ssh服务(FinalShell远程登录Linux使用的即为此服务)
```

### 软连接：

​		在Linux系统中创建软链接，可以将文件、文件夹链接到其它位置，类似于windows系统中的《快捷方式》

#### ln 命令：

```apl
# ln ———— 创建软连接
语法: ln -s 参数1 参数2
-s 创建软连接
参数1 被链接的文件或文件夹
参数2 将要链接目的地
```

![image-20241007195707797](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015123000183-485083191.png)

### 日期与时间：

#### date 命令：

```apl
# date ———— 查看系统时间
语法: date [-d] [+格式化字符串]
-d 表示按照指定字符串显示日期(常用于日期计算)
格式化字符串 通过特定的字符串标记控制显示的日期格式
```

| 格式化字符串 | 时间标记 |                    描述                     |
| :----------: | :------: | :-----------------------------------------: |
|      %Y      |   year   |                     年                      |
|      %y      |   year   |                年份后两位数                 |
|      %m      |  month   |                    月份                     |
|      %d      |   day    |                     日                      |
|      %H      |   hour   |                     时                      |
|      %M      |  minute  |                     分                      |
|      %S      |  second  |                     秒                      |
|      %s      |  second  | 自 1970-01-01 00：00：00 UTC 至当前时间秒数 |

![image-20241007200748446](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122959677-580336309.png)

![image-20241007201455200](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122959274-11297005.png)

#### 修改时区（亚洲时区）：

```apl
# 修改时区为亚洲时区
rm -f /etc/localtime
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 使用ntp程序手动校准时间
ntpdate -u ntp.aliyun.com
```

![image-20241007202125902](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122958882-21782530.png)

### IP地址与主机名：

​		每台联网电脑均有一个IP地址，用于与其它**计算机进行通讯**，IP地址主要有2个版本，**V4版本**与V6版本，其中V4版本较为常见，如192.168.88.01就是标准的IPV4地址

#### 基础指令：

|              指令               |      作用      |
| :-----------------------------: | :------------: |
|            ifconfig             | 查看本机IP地址 |
|            hosthome             | 查看系统主机名 |
| hostnamectl set-hostname 主机名 |   修改主机名   |

#### 特殊IP地址：

> 127.0.0.1 表示本机地址

> 0.0.0.0 地址表示范围较广：
> 1.用于指代本机
> 2.在端口绑定中用于确定绑定关系
> 3.在某些IP地址限制中，表示所有IP的意思，如放行规则设置为0.0.0.0 表示允许任意IP访问

#### 域名解析：

![image-20241007204410671](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122958353-1773678252.png)

#### IP固定：

​		虚拟机的Linux操作系统，其IP地址是通过DHCP服务获取的，DHCP服务会动态获取IP地址，即每次重启设备后都会重新获取，可能导致IP地址频繁变更

```apl
# ens33网卡设置
IPADDR="192.168.88.130"
NETMASK="255.255.255.0"
GATEWAY="192.168.88.2"
DNS1="192.168.88.2"
```

### 网络传输：

#### ping 命令：

```apl
# ping ———— 检查网络服务器是否连通
语法: ping [-c num] ip/主机名
-c 表示检查次数(忽略选项将无限次数持续检查)
ip/主机名 表示被检查的服务器的IP地址或主机名地址
```

![image-20241008102227711](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122957557-1249459245.png)

#### wget 命令：

```apl
# wget ———— 命令行内下载网络文件
语法: wget [-b] url
-b 表示后台下载,下载日志将写入当前工作目录的wget-log文件中(可使用tail命令持续跟踪下载进度)
url 下载链接
```

#### curl 命令：

```apl
# curl ———— 发送网络请求用于下载文件、获取信息等
语法: curl [-O] url
-O 用于下载文件(忽略参数即仅发送网络请求不进行下载操作)
url 向发起请求的网络地址
```

![image-20241008103304917](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122957035-2016533474.png)

#### 端口：

##### 简介：

​		IP地址通常只能用于锁定某台计算机，而想要更加精确地锁定计算机上的某个程序则需要依靠计算机的端口来实现

![image-20241008103838209](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122956370-1494426664.png)

>物理端口：又称为接口，为可见的端口，如USB接口，RJ45网口，HDMI端口等
>虚拟端口：指计算机内部的端口，是不可见的，用于操作系统和外部进行交互使用

>公认端口：1~1023，通常用于系统内置或知名程序的预留使用，如SSH服务的22端口，HTTPS服务的443端，非特殊需要，不可占用此范围的端口
>注册端口：1024~49151，通常可以随意使用，用于松散地绑定某些程序\服务
>动态端口：49152~65535，通常不会固定绑定程序，而是当程序对外进行网络链接时用于临时使用

##### nmap 命令：

```apl
# nmap ———— 查看主机端口占用情况
语法: nmap IP地址
```

![image-20241008105055663](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122955854-2084906108.png)

##### netstat 命令：

```apl
# netstat ———— 查看指定端口占用情况
语法: netstat -anp | grep 端口号
```

![image-20241008105724855](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122955105-1131199123.png)

### 进程管理：

#### 进程：

> 程序运行在操作系统中，是被操作系统所管理的
> 为管理运行的程序，每个程序在运行的时候，便被操作系统注册为系统中的进程
> 并会为每个进程都分配独有的进程ID（进程号）

#### ps 命令：

```apl
# ps ———— 查看Linux系统进程信息
语法: ps [-e -f]
-e 显示所有进程
-f 以完全格式化的形式展示信息
```

![image-20241008112341774](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122954574-1850594100.png)

#### kill 命令：

```apl
# kill ———— 关闭进程
语法: kill [-9] 进程ID
-9 表示强制关闭进程
```

### 主机状态：

#### 资源占用：

##### top 命令：

```apl
# top ———— 查看CPU、内存占用情况
语法: top
```

###### 命令选项：

|   选项    |                             功能                             |
| :-------: | :----------------------------------------------------------: |
|  -p PID   |                     仅显示某个进程的信息                     |
|  -d num   |               设置刷新时间（单位秒，默认5秒）                |
|    -c     |             显示产生进程的完整命令（默认进程名）             |
|  -n num   |                         指定刷新次数                         |
|    -b     | 以非交互非全屏模式运行，以批次的方式执行top<br />通常配合 -n选项 指定输出统计信息次数，将输出结果重定向到指<br/定文件，例如 top -b -n 3 > /tmp/top.tmp |
|    -i     |          不显示任何闲置（idle）或无用（zombie）进程          |
| -u 用户名 |                    查找特定用户启动的进程                    |

###### 交互式按键（非-b选项启动）：

| 按键 |                 功能                  |
| :--: | :-----------------------------------: |
|  h   |             显示帮助画面              |
|  c   | 显示产生进程的完整命令，等同于 -c选项 |
|  f   |          选择需要展示的项目           |
|  M   |      根据驻留内存大小（RES）排序      |
|  P   |     根据CPU使用百分比大小进行排序     |
|  T   |       根据时间/累计时间进行排序       |
|  E   |         切换顶部内存显示单位          |
|  e   |         切换进程内存显示单位          |
|  l   |    切换显示平均负载和启动时间信息     |
|  i   | 不显示闲置或无用的进程，等同于 -i选项 |
|  t   |          切换显示CPU状态信息          |
|  m   |           切换显示内存信息            |

###### 参数详解：

![image-20241008212547112](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122953956-1237631242.png)

|  参数   |                            描述                             |
| :-----: | :---------------------------------------------------------: |
|   PID   |                           进程ID                            |
|  USER   |                        进程所属用户                         |
|    S    | 进程状态（S休眠，R运行，Z僵死状态，N负数优先级，I空闲状态） |
|  %CPU   |                        进程占用CPU率                        |
|  %MEM   |                       进程占用内存率                        |
| COMMAND |                进程的命令名称或程序文件路径                 |

详情参数解析：[top命令详解](https://blog.csdn.net/weixin_45465395/article/details/115728520#:~:text=top命令经常用来监)

#### 磁盘信息：

##### df 命令：

```apl
# df ———— 查看磁盘使用情况
语法: df [-h]
-h 人性化单位显示
```

![image-20241008212831312](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122953540-2085752483.png)

##### iostat 命令：

```apl
# iostat ———— 查看CPU、磁盘的相关信息
语法: iostat [-x] [num1] [num2]
-x 显示更多信息
num1 刷新间隔
num2 刷新次数
```

###### 参数详解：

![image-20241008213248364](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122952903-1071319120.png)

| 参数  |            描述            |
| :---: | :------------------------: |
| rKB/s | 每秒发送到设备的读取请求数 |
| wKB/s | 每秒发送到设备的写入请求数 |
| %util |         磁盘利用率         |

#### 网络状态：

##### sar 命令：

```apl
# sar ———— 查看网络相关统计
语法: sar -n DEV num1 num2
-n 查看网络
DEV 表示查看网络接口
num1 刷新间隔(默认单次)
num2 查看次数(默认无限次)
```

###### 参数详解：

![image-20241008214053139](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122952192-87631592.png)

|  参数  |               描述               |
| :----: | :------------------------------: |
| rxKB/S | 每秒钟接受的数据包大小，单位为KB |
| txKB/S | 每秒钟发送的数据包大小，单位为KB |

### 环境变量：

​		环境变量是操作系统在运行的时候记录的某些关键性信息（键值对），用以辅助系统运行，而环境变量中 PATH项目 的值则记录了系统执行任何命令的搜索路径

> /usr/local/bin
> /usr/bin
> /usr/local/sbin
> /usr/sbin
> /home/tassel/.local/bin
> /home/tassel/bin

#### 基础指令：

|    指令     |          功能          |
| :---------: | :--------------------: |
|     env     |    查看系统环境变量    |
| $环境变量名 | 取出环境变量名对应的值 |

#### 自定义环境变量：

##### 普通环境变量：

```apl
# 临时配置 ———— export命令
语法: export 变量名=变量值 (不可有空格)
# 永久配置
·针对当前用户生效,配置在当前用户 ~/.bashrc 文件中
·针对所有用户生效,配置在系统 /etc/profile 文件中
# 通过语法 source 配置文件,进行立刻生效或重新登录FinalShell生效
```

![image-20241008220511785](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122951756-1823882668.png)

##### PATH环境变量：

​		环境变量PATH项目中记录了系统执行命令的搜索路径，将自定义程序搜索路径加入到PATH环境变量中，即可实现在任意工作目录下执行指定程序

`语法: export PATH=$PATH:自定义路径`[^3]

![image-20241009164156502](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122951168-972066829.png)

### 上传与下载：

#### FinalShell 软件：

![image-20241009165233038](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122950413-626293251.png)

#### rz-sz 命令：

```apl
# sz ————— 文件下载到本地
语法: sz 文件名
# 文件会自动下载到桌面的fsdownload文件夹中
# rz ———— 上传本地文件(适用于小文件)
语法: rz
```

### 压缩与解压：

#### 常见压缩格式：

<img src="./Linux.assets/image-20241009170003349.png" alt="image-20241009170003349" style="zoom: 50%;" />

> .tar，称之为tarball，归档文件，即简单地将文件组装到一个.tar的文件内，并没有过多文件体积的减少，仅为封装
> .gz，也常见为.tar.gz、gzip格式压缩文件，即使用gzip压缩算法将文件压缩，可以极大地减少压缩后的体积

#### tar 命令：

```apl
# tar ———— 文件压缩与解压
语法: tar[-c -v -x -f -z -C] 参数1 参数2 ... 参数N
```

##### 选项描述：


| 选项 |                           描述                            |
| :--: | :-------------------------------------------------------: |
|  -c  |                创建压缩文件，用于压缩模式                 |
|  -v  |             显示压缩、解压过程，用于查看进度              |
|  -x  |                         解压模式                          |
|  -f  | 要创建文件或解压的文件（-f 选项必须在所有选项中处于末尾） |
|  -z  |            gzip模式（否则为普通的tarball格式）            |
|  -C  |               选择解压目的地，用于解压模式                |

##### 选项组合：

```apl
# 压缩
1.将1.txt、2.txt、3.txt压缩到test.tar文件内
tar-cvf test.tar 1.txt 2.txt 3.txt
2.将1.txt、2.txt、3.txt压缩到test.tar.gz文件内(使用gzip模式)
tar -zcvf test.tar.gz 1.txt 2.txt 3.txt
# 解压
1.解压test.tar,将文件解压至当前目录
tar -xvf test.tar
2.解压test.tar,将文件解压至指定目录
tar -xvf test.tar -C /home/tassel
3.以Gzip模式解压test.tar.gz,将文件解压至指定目录
tar -zxvf test.tar.gz -C /home/tassel
```

#### zip 命令：

```apl
# zip ———— 压缩文件为zip压缩包
语法: zip [-r] 参数1 参数2 ... 参数N
-r 用于含文件夹的压缩
```

---

```apl
# 示例
1.将a.txt b.txt c.txt 压缩到test.zip文件内
zip test.zip a.txt b.txt c.txt
2.将test、tassel文件夹和a.txt文件,压缩到test.zip文件内
zip -r test.zip test tassel a.txt
```

#### unzip 命令：

```apl
# unzip ———— 解压zip压缩包
语法: zip [-d] 压缩文件
-d 指定解压目的地
```

---

```apl
# 示例(若解压有同名文件将覆盖且不会提示)
1.将test.zip解压到当前目录
unzip test.zip
2.将test.zip解压到指定目录
unzip test.zip -d /home/tassel
```

## 实战软件部署：

### MYSQL：

#### MYSQL5.7版本：

##### 安装：

1.配置yum仓库：


 ```apl
 # 更新密钥(导入MYSQL仓库密钥)
 rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
 
 # 安装MYSQL yum库(配置MySQL的yum仓库)
 rpm -Uvh http://repo.mysql.com//mysql57-community-release-el7-7.noarch.rpm
 ```

2.安装MYSQL：

```apl
# yum安装Mysql
yum -y install mysql-community-server
```

3.启动MYSQL并配置开机自启动：

```apl
systemctl start mysqld		# 启动
systemctl enable mysqld		# 开机自启
# MYSQL安装完成后会自动配置为名叫：mysqld的服务,可被systemctl所管理
```

4.检查MYSQL运行状态：

```apl
systemctl status mysqld
```

##### 配置：

​		配置管理员用户root的密码以及允许远程登录的权限

1.获取MySQL的初始密码

```apl
# 通过grep命令在 /var/log/mysqld.log文件中过滤temporary password关键字,得到初始密码
grep 'temporary password' /var/log/mysqld.log
```

![image-20241010171555816](https://img2023.cnblogs.com/blog/3482954/202410/3482954-20241015122949707-1275800408.png)

2.登陆MySQL数据库系统

```apl
# 登陆MySQL数据库系统
mysql -uroot -p
-u 登陆的用户(MySQL数据库的管理员用户root)
-p 表示使用密码登陆
# 执行完毕后输入刚得到的初始密码即可进入MySQL数据库
```

3.修改root用户密码

```sql
# 在MySQL控制台内执行
ALTER USER 'root'@'localhost' IDENTIFIED BY '密码';
# 密码需符合：大于8位、有大写字母、有特殊符号
```

[扩展]：配置root简单密码（仅供学习与测试中使用）

```sql
# 设置简单密码需要降低MySQL的密码安全级别
set global validate_password_policy=LOW; # 密码安全级别低
set global validate_password_length=4;	 # 密码长度最低4位
ALTER USER 'root'@'localhost' IDENTIFIED BY '简单密码';
```

[扩展]：配置root运行远程登录

​		默认情况下，root用户是不允许远程登录的，只允许在MySQL当前所在的Linux服务器登陆上MySQL系统。请注意，允许root用户远程登录会带来安全风险

```apl
# 授权root远程登录
grant all privileges on *.* to root@"IP地址" identified by '密码' with grant option;  
IP地址 表示允许登陆的IP地址(也可以填写% 表示允许任何地址)
密码 表示给远程登录独立设置密码(和本地登陆的密码可以不同)
# 刷新权限
flush privileges;
```

4.退出MySQL控制台页面

```apl
# 退出命令
exit
```

5.检查端口

​		MySQL默认绑定3306端口，可以通过端口占用检查MySQL的网络状态

```apl
netstat -anp | grep 3306
```

#### MYSQL8.0版本（需先删除原MYSQL）：

[MySQL8.0安装](https://www.bilibili.com/video/BV1n84y1i7td?p=45&vd_source=8dc741e421f8ee598aa7096f9035a137)

### Tomcat：

​		Tomcat 是由 Apache 开发的 **Servlet 容器**，实现了对 Servlet 和 JSP 的支持，并提供了作为**Web服务器的特有功能**，如Tomcat管理和控制平台、安全域管理和Tomcat阀等。简单来说，Tomcat是**WEB应用程序的托管平台**，可以让用户编写的WEB应用程序被Tomcat所托管，并提供网站服务，即让用户开发的WEB**应用程序，变成可以被访问的网页**。

> 本次安装使用的Tomcat版本是：10.1.31版本，需要Java（JDK）版本最低为JDK11
>
> 案例演示中的JDK版本是：JDK-17.0.12版本

#### 安装JDK环境：

1.下载JDK软件（安装包中自行查找）

`jdk-17_linux-x64_bin.tar.gz`

2.通过FinalShell，上传下载好的JDK安装包

3.创建文件夹，部署JDK，将JDK和Tomcat都安装部署到：/export/server 内

```apl
mkdir -p /export/server
```

4.解压缩JDK安装文件

```apl
tar -zxvf jdk-17_linux-x64_bin.tar.gz -C /export/server
```

5.配置JDK软链接

```apl
ln -s /export/server/jdk-17.0.12 /export/server/jdk
```

6.配置JAVA_HOME环境变量，以及将$JAVA_HOME/bin文件夹加入PATH环境变量中

```apl
# 编辑/etc/profile文件
export JAVA_HOME=/export/server/jdk
export PATH=$PATH:$JAVA_HOME/bin
```

7.生效环境变量

```apl
source /etc/profile
```

8.配置java执行程序软链接

```apl
# 删除系统自带的java程序
rm -f /usr/bin/java
# 软链接自己安装的java程序
ln -s /export/server/jdk/bin/java /usr/bin/java
```

9.执行验证

```apl
java -version
```

#### 解压并部署Tomcat：

1.首先，放行Tomcat需要使用的8080端口的外部访问权限

> CentOS系统默认开启了防火墙，阻止外部网络流量访问系统内部
>
> 所以，如果想要Tomcat可以正常使用，需要对Tomcat默认使用的8080端口进行放行
>
> 两种操作方式：
>
> 1. 关闭防火墙
> 2. 配置防火墙规则，放行端口

```apl
# 方式1:关闭防火墙
systemctl stop firewalld		# 关闭防火墙
systemctl disable firewalld		# 停止防火墙开机自启

# 方式2:放行8080端口的外部访问
firewall-cmd --add-port=8080/tcp --permanent		
# --add-port=8080/tcp表示放行8080端口的tcp访问,--permanent表示永久生效
firewall-cmd --reload		    # 重新载入防火墙规则使其生效
```

2.创建Tomcat用户

```apl
# root用户操作
useradd tomcat
# 为Tomcat用户配置密码(可选)
passwd tomcat
```

3.下载Tomcat安装包

```apl
# root用户操作
wget https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.31/bin/apache-tomcat-10.1.31-src.tar.gz
# 若出现https相关错误,可以使用--no-check-certificate选项
wget --no-check-certificate https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.31/bin/apache-tomcat-10.1.31-src.tar.gz
```

4.解压Tomcat安装包

```apl
# root用户操作,否则无权限解压到/export/server内,除非修改此文件夹权限
tar -zxvf apache-tomcat-10.1.31-src.tar.gz -C /export/server
```

5.创建Tomcat软链接

```apl
# root用户操作
ln -s /export/server/apache-tomcat-10.1.31-src /export/server/tomcat
```

6.修改Tomcat安装目录权限

```apl
# root用户操作,同时对软链接和tomcat安装文件夹进行修改,使用通配符*进行匹配
chown -R tomcat:tomcat /export/server/*tomcat*
```

7.切换到Tomcat用户，并启动Tomcat（Java环境与Tomcat环境不匹配无法正常启动）

```apl
su - tomcat
/export/server/tomcat/bin/startup.sh
```

8.Tomcat默认启动在8080端口

```apl
netstat -anp | grep 8080
```

9.打开浏览器，输入：http://centos:8080或http://192.168.88.130:8080

使用主机名（需配置好本地的主机名映射）或IP地址访问Tomcat的WEB页面

![image-20221017223915498](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2022/10/17/20221017223915.png)

### Nginx：

​		Nginx (engine x) 是高性能的HTTP和反向代理web服务器，同时也提供了IMAP/POP3/SMTP服务。Nginx还可以托管用户编写的WEB应用程序成为可访问的网页服务，同时也可以作为流量代理服务器，控制流量的中转。

1.安装yum依赖程序

```apl
# root执行
yum install -y yum-utils
```

2.手动添加Nginx的yum仓库

yum程序使用的仓库配置文件存放在：`/etc/yum.repo.d`内

```apl
# 创建文件使用vim编辑
vim /etc/yum.repos.d/nginx.repo
# 填入如下内容并保存退出
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

[nginx-mainline]
name=nginx mainline repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=0
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
```

3.通过yum安装最新稳定版的Nginx

```apl
# root执行
yum install -y nginx
```

4.启动（Apache占用 tcp6的80端口，导致Nginx无法正常启动）

```apl
# Nginx自动注册systemctl系统服务
systemctl start nginx		# 启动
systemctl stop nginx		# 停止
systemctl status nginx		# 运行状态
    systemctl enable nginx		# 开机自启
systemctl disable nginx		# 关闭开机自启
```

5.配置防火墙放行

Nginx默认绑定80端口，需要关闭防火墙或放行80端口

```apl
# 方式1:关闭防火墙
systemctl stop firewalld		# 关闭
systemctl disable firewalld		# 关闭开机自启

# 方式2:放行80端口
firewall-cmd --add-port=80/tcp --permanent	    # 放行tcp规则下的80端口，永久生效
firewall-cmd --reload						  # 重新加载防火墙规则
```

6.启动后浏览器输入Linux 服务器的IP地址或主机名即可访问：http://192.168.88.130 或 http://centos

> ps：80端口是访问网站的默认端口，所以后面无需跟随端口号
>

### RabbitMQ：





















 [^1]：关于用户与用户组的命令均需使用root权限

 [^2]：得到历史命令后，回车即执行命令，键盘左/右键即可得到命令（不执行）

 [^3]：案例中环境变量配置内容为：export PATH=$PATH:/root/myenv



