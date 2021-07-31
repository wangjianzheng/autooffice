from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
base_url = "https://avatar.mws.sankuai.com/#/service/detail/info?appkey={}&env=prod"
app_keys = ["com.sankuai.waimai.order.trans"]

for k in app_keys:
    url = base_url.format(k)
    d.get(url)
    xpath = "//*[@id=\"layout\"]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[1]"

     = WebDriverWait(d, 10, 0.5).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    time.sleep(0.1)
    print(McDistr.text)

    McDistr.click()
    ActionChains(d).move_to_element_with_offset(McDistr, 0, 0).context_click(McDistr).perform()

    x = input()

    ActionChains(d).move_to_element_with_offset(McDistr, 20, 20).context_click(McDistr).perform()

    content_xpath = "//*[@id=\"layout\"]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]"
    content = WebDriverWait(d, 10, 0.5).until(
        EC.presence_of_element_located((By.XPATH, content_xpath))
    )
    # name = content.find_elements_by_tag_name("span")[0].text
    #name = d.find_element_by_xpath("//*[@id=\"layout\"]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/span[1]")

    num = content.text

    print(":", num)

#//*[@id="layout"]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/span[1]


x = input()
d.quit()
