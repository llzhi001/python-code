# coding=utf-8
from bs4 import BeautifulSoup

info = []
with open('/Users/fangjiaqi/20180226-MyCode/Python/spider/oneweek/1-2/homework/homework_required/index.html','r',encoding='utf-8') as  wb_data:
    soup = BeautifulSoup(wb_data,'lxml')
    #print(soup)
    images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    rates = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')

    #print(images,titles,prices,rates,stars,sep='\n-----------------------\n')
for title,image,price,rate,star in zip(titles,images,prices,rates,stars):
    data = {
        'title': title.get_text(),
        'rate': rate.get_text(),
        'price': price.get_text(),
        'star': len(star.find_all("span",class_='glyphicon glyphicon-star')),
        'image': image.get('src'),
    }
    print(data)
    #info.append(data)

