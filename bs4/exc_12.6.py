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

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
sum = 0
list = list()
tags = soup('span')
for tag in tags:
    line = tag.decode()
    line = line.split('\n')
    for a in line:
        num = re.findall('[0-9]+', a)
        num = ''.join(num)
        list.append(num)
for b in list:
    c = int(b)
    sum = sum + c
print(sum)
