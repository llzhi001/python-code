#CalUR.py
import jieba
txt = open("/Users/fangjiaqi/Downloads/wechat_context.txt", "r", encoding="utf-16").read()
excludes = {"微信","什么","为什么","非常","时候","一次","自己","以前","还是","怎么","一个","这个"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) ==1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(30):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
