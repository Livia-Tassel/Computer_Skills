<center style="font-family: 'Times New Roman', sans-serif; color: orange; font-size: 2em; font-weight: bold">ssh</center>
<div style="text-align: right; font-family: 'Times New Roman', serif; font-size: 1em;">Livia Tassel</div>

[TOC]

# Win端（PowerShell）

## 1. 配置 SSH Server
```powershell
# 安装 OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# 启动 sshd 服务
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# 开放防火墙端口 22
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

# ssh 服务状态
Get-Service sshd
ssh -V
Get-Service -Name *ssh*
netstat -an | findstr :22
ipconfig
```

## 2. 固定 IP
```powershell
# 网卡名称
Get-NetAdapter

# 假设网卡名为 "WLAN"，配置静态 IP：
New-NetIPAddress -InterfaceAlias "WLAN" -IPAddress 192.168.100.200 -PrefixLength 24 -DefaultGateway 192.168.100.1
Set-DnsClientServerAddress -InterfaceAlias "WLAN" -ServerAddresses ("1.1.1.1", "8.8.8.8")
```


# Mac端

## 1. macOS 端
```bash
ssh username@192.168.100.200
```
> 示例：`ssh 3459465562@qq.com@192.168.100.200`

## 2. 远程默认 shell 为 Git Bash
Windows PowerShell（admin）中执行：
```powershell
Set-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Program Files\Git\bin\bash.exe"
Restart-Service sshd
```

## 3. 远程终端乱码 / 兼容问题
在 `~/.bashrc` 添加以下内容：
```bash
# 解决 tmux-256color 兼容问题
[ "$TERM" = "tmux-256color" ] && export TERM=xterm
```

## 4. Git Bash（PS1）
```bash
PS1='@\[\e[32m\]\h\[\e[0m\] \[\e[33;1m\]\w\[\e[0m\] \[\e[35m\]\$\[\e[0m\] '
```
> 显示：绿色主机名 + 亮黄色路径 + 紫色 `$` 符号，简洁美观。

修改后执行：
```bash
source ~/.bashrc
```
