#coding=utf-8
import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url, code="utf-8"):
    header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
    try:
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

def main():
    for book in soup.find_all('book'):
        school_list_url = 'http://www.mhedu.sh.cn/school/list.jsp?cur_page={}&tm_id=475&xdfl=19&sdjd=&djjb=&jbzlx=&xxmc='
        getHTMLText(school_list_url)
    print(s)

main()
