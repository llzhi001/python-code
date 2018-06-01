import requests
import time

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()   #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.baidu.com"
    total_time = 0
    for i in range(101):
        start_time = time.perf_counter()
        txt = getHTMLText(url)
        end_time = time.perf_counter()
        print("第{}次抓取耗时{:.3f}秒".format(i, end_time-start_time))
        a = '*' * int(i/5)
        b = '.' * (20 - int(i/5))
        c = (i/100)*100
        print("\r[{}->{}] {:^3.0f}%".format(a, b, c), end="")
        total_time += end_time - start_time
    print("程序执行完毕，总共耗时{:.3f}秒".format(total_time))

