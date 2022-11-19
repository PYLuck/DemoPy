# 删除文本中出现的 空格;[适用于复制pdf文本->粘贴到txt过程中出现的 空格乱码 问题]

# 读取txt文本
# ecoding=utf-8


outfile = open(r"../output.txt", 'a+', encoding="utf8")
with open(r"../1.txt", 'r', encoding="utf8") as f:
    for eachline in f.readlines():
        # 去掉文本行里面的空格、\t、数字（其他有要去除的也可以放到' \t1234567890'里面）
        lines = filter(lambda ch: ch not in ' ', eachline)      # __class = filter
        Lines = list(lines)
        outfile.write(''.join(Lines))  # 写入

    outfile.write('\n'+'——'*18 + '\n')  # 写入

outfile.close()
