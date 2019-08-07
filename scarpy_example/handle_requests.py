#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
# 通过get方法请求腾讯的首页数据
# result = requests.get("http://www.qq.com")
# print(result.text)

print("-----------------分割线------------------")

# 构造发送数据，字典格式
data = {"name": "Allen"}
# 使用post方法发送请求，使用data关键字
result = requests.post("http://httpbin.org/post", data=data)
print(result.text)  # 查看返回数据

print("-----------------分割线------------------")

# 构造url的数据，一定要和post请求做好区分
data = {"key1": "value1", "key2": "value2"}
# 使用的是get方法请求，使用params关键字，注意区分
result = requests.get("http://httpbin.org/post", params=data)
print(result.url)  #查看是哪个url返回了信息
print(result.headers)  #查看返回“头”信息
print(result.text)  #查看返回“体”信息

print("-----------------分割线------------------")

# get方法请求图片
result = requests.get("http://www.imooc.com/static/img/index/logo.png")
# 返回的是二进制的数据，写入图片数据时，一定要使用wb模式
with open("imooc.png", "wb") as f:
    f.write(result.content)

print("-----------------分割线------------------")

# 请求json数据
result = requests.get("http://httpbin.org/ip")
# 返回的是josn格式的数据
data = result.json()
print(data)
print(data['origin'])

print("-----------------分割线------------------")

# 用timeout设置请求的超时时间
# 如在设置的时间之内没有返回数据，则会抛出一个超时的错误
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

result = requests.get("http://github.com", timeout=0.001)
print(result.text)

print("-----------------分割线------------------")

# 当前查看cookies的url
url = "http://httpbin.org/cookies"
# 使用字典类型的数据结构来构造cookie
cookies = dict(cookies_are="Hello world")
# 使用get方法来发送请求
result = requests.get(url=url, cookies=cookies)
print(result.text)
