from selenium import webdriver
import time

url = 'https://weibo.com/2656274875/Gpzg1uODo?type=comment'
def start_chrome():
    driver = webdriver.Chrome(executable_path='/Users/fangjiaqi/github/python-code/mugglecode/spider/week3/chromedriver')
    driver.start_client()
    return driver

def find_info():
    # css_selector
    sel = 'span > span.line.S_line1 > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]

while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(6) #wait loading
    info = find_info()
    #[123,456,789]
    rep,comm,like = info
    if rep > 3000:
        print('你关注的微博转发量已经过' + str(rep))
        print(f'你喜欢的微博转发量已经超过{rep}')  #f-string
        break
    else:
        print('Not happening')
    time.sleep(1200)

print('Done')


