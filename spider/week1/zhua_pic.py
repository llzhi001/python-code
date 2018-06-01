import requests
import os
url = "http://image.ngchina.com.cn/2018/0601/20180601032223793.jpg"
root = "/github/python-code/spider/week1/"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url, timeout = 30)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
