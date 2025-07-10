<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">Git Init</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

### 常见错误：

#### 错误 1：路径名或者变量有空格时候，会造成参数太多的错误提示

`bash: cd: too many arguments`
解决方案：使用双引号将带有空格的部分括住

#### 错误2：Git Bash 中的路径切换为正斜杠 " /  "，而不是 Windows 中的反斜杠 "  \ "

#### ![img](./initgit.assets/image-20240725103921114.png)

正确示例：

```bash
Users MINGW64 /d
$ cd D:/"yi yi"/文档合集/新技能新气象/计算机/Git实践案例
Users MINGW64 /d/yi yi/文档合集/新技能新气象/计算机/Git实践案例
```

#### 错误3：使用某些查找命令时，文本过长 Git 会自动进入浏览模式，此时无法再输入任何指令

```bash
commit version
Author: User's name <email>
Date:   Sun Jul 21 21:31:06 2024 +0800

    v1
(END)
```

解决方案：英文键盘 Q 退出

#### 错误4：向 github 推送或者下载代码时网络超时

git clone 或 git pull 等操作时出现 " fatal: unable to access ' https://github.com/…/.git ': Recv failure Connection was reset "的报错。这个问题通常是由网络连接问题或代理设置不正确导致的。
解决方案：通过在终端执行以下命令，可以取消 Git 的代理设置：

```bash
git config --global --unset http.proxy 
git config --global --unset https.proxy
```

#### 错误5：windows 下解决Git报错： LF will be replaced by CRLF the next time Git touches it

原因：
Uinx/Linux 采用换行符LF表示下一行（LF：LineFeed），即：\n；
Dos 和 Windows 采用回车+换行CRLF表示下一行（CRLF：CarriageReturn LineFeed），即：\r\n；
Mac OS采用回车CR表示下一行（CR：CarriageReturn），即：\r。
解决方案：
`git config --global core.autocrlf true`

###  基本 Git 命令行：

|                             指令                             |                             作用                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                           git init                           |           初始化当前路径下的文件夹，开启 Git 管理            |
|                          git status                          |                   显示当前文件夹中所有文件                   |
|           git add 文件名(test.txt)<br />git add .            | 将指定文件管理权限交于 Git<br />将当前文件夹中所有文件管理权限交于 Git |
|                      git commit -m 'v1'                      | 将当前 Git 所管理的文件[^1]生成新的版本 （其中 ' ' 中为描述信息） |
| git log<br />git log --graph<br />git log --graph --pretty=format:"%h %s" | 查看版本历史提交记录<br />以图形化方式查看版本历史提交记录<br />以格式化流程查看版本历史提交记录 |
|                   git reset --hard 版本号                    |       回滚到对应版本（此时文件夹中的内容也会相应改变）       |
|                          git reflog                          |          查看历史所有版本（包括回滚版本之后的版本）          |
| git checkout 文件名(test.txt)<br />git reset HEAD 文件名(test.txt) | 将工作区的未管文件转化为已管文件（通过撤销修改或删除新文件实现）<br />将暂存区文件转化为工作区的未管文件（即 add 命令的逆操作） |

### Git分区：

|       区域       |                           文件类型                           |
| :--------------: | :----------------------------------------------------------: |
| 工作区（文件夹） |        已管文件<br />未管文件[^2]（新文件、修改文件）        |
|      暂存处      |     通过add命令提交的文件（已管文件）即均存储在暂存区中      |
|      版本库      | 通过commit命令将暂存区中的已管文件所生成的版本存储在版本库中 |

### 分支：

:star2:Git 管理生成的不同版本之间并不是独立的，新版本实际上只会保留新修改的文件，而其余文件则通过指针指向之前版本。
![image-20240722093029639](./initgit.assets/image-20240722093029639.png)
通过分支即可以实现项目 bug 的紧急修复：
1.将当前正在开发但未完成的版本形成新分支（dev)
2.修改 bug 的版本也形成新分支（bug)
3.完成后合并到主干 master

#### 分支Git命令行：

|         指令         |                          作用                          |
| :------------------: | :----------------------------------------------------: |
|      git branch      |                  显示目前所处分支[^3]                  |
|  git branch 分支名   | 创建新分支（指向当前所处分支的当前版本，而非最新版本） |
| git checkout 分支名  |                     跳转到对应分支                     |
| git branch -d 分支名 |                      删除对应分支                      |
|   git merge 分支名   |     合并[^4]对应分支的对应版本到当前分支的当前版本     |

