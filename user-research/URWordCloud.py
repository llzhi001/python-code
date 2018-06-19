#GovRptWordCloudV2.py
import jieba
import wordcloud
#from scipy.misc import imread
#mask = imread("fivestar.png")
f = open("/Users/fangjiaqi/Downloads/wechat_context.txt", "r", encoding="utf-16")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="/Library/Fonts/Arial Unicode.ttf", width=1000, height=700, background_color="white", max_words=30)
w.generate(txt)
w.to_file("/Users/fangjiaqi/github/python-code/user-research/urwordcloud.png")
