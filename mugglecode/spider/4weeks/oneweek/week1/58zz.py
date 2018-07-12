#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time

def get_item_info(url):
    #url = 'http://zhuanzhuan.58.com/detail/978850025531195405z.shtml?fullCate=5%2C38484%2C23094&fullLocal=1&from=pc&metric=null&PGTID=0d305a36-0000-1c70-a2b6-ecce0dd58fd9&ClickID=2'

    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)

    title = soup.select('h1.info_titile')[0].text
    price = soup.select('span.price_now > i')[0].text
    views = soup.select('span.look_time')[0].text
    area = soup.select('div.palce_li > span > i')[0].text
    cate = soup.select('span.crb_i > a')[-1].text.strip()

    #print(title,price,views,area,cate)

    data = {
        'title' : title,
        'price' : price,
        'views' : views,
        'area' : area,
        'cate' : cate,
    }
    print(data)

def get_all_items_info():
    url = 'http://bj.58.com/pbdn/0/'
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')
    #print(soup)
    hrefs_list = soup.select('a.t')
    for href in hrefs_list:
        link = href.get('href')
        #print(link)
        if 'zhuanzhuan' in link:
            get_item_info(link)





