'''
import urllib.request
import requests
import urllib.parse

# res = urllib.request.urlopen("http://www.baidu.com/")
# print(res.read().decode("utf-8"))
url = "http://www.baidu.com/"
dict = {"name": "haha"}
data = bytes(urllib.parse.urlencode(dict).encode("utf-8"))
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''

import requests
import json

response = requests.get("http://www.baidu.com/")
print(type(response))
print(response.status_code)
print(response.text)

data = {"name": "hah", "age": 22}
response = requests.get("http://www.baidu.com/", params=data)
print(response.text)
print(response.json)
print(type(response.json))
# print(json.loads(response.text))

res = requests.get("http://p2.qhimg.com/t014e7e8427df3681d2.png")
print(type(res.text))
print(type(res.content))
print(res.text)
print(res.content)
with open("weibo.png", "wb") as f:
    f.write(res.content)
    f.close()

headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
res1 = requests.get("http://www.baidu.com/", headers=headers)
print(res1.text)

data = {"name": "aa", "age": 20}
res2 = requests.post("http://httpbin.org/post", data=data, headers=headers)
print(res2.json())

files = {"file": open("weibo.jpg", "rb")}
res3 = requests.post("http://httpbin.org/post", files=files)
print(res3.text)

res4 = requests.get("http://www.baidu.com/")
print(res4.cookies)
print(type(res4.cookies))
for key, value in res.cookies.items():
    print(key + "-" + value)

s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456")
res5 = s.get("http://httpbin.org/cookies")
print(res5.text)

# from requests.packages import urllib3
# res6 = requests.get("https://12306.cn", verify=False)
# print(res6.status_code)

from requests.auth import HTTPBasicAuth
res7 = requests.get("",auth={"user", 123})




