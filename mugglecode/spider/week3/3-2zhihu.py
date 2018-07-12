from selenium import webdriver
import time


def start_chrome():
    driver = webdriver.Chrome(executable_path='/Users/fangjiaqi/github/python-code/mugglecode/spider/week3/chromedriver')
    driver.start_client()
    return driver

def find_strangers():
    # btn
    btn_sel = 'div.ContentItem-extra > button.Button--blue'
    elems = driver.find_elements_by_css_selector(btn_sel)
    return elems

def add_fren():
    pass

while True:
    url = 'https://www.zhihu.com/'
    follower_url = 'https://www.zhihu.com/people/XXXX/followers'
    driver = start_chrome()
    driver.get(url)
    if not driver.get_cookies():
        push()
    time.sleep(20) #wait login
    driver.get(follower_url)
    time.sleep(6)  # wait for loading page & users
    strangers = find_strangers()
    for s in strangers:
        s.click()
        time.sleep(3)
    print('Done!')
    time.sleep(3000)
        #js_execute('xxx.click())
