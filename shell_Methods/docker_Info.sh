#!/bin/sh

# 查看docker信息
docker info
docker images -a
docker ps
# 备用docker镜像源
:<<!
1.网易
http://hub-mirror.c.163.com
2.Docker中国区官方镜像
https://registry.docker-cn.com
3.ustc
https://docker.mirrors.ustc.edu.cn
4.中国科技大学
https://docker.mirrors.ustc.edu.cn
!

# 基本用法
:<<!
docker info: 常用命令汇总
Ref@  https://blog.csdn.net/qq_21768483/article/details/124838851

docker镜像市场，例如： http://hub.daocloud.io/    https://hub.docker.com/
0.第三方镜像拉取，如docker pull [tag]
docker search 镜像名
docker pull 1.9.1-cuda11.1-cudnn8-runtime
docker rmi 镜像名          # 删镜像
拉取完毕后，查看镜像：
docker images -a
  0.1 基于镜像,run 创建一台全新的容器
  docker run -itd --name=pyl_test01  [REPOSITORY:TAG] /bin/bash
  -d  启动守护式容器（后台服务器）
  -it 以交互模式运行容器
  -p 宿主机端口:容器端口    —P 随机端口映射
  --name='容器新名字'

  # 查看/删除 容器状态和ip：
  docker ps
  docker rm -f [容器ID]       # 强制删除容器
  docker inspect $(docker ps -aq)|grep -i ipaddr|tail -1
  docker logs [容器id]        # 日志

  0.2 进入容器,退出,重启[restart]
  docker exec -it [容器名] /bin/bash         # exec会打开新的终端，exit退出不会导致容器停止
  docker attach                             # attach直接进容器启动命令的终端，exit退出会导致容器停止
  exit   退出并停止容器    --> 恢复： docker start 容器名
  ctrl+P+Q 退出不停止容器  --> 停止： docker stop 容器名

  # 文件拷贝
  docker cp 容器名:容器路径 主机路径

  0.3 镜像加强_commit: 提交容器副本,使其成为新的镜像
  docker commit -m="描述信息" -a="作者" 容器id  新镜像名:[新版本号]

  0.4 导出,导入容器
  # 容器打包成镜像 导出
  docker export 容器id > aaa_test.tar         # 类似快照，所以不包含元数据及历史信息，体积更小
  # 镜像打包
  docker save -o image_name > 存储路径/镜像名.tar

  # 导入
  docker load < Path/your_image.tar
  cat aaa_test.tar | docker import - 镜像用户/镜像名:镜像版本号
  导入该镜像后,(1) docker run启动;(2) docker exec进入

!

# 高级篇
:<<!
【一】、Dockerfile         创建镜像：
用来构建Docker镜像的文本文件, 是由一条条构建镜像所需要的指令和参数构成的脚本！
    由4部分信息组成：基础镜像信息、维护者信息、镜像操作指令和容器启动时执行指令
# Usage:
docker build -t 新镜像名:TAG .

# 保留字:
FROM  基础镜像
MAINTAINER  镜像维护者Neme@
ENV   设置环境变量

RUN   容器构建时需要执行的命令
WORKDIR  指定容器创建后, 终端登录进来的 默认工作目录
ADD   将文件<src>拷贝到 镜像路径<dest>, 且会自动解压tar包和处理URL


EXPOSE  当前容器对外暴露出的端口
CMD   指定容器启动后 要做的[]; Dockerfile中只有最后1个CMD命令生效; 会被docker run之后的参数覆盖
ENTRYPOINT  类似CMD, 但不会被docker run后面的命令覆盖

# 不常用
USER  指定该镜像以什么用户去执行, 不指定默认root
VOLUME  容器数据卷, 相当于 -v

# 删除虚悬镜像 <none none>
docker image ls -f dangling=true
docker image prune


【二】docker-compose.yml 容器编排  配置自己的容器服务
Compose是Docker公司推出的工具软件,可以管理多个Docker容器，用配置文件启动关闭这些容器；
官网安装docker compose:
https://docs.docker.com/compose/install/other/

# 常用命令
docker-compose --version
docker-compose config -q  # 检查配置, 有问题才有输出

docker-compose up -d     # 启动所有的docker-compose服务并后台运行
docker-compose -f /proj/docker-compose.yml up -d

docker-compose images       # 仅查看通过yml得到的容器

# docker-compose.yml 编写示例:
# yml文件的格式层级关系是缩进两个英文状态的空格，不能用缩进符等替代空格
version: "3"    # 使用3以后的版本

services:     # 有几个容器服务
  your_service_01:    # 容器名
    image: ubuntu/pytorch:1.9.1-cuda11.1-cudnn8-runtime
    environment:
      - USER: 'root'
      - PASSWORD: '123456'
    ports:
      - "8420:88"
    volumes:
      - /data/sda1/workspace: /workspace    # 从宿主机挂载目录
    networks:
      -
    command: /bin/bash

!


# 小结及汇总
:<<!
# step1:  镜像拉取/下载
docker search 镜像名
docker pull 1.9.1-cuda11.1-cudnn8-runtime
docker images -a
# step2:
vim Dockerfile      # 构造自己的镜像
docker build -t 新镜像名:TAG .

# step3:  基于镜像docker run一个或compose多个容器
vim docker-compose.yml    # 构造自己的容器
docker run -itd -v /home/dock/workspace:/workspace --name=pyl_test01  [REPOSITORY:TAG] /bin/bash
docker ps
#step4: 进入容器
docker exec -it [容器名] /bin/bash
# step5:
[OK]
!
