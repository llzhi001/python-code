import requests
from lxml import etree
import time


def spider(the_url):
    hea = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
    r = requests.get(the_url, headers=hea)
    return r.json()

def get_all_url(page_num):
    pre_url = 'http://36kr.com/api/search-column/mainsite?per_page=20&page='
    for num in range(1, page_num+1):
        res = spider( pre_url + str(num))
        for article in res.get('data').get('items'):
            article_url = 'http://36kr.com/api/post/' + str(article.get('id')) + '/next'
            yield article_url

def spider_detail(url):
    response = spider(url)
    title = response.get('data').get('title')
    content = response.get('data').get('content').replace('</p><p>','\n')
    sel = etree.HTML(content)
    cleared_content = sel.xpath('string(//*)')
    data_writer(title, cleared_content)

def data_writer(title, cleared_content):
    with open('/Users/fangjiaqi/github/python-code/36kr/article/' + title.replace('|', '').replace('？', '') + '.txt', 'wt', encoding='utf-8') as f:
        f.write(cleared_content)
        print(title)

for url_ in get_all_url(2):
    try:
        spider_detail(url_)
    except:
        print(url_)
        continue

