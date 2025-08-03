<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">给小楚南的入门指南</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]


### **【新手伙伴专属】Git & GitHub 协作快速入门指南**
你好！欢迎加入 `Herbal-Wonderland` 项目！
**目标：** 完成一次标准的开发流程，最终通过 **Pull Request (PR)** 的方式，把你写的一行代码合并到项目的开发分支中。
**开始前请保证：**
  * 你的电脑已经安装了 Git。
  * 你的电脑上配置好了 SSH 密钥并添加到了你的 GitHub 账户。

-----

### **Part One：把项目代码拿到你的电脑**
把云端（GitHub）的项目代码复制一份到你的电脑上。
#### **步骤 1.1：创建你的“工作区”文件夹**
1.  打开你的 **Git Bash** 终端。
2.  创建一个名为 `Herbal-Wonderland` 的文件夹并进入其中。
    ```bash
    cd /e/
    mkdir Herbal-Wonderland夹
    cd Herbal-Wonderland
    ```
    现在，你的终端路径应该像这样： `.../Herbal-Wonderland`。
#### **步骤 1.2：克隆项目到本地 (关键步骤)**
**注意：** 你**不需要**执行 `git init`！`git init` 用于从零创建一个全新的仓库。而我们的仓库已经在 GitHub 上了，所以我们用 `git clone`（克隆）来获取它。

在 Git Bash 终端里，执行以下命令：
```bash
git clone git@github.com:Livia-Tassel/Herbal-Wonderland.git .
```
（注意命令中的 "."，它表示“克隆到当前这个空文件夹里”）

当你看到终端显示 `done.` 或类似信息时，就表示项目已经成功克隆到你的电脑上了！`Herbal-Wonderland` 文件夹现在就是你的项目根目录。

-----

### **Part Two：核心工作流**
现在你有了项目的完整拷贝。接下来，我们将模拟一次真实的功能开发。我们的任务是：**修改项目里的说明文件 `README.md`，加上你的名字**。
#### **步骤 2.1：在 `dev` 开发分支**
我们的主要开发工作都在 `dev` 分支上进行。
1.  首先，检查一下你本地有哪些分支。
    ```bash
    git branch
    ```
    （可能只有一个 `* master` 分支）
2.  切换到 `dev` 分支，从远程仓库获取 `dev` 分支并在本地创建关联。
    ```bash
    git checkout dev
    ```
    若上一步失败并提示找不到 `dev`，请让仓库所有者（Livia-Tassel）先执行 `git push -u origin dev`，然后再让你执行 `git fetch origin` 和 `git checkout dev`。

#### **步骤 2.2：创建你自己的“功能分支”**
为了不影响主开发分支 `dev`，创建一个属于你自己的“草稿纸”，我们称之为**功能分支 (Feature Branch)**。
创建并立即切换到一个名为 `feature/add-my-name` 的新分支。
```bash
git checkout -b feature/add-my-name
```
  * **为什么要这样做？** 因为你在自己的分支上可以随意修改、提交，即使搞砸了，也只是弄乱了自己的“草稿纸”，不会影响到 `dev` 分支和其他人。

#### **步骤 2.3：修改代码**
1.  在你的文件浏览器中，找到 `Herbal-Wonderland` 文件夹。
2.  找到名为 `README.md` 的文件，用记事本或者任何文本编辑器打开它。
3.  在文件的最后，加上一行字，比如：
    > `由 Livia-Tassel 与 CoolSky 共同协作完成。`
4.  保存并关闭文件。

#### **步骤 2.4：拍照存档**
1.  **“选东西” (`git add`)**：告诉 Git，将改动记录下来。
    ```bash
    # 这个 "." 表示“所有被修改过的文件”，简单方便
    git add .
    ```
2.  **“按快门” (`git commit`)**：正式记录这次快照，并附上一句描述。
    ```bash
    git commit -m "docs: 在README中添加协作者"
    ```
      * `-m` 后面的文字是**提交信息**，必须写！

-----

### **第三部分：分享与协作 - 提交你的 Pull Request (PR)**
#### **步骤 3.1：将你的功能分支推送到 GitHub**
将你的 `feature/add-my-name` 分支以及上面的所有 commit，都上传到 GitHub 云端仓库。
```bash
git push -u origin feature/add-my-name
```
（`-u` 参数只在第一次推送这个新分支时需要，它会把本地分支和远程分支关联起来）

#### **步骤 3.2：创建你的第一个 Pull Request (PR)**
1.  打开你的浏览器，进入 `Herbal-Wonderland` 的 GitHub 仓库主页。
2.  你会看到一个提示条，写着 "feature/add-my-name had recent pushes"。
3.  点击右边的绿色按钮 **“Compare & pull request”**。
4.  现在你会进入一个新页面，请检查：
      * **`base:` 分支** 应该是 **`dev`**。
      * **`compare:` 分支** 应该是 **`feature/add-my-name`**。
5.  给你的 PR 写一个清晰的标题，比如“添加协作者到 README”。
6.  点击绿色的 **“Create pull request”** 按钮。

**恭喜你！你已经成功提交了你的第一个 PR！**

接下来，仓库所有者（Livia-Tassel）会收到通知。他会去审查你的代码，如果没有问题，就会点击“Merge pull request”按钮，将你的代码正式合并到 `dev` 分支中。至此，一次完美的协作流程就完成了！

这个流程以后会成为你的日常，多做几次就会非常熟练。祝你编码愉快！