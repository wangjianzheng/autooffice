from selenium import webdriver
import time
import json

from selenium.webdriver import ActionChains

d = webdriver.Chrome("/Users/wangjianzheng/webdriver/chromedriver")
d.get("http://www.baidu.com/")
time.sleep(0.2)


x = d.find_element_by_xpath("//*[@id=\"s-usersetting-top\"]")
ActionChains(d).move_to_element(x).perform()
x.get_attribute()
x.text


cook = d.get_cookies()

print(cook)
