import common
import time
import urllib.parse as ups
import json
from selenium.common.exceptions import NoSuchElementException

url_base = "https://raptor.mws.sankuai.com/cat/r/t/hourlyGraphs?"
url_first_base = "https://raptor.mws.sankuai.com/cat/r/t/hourly?"
params = "query=&reportType=hour&date=&startDate=20210723110000&endDate=20210723115900&r=06133&ip=waimai-south&group=waimai-south&domain=com.sankuai.waimai.order.trans&type=OctoService&showId=OctoService"
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

        time.sleep(2)
        # 获取核心接口10个
        pd['type'] = 'OctoService'
        pd['domain'] = k
        pd['ip'] = g
        pd['group'] = g
        pd['isSecond'] = 'false'
        pd['date'] = '2021072311'
        pd['showId'] = 'OctoService'

        url = "{}{}".format(url_first_base, ups.urlencode(pd))
        print(url)
        d.implicitly_wait(10)
        d.get(url)
        time.sleep(3)
        ifaces = d.find_element_by_xpath("/html/body/pre").text
        ifaces = json.loads(ifaces)
        ifaces = ifaces['data']['graphs']['distributionGraph']['rows']

        table_len = len(ifaces)
        if table_len > 10:
            cut_len = 10
        else:
            cut_len = table_len

        print("cutlen", cut_len)
        ifaces = ifaces[:cut_len]
        ifaces_name = []
        for i in ifaces:
            temp = i['name']
            ifaces_name.append(temp)

        for item in ifaces_name:
            line = [k, g]
            pd['showId'] = item
            pd['name'] = item
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
            tops = contents_json['data']['graphs']['tpLine']['rows']
            if not hits:
                continue
            print(type(hits[0]['Hits']))
            if not hits[0]['Hits']:
                continue

            foo = lambda s: s['Hits'] if s['Hits'] else 0.
            hoo = lambda s: s['tp99'] if s['tp99'] else 0.
            hits.sort(key=foo)
            h_num = hits[-1]['Hits']
            print(h_num)
            tops.sort(key=hoo)
            top99 = tops[-1]['tp99']

            machines = contents_json['data']['report']
            m_num = len(machines)
            qps = h_num / 60 / m_num
            print(qps)
            line.append(str(item))
            line.append(str(qps))
            line.append(str(top99))

            # result.append(";".join(line)+"\n")
            with open("qps_iface", "a+") as f:
                f.write(";".join(line) + "\n")

print("over input anykey")
input()
d.quit()
