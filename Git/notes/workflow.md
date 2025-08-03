<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">GitHub 工作流</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

-----
本流程将以 **`dev` 分支为核心开发分支**，并引入**功能分支 (Feature Branch)** 的概念，现代软件开发的最佳实践，能最大程度地避免冲突，让协作变得简单。

-----

### **A. 核心与约定**
1.  👑 **`master` 分支**: **神圣的而不可侵犯**的分支。仅存放已经测试过、可以随时发布的版本。**任何人未经作者允许都不可向 `master` 提交代码**。
2.  🛠️ **`dev` 分支**: **主要的开发分支**，所有新功能的“整合区”，所有新功能最终都会合并到这里。
3.  ✨ **功能分支 (如 `feature/login`, `feature/user-profile`)**: **具体干活**的地方，每当要开发一个新功能或修复一个Bug，都应该从 `dev` 分支创建出一个新的功能分支。**开发工作都在功能分支上进行**。功能分支的生命周期很短，开发完成后就合并回 `dev`，然后删除。

-----

### **B. 准备工作**
**1. 仓库所有者 (Livia-Tassel) 创建 `dev` 分支**
若远程仓库还没有 `dev` 分支，先创建并推送它。
创建 `dev` 分支
```bash
cd Herbal-Wonderland
git checkout -b dev
```
将 `dev` 分支推送到 GitHub，并上游跟踪
```bash
git push -u origin dev
```

**2. 协作者 (CoolSky) 获取 `dev` 分支**
克隆仓库，现在保证本地有 `dev` 分支并与之同步。
从远程仓库拉取所有分支
```bash
cd Herbal-Wonderland
git fetch origin
```
在远程的 `dev` 分支创立一个本地的 `dev` 分支并切换过去
```bash
git checkout -b dev origin/dev
```
(本地已有dev) 则切换到dev分支并和远程同步
```bash
git checkout dev
git pull origin dev
```

-----

### **C. 日常开发**
**步骤 1: 开始新任务前，先同步 `dev` 分支**
在开始写任何代码之前，**务必**检查你的本地 `dev` 分支是最新版本。
切换到 `dev` 分支，从 GitHub 拉取最新的 `dev` 分支代码
```bash
git checkout dev
git pull origin dev
```

**步骤 2: 创建的功能分支**
从最新的 `dev` 分支上创建一个属于你的、描述清晰的功能分支。
```bash
git checkout -b branch-name
```
(`branch-name` 建议采取 `feature/功能描述` 或 `fix/bug描述` 的格式)

**步骤 3: 在功能分支上编码和提交**
现在，你可以安心地在这个 `feature/***` 分支上进行所有的开发工作。
```bash
# ... working ...

git add .
git commit -m "feat: 完成UI"
```

(可以多次提交，建议提交只包含一个小的、完整的功能点)

**步骤 4: 将功能分支推送到 GitHub**
当你觉得这个功能开发告一段落，或者想让对方看到你的进度时，就把你的功能分支推送到远程仓库。
首次推送这个分支时，采取 `-u` 参数
```bash
git push -u origin feature/user-login
```
后续推送可简化命令
```bash
git push
```

**步骤 5: 在 GitHub 上创建 Pull Request (PR)**
推送成功后，去 GitHub 的仓库主页，有一个黄提示条，让你为你推送的分支创建一个 Pull Request。
1.  点击 **“Compare & pull request”** 按钮。
2.  **Base 分支** 选择 `dev` (将代码合并到 `dev`)。
3.  **Compare 分支** 选择 `feature/user-login` (正在开发的分支)。
4.  写一个清晰的标题和描述。
5.  点击 **“Create pull request”**。

**步骤 6: 审查与合并 Pull Request**
PR 创建后，另一个人（协作者）会收到通知。他去审查你的代码。
1.  打开这个 PR，查看代码改动。
2.  可以提出评论或修改建议。
3.  如果代码没有问题，点击绿色的 **“Merge pull request”** 按钮，再点击确认。

这样，你的 `feature/user-login` 分支的代码就安全地合并到 `dev` 分支里了。

**步骤 7: 清理已合并的分支**

合并成功后，这个功能分支就完成了它的历史使命。
1.  在 GitHub 上，PR 合并后会有一个 **“Delete branch”** 的按钮，点击它删除远程功能分支。
2.  你们俩也应该删除本地的这个功能分支。
    切换回 `dev` 分支
    ```bash
    git checkout dev
    ```
    删除本地的 `feature/user-login` 分支
    ```bash
    git branch -d feature/user-login
    ```

**然后，循环开始，回到步骤 1，拉取新的 `dev` 分支！**

-----

### **D. 版本发布**
当 `dev` 分支上的功能积累到一定程度，测试通过，发布一个新版本时，由你来执行以下操作：
1.  **切换到 `master` 分支并拉取**
    ```bash
    git checkout master
    git pull origin master
    ```

2.  **将 `dev` 分支合并到 `master`**
    ```bash
    git merge dev
    ```

3.  **推送 `master` 分支**
    ```bash
    git push origin master
    ```

4.  **(推荐) 创建标签，标记版本号**
    ```bash
    git tag -a v1.0.0 -m "发布 1.0.0 版本，功能"
    git push origin v1.0.0
    ```

-----

### **总结**
1.  **开始任务**: `git checkout dev` -\> `git pull origin dev` -\> `git checkout -b feature/xxx`。
2.  **开发**: `git add .` -\> `git commit -m "..."`。
3.  **分享**: `git push -u origin feature/xxx`，然后去 GitHub 创建 PR (合并到 `dev`)。
4.  **结束**: 等 PR 被合并后，`git checkout dev` -\> `git branch -d feature/xxx`。