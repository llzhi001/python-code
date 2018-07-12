# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.xiaozhu.com/fangzi/25407842803.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': 'abtest_ABTest4SearchDate=b; xz_guid_4se=39e1360e-fa95-45f6-a725-b1e9c126a5ac; _ga=GA1.2.2001717627.1522379541; _gid=GA1.2.445657964.1522379541; gr_user_id=093b1355-da94-4396-b893-970b1e38ac48; __utma=29082403.2001717627.1522379541.1522379542.1522379542.1; __utmc=29082403; __utmz=29082403.1522379542.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
}

wb_data = requests.get(url,headers=headers)
time.sleep(5)
soup = BeautifulSoup(wb_data.text,'lxml')
#print(soup)
titles = soup.select('div.pho_info > h4')[0].text
address = soup.select('div.pho_info > p')[0].get('title')
prices = soup.select('div.day_l > span')[0].text
imgs = soup.select('#curBigImage')[0].get('src')
host_name = soup.select('a.lorder_name')[0].text
host_gender = soup.select('div.member_pic > div')[0].get('class')[0]
host_pic = soup.select('div.member_pic > a > img')[0].get('src')

print(titles)
print(address)
print(prices)
print(imgs)

print(host_name)
print(host_pic)

def print_gender(class_name):
    if class_name == 'member_ico1':
        return '女'
    if class_name == 'member_ico':
        return '男'

data = {
    'title':titles,
    'address':address,
    'price':prices,
    'pic':imgs,
    'host_name':host_name,
    'host_gender':print_gender(host_gender),
    'host_pic':host_pic,
}

print(data)



# -------------------补充------------------
# 如何批量获取链接

page_link = [] # <- 每个详情页的链接都存在这里，解析详情的时候就遍历这个列表然后访问就好啦~

def get_page_link(page_number):
    for each_number in range(1,page_number): # 每页24个链接,这里输入的是页码
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_number)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        for link in soup.select('a.resule_img_a'): # 找到这个 class 样为resule_img_a 的 a 标签即可
            page_link.append(link)
    print(page_link)
# ---------------------

get_page_link(3)