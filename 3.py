import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import common


d = common.login()

head = {

}
data = {
'username': 'wangjianzheng',
'originPassword': "",
'refer': "",
'clientId': 'com.sankuai.it.ead.citadel',
'callback': 'https%3A%2F%2Fkm%2Esankuai%2Ecom%2Fsso%2Fcallback%3Foriginal-url%3D%252F',
'os': 'MacIntel',
'screen': '1792x1120',
'lt': 'LT-98708-LTbnCIb41qDQfc8o6aPsN9mIPR9iUs-ssosv.it',
'isFromSsoGw': 'false',
'isFromBj': 'false',
'sceneType': 'WebScene',
'noPwdLogin': 'false',
'webTokenInfo': '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',
'moaInfo': {"type":"success", "data": {"time":"1627909147583","moaType":"MAC","key":"ttlcHG6jV7GUWg605rKBb9FPHQSY/5d6CRFjPjJm7yJo3DxFKSfrAJ7/J16XjG0ZkiztIYPruzm3qpW+bVC/1iDAxcShj/SdRQH0gSu4jle3abbzkKUIvjqlpSRyRmXjEP6D/Eaxj4GkSldNkwRvwRK+4WdERQbxVhhBGgRQnFk=","msgType":"100","moaVersion":"1.9.2.1","content":"bs+yG4Z9K+B0CwVmlZ0rZOLWquFXGkGEv4LSB/AsqQPwfvlprEF/vZf68nCi1+AOnSD4FD43Qk7tamj49CDE7Q=="}},
'password': 'Cwg5hPhzjpDi6Apw3udKWPCWtTfaB/7AXwW1z8d4cfodZKEBFWjMI5FPFX9GWUna',
'encryptionKey': 'c512eecac4a94d83918a1795f561f0bf',
}

url = "https://raptor.mws.sankuai.com/raptor/r/hosts/metric/bigGraph"
params = {
'displaySum': 'true',
'domain': "com.sankuai.waimai.order.trans",
'endDate': "202107231159",
'endpoints': ["set-gh-tsp-order-ordertrans01", "set-gh-tsp-order-ordertrans02", "set-gh-tsp-order-ordertrans03"],
'metric': "load.1minPerCPU",
'sample': "avg",
'second': 'false',
'startDate': "202107231100",
'topK': '20',
}









