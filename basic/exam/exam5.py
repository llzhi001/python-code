'''
词频统计之《哈姆雷特》
 

描述
Hamlet 《哈姆雷特》是莎士比亚的一部经典悲剧作品。这里提供了该故事的文本文件：hamlet.txt。

请统计该文件中出现英文的词频，按照如下格式打印输出前10个高频词语：

the       , 1138

即：英文单词（左对齐，宽度为10）+ 逗号 + 词语出现的频率（右对齐，宽度为5）

 

要求与说明：

1. 标点符号及组合不算作英文词语

2. 同一单词的各种大小写形式记作一个词，如The和the相同 

3. 在程序中，请使用文件名打开文件：hamlet.txt

# 仅作为示例
f = open("hamlet.txt", "r")
f.close()
'''

#CalHamletV1.py
def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘’{|}~·':
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
n = input()
if n == '':
    for i in range(1):
        word, count = items[i]
        print("{0:<10},{1:>5}".format(word, count))
else:
    for i in range(10):
        word, count = items[i]
        print("{0:<10},{1:>5}".format(word, count))
