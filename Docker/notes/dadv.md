<h1 style="font-family: '仿宋', 'FangSong', 'Times New Roman', serif; color: orange; font-size: 2em; font-weight: bold; text-align: center; border-bottom: none; margin-bottom: 0;">Docker 进阶</h1>
<p style="font-family: 'Times New Roman', serif; font-size: 1em; text-align: right; margin-top: 0;">Livia Tassel</p>
<div style="font-family: 'Times New Roman', 'FangSong', '仿宋', serif;">

[TOC]

# Docker 安装
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
``` 

自动化部署完 Docker 后，检查版本：
```bash
sudo docker version
```

# Docker 命令速查表
| 命令 | 描述 |
| :---: | :---: |
| docker ps | 查看本地正在运行的容器 |
| docker ps -a | 查看包括已停止的所有容器 |
| docker run image_name | 启动新的容器 |
| docker run -d image_name | 在后台运行容器（分离模式） |
| docker run --name container_name image_name | 为容器命名运行 |
| docker run -p 8080:80 image_name | 映射端口（宿主机:容器） |
| docker logs container_name/id | 查看容器日志 |
| docker top container_name/id | 查看容器内部进程 |
| docker exec -it container_name/id /bin/bash | 进入正在运行的容器交互模式 |
| docker stop container_name/id | 停止正在运行的容器 |
| docker start container_name/id | 启动已停止的容器 |
| docker restart container_name/id | 重启容器 |
| docker rm container_name/id | 删除容器 |
| docker rm -f container_name/id | 强制删除容器 |
| docker container prune | 删除所有已停止的容器 |
| docker images | 查看镜像列表 |
| docker rmi image_name/id | 删除镜像 |
| docker pull image_name | 拉取镜像 |
| docker build -t image_name:tag . | 构建镜像 |
| docker info | 查看 Docker 系统信息 |
| docker version | 查看 Docker 版本 |