### 代码托管（github）：

|               指令               |           作用           |
| :------------------------------: | :----------------------: |
| git remote add 别名 远程仓库地址 |   为远程仓库起别名[^5]   |
|     git push -u 别名 分支名      |    向远程仓库推送代码    |
|      git clone 远程仓库地址      | 首次拷贝远程仓库代码[^6] |
|       git pull 别名 分支名       |    选择性更新本地代码    |

![屏幕截图 2024-07-24 205709](./initgit.assets/image-20240722093029637.png)

### 补充：GitBash / Mac 常见指令：

|                     指令                      |                   作用                   |
| :-------------------------------------------: | :--------------------------------------: |
|                  cat 文件名                   |               查看文件内容               |
|                     cd ..                     |              回退上一级目录              |
|                      ls                       |              浏览当前文件夹              |
|                      pwd                      |           显示当前目录的路径名           |
| mkdir 目录名<br />rmdir 目录名<br />rm 文件名 |   新建目录<br />删除目录<br />删除文件   |
|                  file 文件名                  |               显示文件类型               |
|            open 文件名<br />open .            | 使用默认的程序打开文件<br />打开当前目录 |
|                     date                      |         显示系统的当前日期和时间         |
|                     clear                     |            清除屏幕或窗口内容            |
|                    whoami                     |        显示当前正进行操作的用户名        |

### 变基 rebase：

#### 应用场景1：整合非重要版本记录

|          指令          |                   作用                    |
| :--------------------: | :---------------------------------------: |
|  git rebase -i 版本号  |  将当前版本与指定版本之间的所有版本合并   |
| git rebase -i HEAD~num | 从当前版本（包含自身）向前合并 num 个版本 |

```bash
//执行完以上任意一个操作后,修改合并方式, :wq 保存
pick 0aa4591 v2  --->  pick 0aa4591 v2
pick 9few83b v3  --->  s 9few83b v3
pick 3jnk30f v4  --->  s 3jnk30f v4
```

---

```bash
//合并之后,调整新记录的信息(替换为步骤三代码), :wq 保存
# This is the 1st commit message:
v2
# This is the commit message #2:
v3
# This is the commit message #3:
v4
```

---

```bash
# This is the 1st commit message:
v2 & v3 & v4
```

:star2:通常 rebase 合并操作在提交代码至远程仓库之前，若先提交至远程仓库再合并记录会导致版本记录混乱

#### 应用场景2：避免拉取远程代码时 Git 中产生分叉

|          指令          |               作用               |
| :--------------------: | :------------------------------: |
| git fetch 别名 分支名  | 将远程仓库中的分支拉取到本地仓库 |
| git rebase 别名/分支名 |      合并两条分支（无分叉）      |

```bash
git pull origin dev (替换为步骤二代码)
```

---

```bash
git fetch origin dev
git rebase origin/dev (提前切换到dev分支)
```

#### 注意事项：

1、如果在 rebase 合并时产生冲突，自行解决冲突之后，将新代码添加至暂存区或者提交为新版本并执行以下命令即可继续正常运行：
' git rebase --continue '
2、下载 Beyond Compare 软件（正版需要收费）可用于自动解决冲突问题：

```bash
git 配置：
git config --global merge.tool bc4
git config --global mergetool.bc4.cmd '"D:\应用合集\BCompare\Beyond Compare 5\BComp.exe" "$LOCAL" "$REMOTE"'
git config --global mergetool.keepBackup false
应用 Beyond Compare 解决冲突：
git merge dev
git mergetool
```

### 协同开发：

gitflow 工作流：
![image-20240725104411865](./initgit.assets/image-20240725104411865.png)

#### 项目实践：

1.创建（master）项目以及组织
邀请同伴（个人项目）：github -> Settings -> Collaboration
![image-20240725104916365](./initgit.assets/image-20240725104916365.png)
邀请同伴（公司项目)：New organization
组织中可以有多个项目，而组织中的成员可以对组织中的某些项目进行读、写操作
![image-20240725105221066](./initgit.assets/image-20240725105221066.png)

补充：为版本打标签以便后续管理

|               指令                |        作用         |
| :-------------------------------: | :-----------------: |
| git tag -a 版本标记 -m '补充信息' | 为不同的版本打标签  |
|      git push origin --tags       | 将标签推送至 github |

