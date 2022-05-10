# 词云--出现频率越多的词，字体越大;    词云库、jieba库;
"""
pip install wordcloud   wordcloud安装成功之后，numpy、pillow库会被自动安装
生成词云时, wordcloud 默认会以空格或标点为分隔符对目标文本进行分词处理。
对于中文文本，分词处理需要由用户来完成: 一般步骤是先将文本分词处理，然后以空格拼接，再调用wordcloud库函数。
处理中文时还需要指定中文字体: 例如，选择了微软雅黑字体（电脑C:\Windows\Fonts\msyh.ttf）作为显示效果，需要将该字体文件与代码存放在同一目录下或在字体文件名前增加完整路径。

"""


import jieba
from wordcloud import WordCloud

# 读入txt文本数据
text = open(r"D:\Software\Desktop\192030021.txt", "r").read()
cut_text = jieba.cut(text)  # 结巴中文分词，生成字符串，默认精确模式，如果不通过分词，无法直接生成正确的中文词云
result = " ".join(cut_text)  # 必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云

'''
# 预处理示例
txt = '弱小的人,才习惯,嘲讽和否定，而内心,强大的人,从不吝啬，赞美和鼓励！我们就是后浪，奔涌吧！后浪，奔涌吧！'
words = jieba.lcut(txt)     #精确分词
result = ''.join(words)    #空格拼接
wcloud.generate(result)
'''




# 排除词云中 不需要的连接词
exclude = {'的', '为', '与', '和', '因此', '在', '一种', '本章', '那么','等','可以','进行','且',
           '针对', '基于', '对', '通过', '这是', '一个', '是', '不同', '采用','提出','使用',
           '没有', '所示', '如图', '这种', '主要', '以', '中', '了', '这个', '下', '根据','然后',
           '本文', '其中', '为了', '并', '下', '利用','需要', '或', '这', '具有', '方式', '个',"我们","将"}

wcloud = WordCloud(
    font_path="C:\Windows\Fonts\msyh.ttc",  # 设置字体，不指定就会出现乱码
    scale=16,   # 设置词云图的大小
    background_color='white',  # 设置背景色，默认为黑色
    width=1000,  # 设置背景宽
    height=400,  # 设置背景高
    max_font_size=70,  # 最大字体
    min_font_size=10,  # 最小字体
    mode='RGBA',  # 当参数为“RGBA”并且background_color不为空时，背景为透明
    stopwords=exclude
)
wcloud.generate(result)
wcloud.to_file(r'中文词云图.png')


