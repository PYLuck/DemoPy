# created by @Moss 
# used in Ubuntu18.4

"""
Usage:

体验: 双击RunMe文件~
=================== 需求：通过*.sh脚本运行 *.py 代码或程序 =====================================
# 常规用法-在终端中输入:
(base) yskj@yskj-moss:~$ bash ./test_scrip.sh

# 双击*.desktop桌面配置文件实现 快速运行python脚本或程序

> Step1:
cd 桌面 
sudo touch RunMe.desktop | chmod a+x RunMe.desktop	# 编辑如下：
--------------------------------------------------------------------------------
[Desktop Entry]
Name=RunMe
Name[zh_CN]=RunMe
Exec= bash ~/persons/ai_group/Moss/Script/UbuntuRun_soft/test_scrip.sh
Path= ~/persons/ai_group/Moss/Script/UbuntuRun_soft
Terminal=true
Type=Application
---------------------------------------------------------------------------
# if you want open Terminal and not close, Use:
Exec = gnome-terminal -e "bash -c '/home/yskj/anaconda3/envs/labelImg-master/run_lableImg.sh;$SHELL'" 


> Step2: 
touch test_scrip.sh	# 编辑如下：
-------------------------------------------------------------------------------
#! /bin/bash

source ~/anaconda3/bin/activate base	# Env of python3: need conda activate base
python3 ./Usage.py

sleep 1m
exit 0
--------------------------------------------------------------------------
# source 配置python3使用的base环境很重要,一定要有!!!!!!!!!

> Step3: 在 Usage.py 编写代码 


"""


# Example:
print('Bingo !!!')

for i in range(16):
	print('Test:',i)

