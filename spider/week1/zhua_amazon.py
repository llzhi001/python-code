import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
kv = {'user-agant':'Mozilla/5.0'}
try:
    r = requests.get(url, headers = kv, timeout=30)
    r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
