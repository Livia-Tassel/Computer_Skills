<center style="font-family: 'Times New Roman', sans-serif; color: orange; font-size: 2em; font-weight: bold">Tmux</center>
<div style="text-align: right; font-family: 'Times New Roman', serif; font-size: 1em;">Livia Tassel</div>

[TOC]

## 修改配置文件
```bash
touch ~/.tmux.conf
vim ~/.tmux.conf

set -g mouse on # mouse
set -g prefix C-a # Ctrl a

https://github.com/theniceboy/.config/blob/master/.tmux.conf
```

## 快捷键
```bash
tmux # create tmux seesion
tmux new -t sessname # session name

prefix c # create window
prefix & # close window
prefix {num} # select window
prefix , # rename window

prefix % # vertical panes
prefix “ # horizontal panes

prefix "↑/↓/←/→" # navigate panes
prefix q # select panes
prefix ' ' # toggle pane layouts

prefix z # zoom out current pane
prefix x # close pane
prefix w # display all the windows/panes

prefix d # detach session

tmux ls # display all the seesions
tmux a -t 会话序列/名称 # connect to session
tmux kill-session -t 会话序列/名称 # delete session
```

