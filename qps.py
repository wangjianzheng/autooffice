import common
import time
import urllib.parse as ups
import json
from selenium.common.exceptions import NoSuchElementException

url_base = "https://raptor.mws.sankuai.com/application/transaction/type?"
url_base = "https://raptor.mws.sankuai.com/cat/r/t/hourlyGraphs?"

params = "query=&reportType=hour&date=&startDate=20210723110000&endDate=20210723115900&r=06133&ip=waimai-south&group=waimai-south&domain=com.sankuai.waimai.order.trans&type=OctoService&showId=TOTAL"
params_dict = ups.parse_qs(params)
pd = {}
for key in params_dict.keys():
    pd[key] = params_dict[key][0]

d = common.login()
app_key = []
# group = ['waimai-south', 'waimai-north', 'waimai-west', 'waimai-east']
with open("wjz", "r") as f:
    for line in f.readlines():
        app_key.append(line.strip("\n"))

result = []
url_set_base = "https://raptor.mws.sankuai.com/cat/s/host/group?domain={}"
for k in app_key:
    url_set = url_set_base.format(k)
    d.implicitly_wait(10)
    d.get(url_set)
    set_text = d.find_element_by_xpath("/html/body/pre").text
    group = json.loads(set_text)['data']
    if 'set' in group:
        group = group['set']
    elif 'machine' in group:
        group = group['machine']
    else:
        group = []
    group.append('All')
    for g in group:
        line = [k, g]
        time.sleep(2)
        pd['domain'] = k
        pd['ip'] = g
        pd['group'] = g
        pd['isSecond'] = 'false'
        pd['date'] = '2021072311'
        url = "{}{}".format(url_base, ups.urlencode(pd))
        print(url)
        d.implicitly_wait(10)
        d.get(url)
        try:
            text = d.find_element_by_xpath("/html/body/pre").text
        except NoSuchElementException:
            continue

        contents_json = json.loads(text)
        hits = contents_json['data']['graphs']['hit']['rows']
        if not hits:
            continue
        print(type(hits[0]['Hits']))
        if not hits[0]['Hits']:
            continue

        foo = lambda s: s['Hits']
        hits.sort(key=foo)
        h_num = hits[-1]['Hits']
        print(h_num)

        machines = contents_json['data']['report']
        x = 0
        i = -1
        while machines[i]['count']<100:
            x += 1
            i -= 1
        print(x, len(machines))
        m_num = len(machines) - x
        qps = h_num/60/m_num
        print(qps)
        line.append(str(qps))
        # result.append(";".join(line)+"\n")
        with open("qps_total", "a+") as f:
            f.write(";".join(line)+"\n")

print("over input any key")
input()
d.quit()