2.创建分支（bug、release、dev）并上传到 github
3.设置组织成员权限并将相应的成员拉入相应项目（Settings -> Collaboration）
4.成员创建各自分支并进行开发
5.成员开发完毕后进行代码 review
方法：Settings -> Branches -> Add rule -> Require pull request reviews before merging
效果：通过设立规则，要求每次将代码合并到 dev 分支前，需要指定人员进行 review
review步骤：
:one:成员需要在 github 中选择 New pull request 提醒项目负责人进行代码 review
![image-20240725113043294](./initgit.assets/image-20240725113043294.png)
:two:选择需要合并的两个分支，点击创建：
![image-20240725113128776](./initgit.assets/image-20240725113128776.png)
:three:负责人进行 review（右上角）后同意合并（左下角）：
![image-20240725114010385](./initgit.assets/image-20240725114010385.png)
![image-20240725114114563](./initgit.assets/image-20240725114114563.png)
:four:负责人同意之后，分支会进行自动合并，无需成员再合并，此时还可以在 github 中将分支快速删除
![image-20240725114530074](./initgit.assets/image-20240725114530074.png)
6.代码 review 完毕之后，进行线上测试并提交上线

### 开源精神：

在闲暇时间为其他开源项目提供修改意见或者代码，何尝不是未来的一件谈资呢？？
1.Fork 源代码
![image-20240725154108916](./initgit.assets/image-20240725154108916.png)
2.本地进行开发或修改
3.将修改版本提交给原作者（New pull request）
![image-20240725154745548](./initgit.assets/image-20240725154745548.png)

### 配置文件：

```bash
项目配置文件：项目/.git/config
git config --local user.name ''
git config --local user.email '' 
项目配置文件：~/.git/config
git config --global user.name ''
git config --global user.email '' 
系统配置文件：/etc/.git/config
git config --system user.name ''
git config --system user.email '' 
注意：修改系统配置文件需要有 root 权限
```

:star2:配置文件的应用优先级为：项目配置文件 > 项目配置文件 > 系统配置文件（即就近原则）

### Git 忽略文件：

有时我们希望 Git 管理的文件夹中有部分文件脱离管理，此时可以使用 .gitignore 文件来管理：
1.在 Git 管理的文件夹下创建 .gitignore 文件
2.将需要忽略的文件（包括自身）写入 .gitignore 文件

```bash
*.h (其中 * 为任意字符)
！a.h (结合上命令表示将除 a.h 外所有以 .h 结尾的文件忽略)
*.py[c|cpp|text] (表示忽略以.py/c/cpp/text 结尾的文件)
文件夹/ (表示忽略文件夹下的所有文件,也可以配合！使用)
.gitignore
```

![image-20240725162901864](./initgit.assets/image-20240725162901864.png)
:star2:常见的建议可忽略文件在 github 也有总结，可自行下载

### 任务管理：

github -> Issues 面板可以进行问题提问与讨论：
![image-20240725163703155](./initgit.assets/image-20240725163703155.png)

github -> Wiki 面板进行项目详情介绍或者注意事项等等，以便后续新人快速上手项目
![image-20240725164040009](./initgit.assets/image-20240725164040009.png)

持续更新中...:kissing_smiling_eyes:



[^1]: 在git commit -m ''时出现命令执行失败的原因是没有在本地设置用户名和邮箱，在命令行设置一下即可：

```bash
git config –-global user.email 'you@example.com'
git config –-global user.name 'Your name'
```

[^2]: 已管文件与未管文件之间由 Git 进行自动检测与转换

[^3]: 主分支名称为 master，其余分支名称自拟。正式的开发至少有两个分支（master 与 dev），master分支只存储正式版本，而 dev 分支用于开发新功能

[^4]:在合并不同的分支时，有可能会因为文件冲突而需要手动修复

```bash
例如：
<<<<<< HEAD
====== 
>>>>>> dev
```

[^5]:一个项目仓库只需要在其初始化的时候起一次别名即可，后续可直接使用该别名

[^6]:此时将远程仓库中的所有分支均拷贝下来，只不过在 Git 中没有直接显示，不过依旧可以使用 git branch 指令查看并操作<br>注意：上传代码时每次上传一个分支，拷贝代码时只需要拷贝一次




