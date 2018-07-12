# coding=utf-8
from bs4 import BeautifulSoup
import requests

headers = {
'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
}

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'

wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
imgs = soup.select('#a267031 > div.thumb.thumbLLR.soThumb > img')
for i in imgs:
    print(i.get('src'))
#a267031 > div.thumb.thumbLLR.soThumb > div