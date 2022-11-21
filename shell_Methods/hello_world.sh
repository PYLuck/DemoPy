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