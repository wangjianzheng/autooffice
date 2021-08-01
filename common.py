from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def login():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    d = webdriver.Chrome("/Users/wangjianzheng/webdriver/chromedriver", options=chrome_options)
    d.get("https://km.sankuai.com/")
    time.sleep(0.2)
    d.find_element_by_id("form-img").click()
    time.sleep(0.2)
    d.find_element_by_id("login-username").send_keys("wangjianzheng")
    d.find_element_by_id("login-password").send_keys("641515QWEasd@")
    time.sleep(0.5)
    d.find_element_by_id("btn-login").click()
    time.sleep(2)
    return d
