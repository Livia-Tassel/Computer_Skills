<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">SSH 密钥</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

# GitHub 托管
```bash
git remote -v
git remote remove origin
git remote add origin git@github.com:Livia-Tassel/Livia-Tassel.github.io.git
git remote set-url origin git@github.com:Livia-Tassel/Livia-Tassel.github.io.git
git push -u origin master
```


# SSH密钥
**生成SSH密钥**
```bash
ssh-keygen -t rsa -C "@mail"
```
**将密钥拷贝至GitHub中**
`user\username\.ssh\id_rsa.pub`

![alt text](/ssh.assets/image.png)
