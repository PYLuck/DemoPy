#!/usr/bin/env sh

echo "遍历data内的文件夹，分别压缩data内所有的 文件夹："
#cd data || exit

pwd
for file in ./data/*
do
if [ -d "$file" ]
then
  echo "$file is 文件夹"
  echo 开始压缩 ${file##*/} :
#  tar -zcvf  ${file##*/}.tar.gz  ${file}
  echo ${file##*/}.tar.gz 压缩完成
elif [ -f "$file" ]
then
  echo "$file is 文件 ignored"
fi
done

