from selenium import webdriver
import time
import json
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
app_keys = []
result = []
host_map_url_base = "https://avatar.mws.sankuai.com/api/v1/avatar/srv_home/{}/host_map"

with open("wjz","r") as f:
    for l in f.readlines():
        app_keys.append(l)


for k in app_keys:
    time.sleep(0.3)
    print(k, ":")
    line = []
    url = base_url.format(k)
    d.get(url)
    time.sleep(1)
    xpath = "//*[@id=\"layout\"]/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div/span/div/p/span"
    utilization_rate = WebDriverWait(d, 10, 0.5).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    time.sleep(0.5)
    line.append(str(utilization_rate.text))
    host_url = host_map_url_base.format(k)
    print(host_url, type(host_url))

    d.get(host_url)
    time.sleep(0.5)
    host_num_str = d.find_element_by_xpath("/html/body/pre").text
    host_num = json.loads(host_num_str)
    host_num = host_num['data']['chart']['rows']
    line.append(str(host_num))
    line_str = ";".join(line)
    line_str = "{}{}".format(line_str, "\n")
    result.append(line_str)

with open("machine.txt", "a+") as f:
    f.writelines(result)

x = input()
d.quit()


