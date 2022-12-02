##!/bin/sh

:<<!
docker info: 常用命令汇总
Ref@  https://blog.csdn.net/qq_21768483/article/details/124838851

docker镜像市场，例如： http://hub.daocloud.io/    https://hub.docker.com/
0.第三方镜像拉取，如docker pull [tag]
docker pull 1.9.1-cuda11.1-cudnn8-runtime
拉取完毕后可以使用 docker images 查看

1、Dockerfile         构建镜像：
由4部分信息组成：基础镜像信息、维护者信息、镜像操作指令和容器启动时执行指令
ADD，将文件<src>拷贝到container的文件系统对应的路径<dest>

2、docker-compose.yml 配置自己的镜像
!
# 查看docker信息
docker info

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

