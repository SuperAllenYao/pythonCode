# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tagurl = input('Please Enter your URL: ')
time = input('Please Enter the loop time: ')
time = int(time) # 字符串转整形
pos = input('Please Enter the LINK position: ')
pos = int(pos) # 字符串转整形
for loop in range(time+1): # 循环特定次数
    url = tagurl
    print(url)

    html = urllib.request.urlopen(url, context=ctx).read() #获取网页数据
    soup = BeautifulSoup(html, 'html.parser') #第三方库中的规定语法，分析网页中的特定标签
    tags = soup('a') #返回一个特定标签的内容，组成列表

    tags = tags[pos-1].decode() # 解码list中固定位置的数据为String
    link = re.findall('"h.+"',tags) # 查找link
    link = ''.join(link).split('"') # 取出双引号以外的部分
    tagurl = link[1] # 重新赋给这个目标链接
