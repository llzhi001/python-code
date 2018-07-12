# coding=utf-8
from bs4 import BeautifulSoup

info = []
with open('/Users/fangjiaqi/20180226-MyCode/Python/spider/oneweek/1-2/code of video/web/new_index.html','r') as  wb_data:
    soup = BeautifulSoup(wb_data,'lxml')
    #print(soup)
    images = soup.select('body > div.main-content > ul > li  > img')
    titles = soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = soup.select('body > div.main-content > ul > li > div.rate > span')
    cates = soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')

    #print(images,titles,descs,rates,cates,sep='\n-----------------------\n')

for title,image,desc,rate,cate in zip(titles,images,descs,rates,cates):
    #print(title.get_text())
    data = {
        'title' : title.get_text(),
        'rate' : rate.get_text(),
        'desc' : desc.get_text(),
        'cate' : list(cate.stripped_strings),
        'image' : image.get('src'),
    }
    #print(data)
    info.append(data)

for i in info:
    if float(i['rate']) > 3:
        print(i['title'],i['cate'])






'''
    body > div.main - content > ul > li: nth - child(1) > img
    body > div.main - content > ul > li: nth - child(1) > div.article - info > p.description
    body > div.main - content > ul > li: nth - child(1) > div.article - info > p.meta - info > span:nth-child(2)
    body > div.main - content > ul > li: nth - child(1) > div.article - info > h3
    body > div.main - content > ul > li: nth - child(1) > div.rate > span
'''