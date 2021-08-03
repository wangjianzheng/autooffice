import common
import time
import urllib.parse as ups
import json
from selenium.common.exceptions import NoSuchElementException

url_base = "https://raptor.mws.sankuai.com/application/hosts?"
params = "query=&reportType=hour&date=&startDate=20210723110000&endDate=20210723115900&r=02024&ip=waimai-south&group=waimai-south&domain=com.sankuai.waimai.order.trans&type=OctoService&second=false&dataLevel=avg&templateIds=1&displaySum=true"
params_dict = ups.parse_qs(params)
pd = {}
for key in params_dict.keys():
    pd[key] = params_dict[key][0]

d = common.login()
app_key = []
with open("wjz", "r") as f:
    for line in f.readlines():
        if line.startswith("#"):
            continue
        app_key.append(line.strip("\n"))


def process_metric(xpath, line, m_name):
    try:
        load = common.wait_get(d, xpath)
        if not load:
            print("oooho")
            return
        x = load.find_elements_by_tag_name("tr")
        nums = len(x) - 1
        max_load = x[0].find_element_by_xpath("td[5]/div").text
    except NoSuchElementException:
        print("ohuo")
        return
    print(max_load)
    if max_load.endswith("K"):
        max_load = max_load.strip("K")
        max_load = float(max_load) * 1000
    max_load = float(max_load) / nums
    print(max_load)
    line.append(m_name)
    line.append("{}{}".format(str(max_load), ";"))


list_x = "//*[@id=\"app\"]/div/span/div/div/div/div[2]/div[2]"
xpath_base = "//*[@id=\"app\"]/div/span/div/div/div/div[2]/div[2]/div[{}]/div/div[3]/div/div[3]/table"
            #"//*[@id=\"app\"]/div/span/div/div/div/div[2]/div[2]/div[15]/div/div[3]/div/div[3]/table"
url_set_base = "https://raptor.mws.sankuai.com/cat/s/host/group?domain={}"
for k in app_key:
    url_set = url_set_base.format(k)
    #d.implicitly_wait(10)
    d.get(url_set)
    # time.sleep(2)
    set_text = common.wait_get(d, "/html/body/pre")
    if not set_text:
        continue
    set_text = set_text.text
    # set_text = d.find_element_by_xpath("/html/body/pre").text
    group = json.loads(set_text)['data']
    if 'set' in group:
        group = group['set']
    else:
        group = ['All']

    # group = ["waimai-south-experiment"]
    for g in group:
        line = [k, g]
        pd['domain'] = k
        pd['ip'] = g
        pd['group'] = g

        url = "{}{}".format(url_base, ups.urlencode(pd))
        print(url)
        # d.implicitly_wait(10)
        d.get(url)
        time.sleep(5)
        common.move_to_item_bottom(d, ".cat-application__lists")
        time.sleep(30)

        metrics = [1, 2, 14, 15, 16, 17]
        metrics_name = ['load', 'cpu.idle', 'jvm.gc.count', 'jvm.fullgc.count', 'jvm.gc.time', 'jvm.younggc.time']
        metrics_dict = zip(metrics, metrics_name)
        for met, m_name in metrics_dict:
            process_metric(xpath_base.format(met), line, m_name)

        with open("raptor_idx", "a+") as f:
            f.write(":".join(line) + "\n")

print("over input anykey")
input()
d.quit()
