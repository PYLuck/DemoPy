#!/bin/sh

# 测试脚本，写入日志文件
name="pengyu"
echo $name

echo "BACKUP DATE:" $(date +"%Y-%m-%d %H:%M:%S")

DATE=`date '+%Y%m%d-%H%M%S'`
echo $DATE

# 执行脚本，会在当前 指定目录下生成.log文件
LogNameDATE=`date '+%Y%m%d'`

# 判断文件夹是否存在，不存在则创建
if [ ! -d "./log_data/" ];then
  mkdir ./log_data
  else
  echo "文件夹已经存在"
fi

echo "———————————————–" >> ./log_data/log$LogNameDATE.log
echo "BACKUP DATE:" $(date +"%Y-%m-%d %H:%M:%S") >> ./log_data/log$LogNameDATE.log
echo "———————————————– " >> ./log_data/log$LogNameDATE.log

# 获取文件名，获取文件路径
# 参考：https://blog.csdn.net/ksj367043706/article/details/94993422
# https://blog.csdn.net/weixin_30573089/article/details/112960362
# 多行注释用 :<<! 语句块 !
:<<!
对${}的总结：
#代表左起，%代表右起
两个符号代表最后一个字符，一个符号代表第一个字符
    #：左起第一个
    ##： 左起最后一个
    %：右起第一个
    %%：右起最后一个
!
