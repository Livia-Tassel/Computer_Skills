<center style="font-family: 'Times New Roman', sans-serif; color: orange; font-size: 2em; font-weight: bold">Hog</center>
<div style="text-align: right; font-family: 'Times New Roman', serif; font-size: 1em;">Livia Tassel</div>

[TOC]

# 题目复述
## 基础规则
1. 双方玩家轮流掷 🎲，优先超过`GOAL`分者为胜 🎉
2. 骰子若干（0-10）/轮人次，得分为所有 🎲 分之和
3. 逢`1`判负，积`1`分 `Sow Sad`
## 野猪乱斗
玩家未掷 🎲 时，其得分等于 max(1, 3 * abs((rival.score/10) % 10, self.score % 10)) `Boar Brawl`
## Sus Fuss
恰好有3个或4个因子（包括1与其本身）的分，称为`sus`，玩家分加上本轮 🎲 分后如为`sus`，则升级为下一质分

# 工程文件
`hog.py` 功能
`dice.py` 制作与掷骰子
`hog_gui.py` 图形UI
`hog_ui.py` 文本UI
`gui_files` Web GUI 目录
