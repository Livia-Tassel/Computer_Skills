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
| docker run -d image_name | 在后台运行容器 (分离模式) |
| docker attach container_name/id | 重连后台运行的容器 |
| docker run -it image_name /bin/bash | 启动容器并进入交互式 Shell |
| docker run --name container_name image_name | 为容器命名运行 |
| docker run -p 8080:80 image_name | 映射端口 (宿主机端口:容器端口) |
| docker run -v host_path:container_path image_name | 磁盘映射 (卷挂载) (宿主机路径:容器路径) |
| docker run -e VAR=value image_name | 设置环境变量 |
| docker start container_name/id | 启动已停止的容器 |
| docker stop container_name/id | 停止正在运行的容器 |
| docker restart container_name/id | 重启容器 |
| docker exec -it container_name/id /bin/bash | 进入正在运行的容器的交互模式 |
| docker logs container_name/id | 查看容器的日志输出 |
| docker logs -f container_name/id | 实时跟踪查看容器的日志 |
| docker top container_name/id | 查看容器内部运行的进程 |
| docker inspect container_name/id | 查看容器的底层详细信息 (JSON 格式) |
| docker rm container_name/id | 删除已停止的容器 |
| docker rm -f container_name/id | 强制删除正在运行的容器 |
| docker container prune | 删除所有已停止的容器 |
| docker images | 查看本地所有镜像 |
| docker pull image_name:tag | 从 Docker Hub 拉取镜像 |
| docker build -t image_name:tag . | 从当前目录的 Dockerfile 构建镜像 |
| docker rmi image_name/id | 删除镜像 |
| docker inspect image_name/id | 查看镜像的底层详细信息 (JSON 格式) |
| docker image prune | 删除所有悬空 (dangling) 镜像 |
| docker image prune -a | 删除所有未被任何容器使用的镜像 |
| docker info | 查看 Docker 系统信息 (配置、驱动、资源等) |
| docker version | 查看 Docker 客户端和服务器版本 |
| docker network ls | 查看 Docker 网络列表 |
| docker volume ls | 查看 Docker 卷 (volumes) 列表 |
| docker volume prune | 删除所有未被任何容器使用的卷 |
| docker system prune | 清理所有未使用的资源 (容器、网络、卷、镜像) |
| docker system prune -a --volumes | 清理一切 |

# 端口映射
将 Docker 内部端口映射到宿主机端口，以便可以从外部访问。注意，不能多次映射到主机的同一端口。
![alt text](dadv.assets/1.png)

# 磁盘映射
将容器内部的磁盘映射到本地，此时删除容器，磁盘中的文件依旧会在本地保留。
![alt text](dadv.assets/2.png)
