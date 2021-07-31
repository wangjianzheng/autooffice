from selenium import webdriver
import time
import json
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


def proc_one(url, wd):
    wd.get(url)
    time.sleep(1)
    tr_list = wd.find_elements_by_xpath("//*[@id=\"app\"]/div/div[3]/div/div[3]/table//tr")
    l = len(tr_list)
    print(l)
    # tr_list = db_table.find_elements_by_tag_name("tr")
    for i in range(l):
        print("item:", i)
        time.sleep(2)
        tr = wd.find_elements_by_xpath("//*[@id=\"app\"]/div/div[3]/div/div[3]/table//tr")[i]
        info_line_list = []
        info_line = str()
        td_list = tr.find_elements_by_tag_name("td")

        a = td_list[1].find_element_by_tag_name("a")
        info_line_list.append(a.text)
        info_line_list.append(a.get_attribute("href"))

        a1 = td_list[2].find_element_by_tag_name("a")
        info_line_list.append(a1.text)
        info_line_list.append(a1.get_attribute("href"))
        # info_line = ";".join(info_line_list)
        # print(info_line)
        # 进入处理逻辑
        a.click()
        time.sleep(1)
        # 点击db运营
        d.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[1]/div[1]/div/div/div[3]/div").click()
        time.sleep(3)
        # 计算有多少项和多少页
        t_info = {}
        try:
            next_page = wd.find_element_by_xpath("//*[@id=\"app\"]/div/div[3]/div[2]/div[2]/section/div/div[2]/div[4]/div/ul/li[contains(@class,\"mtd-pager-next\")]")
        except NoSuchElementException:
            next_page = None




        # //*[@id="app"]/div/div[3]/div[2]/div[2]/section/div/div[2]/div[4]/div/ul/li[@class='mtd-pager-next']

        # 处理一页table
        while True:
            t_tr_list = d.find_elements_by_xpath(
                "//*[@id=\"app\"]/div/div[3]/div[2]/div[2]/section/div/div[2]/div[3]/div[3]/table//tr")
            for t_tr in t_tr_list:
                t_td_list = t_tr.find_elements_by_tag_name("td")
                temp = str(t_td_list[4].find_element_by_tag_name("span").text)
                print(temp)
                if not temp.endswith("GB"):
                    # print("no")
                    continue
                temp = temp.strip("GB").strip(" ")
                if float(temp) < 100:
                    # print("no1")
                    continue

                t_info[t_td_list[1].find_element_by_xpath("./div/span/span").text] = temp
                print("table:", t_info)

            if not next_page:
                break
            flag = str(next_page.get_attribute("class"))
            print(flag)
            if flag.endswith("disabled"):
                break
            next_page.click()
            time.sleep(1)

        with open("wjz-1.txt", "a+") as f:
            info_line = ";".join(info_line_list)
            info_line = '{};{}\n'.format(info_line, str(t_info))
            f.writelines(info_line)
        wd.get(url)

        # 退出处理逻辑

chrome_options = Options()
chrome_options.add_argument('--headless')
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

d.get("https://rds.mws.sankuai.com/dba/db_manage?current=1")

temp = d.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div")
time.sleep(0.5)
if temp:
    temp.find_element_by_tag_name("i").click()

nums = d.find_element_by_xpath("//*[@id=\"app\"]/div/div[4]/div/span[2]").text
nums = str(nums).replace("共", "").replace("条", "")
nums = int(nums)
print(type(nums), nums)

total_page = int(nums / 10)

db_list_url_base = "https://rds.mws.sankuai.com/dba/db_manage?current={}"

for current in range(17, 19):
    db_list_url = db_list_url_base.format(current)
    print(db_list_url)
    time.sleep(2)
    proc_one(db_list_url, d)

d.quit()
