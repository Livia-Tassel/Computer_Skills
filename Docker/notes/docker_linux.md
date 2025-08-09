[TOC]

## **1. 安装 Docker**

### **步骤 1：更新系统包**

```bash
sudo apt update
sudo apt upgrade -y
```

### **步骤 2：安装 Docker**

```bash
sudo apt install docker.io -y
```

### **步骤 3：启动并启用 Docker**

安装完 Docker 后，启动并设置它随系统启动：

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### **步骤 4：检查 Docker 状态**

检查 Docker 是否安装并正常运行：

```bash
sudo systemctl status docker
```

看到类似如下的输出，表示 Docker 正在运行：

```
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running)
```

### **步骤 5：为非 root 用户授权使用 Docker**

为了不每次都使用 `sudo`，可以将用户添加到 Docker 组：

```bash
sudo usermod -aG docker $USER
```

然后退出并重新登录，或者通过以下命令使更改生效：

```bash
newgrp docker
```

------

## **2. 替换国内Docker镜像源**

### **步骤 1：替换国内镜像**

1. 配置镜像源：

   ```bash
   sudo mkdir -p /etc/systemd/system/docker.service.d
   sudo tee /etc/systemd/system/docker.service.d/override.conf <<EOF
   [Service]
   ExecStart=
   ExecStart=/usr/bin/dockerd --registry-mirror=https://<mirror-url>
   EOF
   ```

   >[🔥截止目前，国内仍然可用docker镜像加速器汇总（2025-2）](https://www.kelen.cc/dry/docker-hub-mirror#:~:text=本文汇总了截止2025年2月国内仍可用的 Docker 镜像加速器。 包含多个docker镜像加速器地址，保证可用性，还介绍了测试镜像可用性的方法，以及在Linux、Windows 和 Mac 系统中的临时和永久配置方法。)

2. 重新加载配置并重启 Docker 服务：

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart docker
   ```

3. 尝试重新拉取镜像：

   ```bash
   sudo docker pull tensorflow/tensorflow:latest
   ```

### **步骤 2：检查防火墙设置**

有时，防火墙可能会限制 Docker 访问外部网络。

#### **查看防火墙状态**：

```bash
sudo ufw status
```

若防火墙启用，尝试暂时禁用它，然后再尝试拉取镜像。：

```bash
sudo ufw disable
```

### **步骤 3：检查 Docker 设置和代理**

若有代理服务器访问互联网，确保 Docker 配置正确的代理设置。

1. 在 **`/etc/systemd/system/docker.service.d/override.conf`** 中，设置代理：

   ```bash
   [Service]
   Environment="HTTP_PROXY=http://proxy:port/"
   Environment="HTTPS_PROXY=http://proxy:port/"
   ```

2. 重新加载并重启 Docker：

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart docker
   ```

然后再尝试拉取镜像。

------

## **3. 安装 TensorFlow Docker 镜像**

### **步骤 1：拉取 TensorFlow Docker 镜像**

```bash
sudo docker pull tensorflow/tensorflow:latest
```

也可以下载其他版本的 TensorFlow，比如：

```bash
sudo docker pull tensorflow/tensorflow:2.4.0
```

### **步骤 2：运行 TensorFlow 容器**

拉取镜像后，启动新的容器并进入该容器：

```bash
sudo docker run -it tensorflow/tensorflow:latest bash
```

启动 TensorFlow 的 Docker 容器，并进入容器内的终端环境。

### **步骤 3：测试 TensorFlow**

在容器内，启动 Python 并测试 TensorFlow：

```bash
python3
>>> import tensorflow as tf
>>> print(tf.__version__)
```

若没有问题，容器中的 TensorFlow 应该会正常显示版本号。

------

## **4. 创建 Dockerfile（可选）**

如要个性化的 Docker 环境，例如安装其他依赖或设置工作目录，可以创建 **Dockerfile** 来自动化环境配置。

```Dockerfile
# 使用 TensorFlow 官方镜像
FROM tensorflow/tensorflow:latest

# 设置工作目录
WORKDIR /workspace

# 安装其他依赖库（如果需要）
RUN pip install numpy pandas matplotlib

# 设置默认命令
CMD ["python3"]
```

然后使用以下命令构建并运行容器：

```bash
docker build -t my_tensorflow .
docker run -it my_tensorflow bash
```

------

## **5. Docker 容器与数据共享**

若在主机和 Docker 容器之间共享数据（比如代码或模型文件），可以使用 **Docker 挂载卷**：

```bash
sudo docker run -it -v /path/to/host/directory:/path/to/container/directory tensorflow/tensorflow:latest bash
```

将主机上的 `/path/to/host/directory` 挂载到容器中的 `/path/to/container/directory`，使得方便地访问和修改文件。