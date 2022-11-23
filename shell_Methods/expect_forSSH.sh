#!/usr/bin/expect -f

:<<!
expect命令 就是用来做交互用的，基本任何交互登录的场合都能使用，如ssh、scp传输文件
但是需要安装expect包：
yum -y install expect   or  apt-get install expect
expect trans_exp.sh

send：用于向进程发送字符串
expect：从进程接收字符串
spawn：启动新的进程
interact：允许用户交互
!

set timeout 6        # 设置超时时间6s

# spawn是expect的语句，执行命令前都要加
#spawn scp -P 端口 -r 目录/文件  root@ip:路径
spawn scp -P 8122  -r ./task_part2_py  cxy@10.1.203.208:/media/cxy/tmp/Wukongdata

expect "*password:"
send "OpenCV3.0"
expect eof        # 结束子进程