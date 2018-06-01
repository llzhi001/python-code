import requests
url = "https://www.so.com/s"
keyword = "Python"
kv = {'q':keyword}
try:
    r = requests.get(url, params = kv)
    print(r.request.url)
    r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
    print(len(r.text))
except:
    print("爬取失败")
