from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import  WebDriverWait
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

d.get("https://km.sankuai.com/page/1026868212")
edit = WebDriverWait(d, 5, 0.5).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id=\"viewPageScrollWrapper\"]/div[1]/div[2]/div/div/button[1]"))
)
edit.click()  # 点击编辑按钮
# 获取表格，根据情况填入xpath  //*[@id="editor-22893321"]/div[1]/div/table   //*[@id="page-wrapper"]/div/div[2]
table_xpath = "//*[@class=\"ct-editor-wrapper\"]//table"
table = WebDriverWait(d, 5, 0.5).until(
    EC.presence_of_element_located((By.XPATH, table_xpath))
)

with open("wjz", "r") as f:
    for line in f.readlines():
        contents = line.split(";")
        trs = table.find_elements_by_tag_name("tr")[-1].find_elements_by_tag_name("td")[0]
        trs.click()
        # d.execute_script("arguments[0].focus()", trs)
        #ActionChains(d).move_to_element(trs).perform()
        add_row = d.find_element_by_xpath("//*[@id=\"page-wrapper\"]//div[@data-action=\"addRowAfter\"]")
        add_row.click()
        time.sleep(1)
        table = WebDriverWait(d, 5, 0.5).until(
            EC.presence_of_element_located((By.XPATH, table_xpath))
        )
        trs = table.find_elements_by_tag_name("tr")[-1].find_elements_by_tag_name("td")[0]
        d.execute_script("arguments[0].innerHTML='wjz'", trs)









        break



