##!/bin/sh

# 查看docker信息
docker info

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
  docker run -itd --name=pyl_test01  [tag] /bin/bash
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
  docker export 容器id > aaa_test.tar
  # 导入
  cat aaa_test.tar | docker import - 镜像用户/镜像名:镜像版本号
  导入该镜像后,(1) docker run启动;(2) docker exec进入

!

# 高级篇
:<<!
1、Dockerfile解析         创建镜像：
由4部分信息组成：基础镜像信息、维护者信息、镜像操作指令和容器启动时执行指令
ADD，将文件<src>拷贝到container的文件系统对应的路径<dest>

2、容器编排 docker-compose.yml 配置自己的镜像
!



# docker镜像源
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

