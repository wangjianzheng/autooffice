from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)
data = resp.read().decode("utf-8")


with open("baidu.html", mode="w") as f:
    f.write(data)

print("over!")