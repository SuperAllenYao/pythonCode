import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl
import re

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
url = address
a = list()
html = urllib.request.urlopen(url, context=ctx).read() #获取网页数据
soup = BeautifulSoup(html, 'html.parser') #第三方库中的规定语法，分析网页中的特定标签
tags = soup('count') #返回一个特定标签的内容，组成列表
for nums in tags:
    nums = nums.decode()
    num = re.findall('[0-9]+',nums)
    b = ''.join(num)
    b = int(b)
    a.append(b)
print(sum(a))
