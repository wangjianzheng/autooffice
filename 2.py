import requests
import re
'''user_agent:标识从什么设备发出请求'''

dic = {
"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}

#url = "https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6"
url = "https://km.sankuai.com/page/90524026"
resp = requests.request('get', url, headers = dic)

print(resp)
print(resp.text)
