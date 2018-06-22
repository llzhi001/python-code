import requests
from bs4 import BeautifulSoup


res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
#print(res.text)
soup = Beautifulsoup(res, 'html.parser')
print(soup.text)





