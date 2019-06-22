# Python学习笔记

---

[TOC]

---

## 文件读写

### 读文件

> 通过open( )方法来读取文件

```python
f = open('/Users/superallen/Desktop/12msj.txt', 'r') 	# 括号内：路径，打开模式
line = f.read()											# 将打开的文件 赋值给 line
print(line)												# 输出一下
f.close()												# 关闭文件操作，推荐每一次都要有，不然会很占电脑内存
```

### 写文件

> 写文件模式会把原来文件中的字符串覆盖

```python
f = open('/Users/superallen/Desktop/12msj_new.txt','w')		# 如果没有此文件，则会自动创建一个
f.write('23232323232323232323232332')						# 写入字符串
f.close()													# 关闭文件操作
```

---

## 函数的定义与调用

> 定义函数

```python
def mean(num_list):
    return sum(num_list) / len(num_list)

def mulitple_w(num_list):
    return [n * 10000 for n in num_list]
```

> 导入文件并且调用函数（放在同一文件夹下）

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import learn1 as le

score_card = [1,2,3,4,5,6,7,8,9,10]

mean = le.mean(score_card)
w_ed = le.mulitple_w(score_card)

mean_w = le.mean(w_ed)

print('Score: ',score_card)
print('旧值: ', mean, '新值: ', mean_w)
```

> 导入标准库

```python
# 导库操作放在代码文件的头部，语法是：import+包名
import math
```

---

## ==re.seach== 函数的使用方法(查找==特定==字符)

```python
import re
re.search("要找的字符",目标)
```

![image-20190328232350884](../截图/image-20190328232350884.png)

---

## ==re.seach== 函数的使用方法(查找==开头==字符)

> re.search()代替startswith()  ⬇️

![Screen Shot 2019-03-28 at 23.40.37](../截图/Screen Shot 2019-03-28 at 23.40.37.png)

---

## Regular Expressions ==正则表达式==

### 字符表

![Screen Shot 2019-03-29 at 17.34.49](../截图/Screen Shot 2019-03-29 at 17.34.49.png)

### 实例1 ⬇️

> 查找规则为：```'^X.*:’ = 字符’X’开头+任意字符+多次匹配+“:”字符```

![image-20190328234846755](../截图/image-20190328234846755.png)

### 实例2 ⬇️

> 查找规则为：```’^X-\S+:’ = 以字符’X’开头跟随“-’’字符+无空格+匹配大于1个条件+“:”字符```

![image-20190328235934151](../截图/image-20190328235934151.png)

### 实例3  findall() 方法⬇️

> 查找规则为：```[0-9]+```指查找多位数字字符
>
> **re.findall(‘规则’,目标)**方法返回的是一个**列表**  

![Screen Shot 2019-03-29 at 16.08.47](../截图/Screen Shot 2019-03-29 at 16.08.47.png)

---

### **贪婪模式**

默认为贪婪模式

![Screen Shot 2019-03-29 at 17.03.52](../截图/Screen Shot 2019-03-29 at 17.03.52.png)

非贪婪模式加 ？号

![image-20190329172029855](../截图/image-20190329172029855.png)

---

### 找到匹配项目并输出括号内的字符

![image-20190329172631298](../截图/image-20190329172631298.png)

---

## 使用接口

待补充

---

## 使用URL库,拉区网页数据

> 为python的内置函数，不再需要解码操作

![image-20190401122519182](../截图/image-20190401122519182.png)

> 如果需要统计文件内的字符的出现频率，这需要解码 如下⬇️

![image-20190401122708200](../截图/image-20190401122708200.png)

---

#### 拉取网页数据

![image-20190401225355036](../截图/image-20190401225355036.png)

---

## XML

### 基本语法

![Screen Shot 2019-04-01 at 23.03.17](../截图/Screen Shot 2019-04-01 at 23.03.17.png)

---

### 结构

![Screen Shot 2019-04-01 at 23.11.35](../截图/Screen Shot 2019-04-01 at 23.11.35.png)

---

### 处理XML

#### 简单树状结构的处理方法

![Screen Shot 2019-04-02 at 18.47.55](../截图/Screen Shot 2019-04-02 at 18.47.55.png)

---

#### 复杂树状结构的处理方法--findall()函数

![image-20190402185455901](../截图/image-20190402185455901.png)

---

## JSON 的处理

### 获取数据（类字典结构）- info()函数

> JSON 中的数据以key-valu对的形式存储

![image-20190402220414896](../截图/image-20190402220414896.png)

---

### 获取数据 列表内嵌字典结构 - item()函数

![image-20190402221013261](../截图/image-20190402221013261.png)

---

## API

### 使用Google API接收并、处理、导出数据 (JSON) 格式

```python
import urllib.request,urllib.parse,urllib.error
import json #导入JSON包

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?' #设置API的URL

while True:
    address = input('Enter location: ')
    if len(address) < 1: break #判断输入的字符串是否为空

    url = serviceurl + urllib.parse.urlencode({'address':address}) #先将用户输入的地址转码为UTF-8格式，再将API的URl和地址参数接合在一起
    print('Retrieved',url) #输入一下最终的URL看看
    uh = urllib.request.urlopen(url) #请求打开此URL
    data = uh.read().decode() #打开此URL后，读取数据，并解码为字符串
    print('Retrieved',len(data),'characters') #输出一下，看看数据的大小

#使用 try-except语句 尝试读取json数据
    try:
        js = json.loads(data)
    except:
        js = None

#判断js变量中的数据是否有误，检查，1.是否有js数据、2.是否有为‘status’的key，3.js中的‘status’的key值是否为OK
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data) # 输出字符串数据
        continue

    print(json.dumps(js,indent=4)) #将js转为JSON的数据结构

    lat = js["results"][0]["geometry"]["location"]["lat"] #查找数据，按位置
    lng = js["results"][0]["geometry"]["location"]["lng"] #查找数据，按位置
    print('lat',lat,'lng',lng) #输出数据
    location = js['results'][0]['formatted_address'] #查找位置数据
    print(location) #输出位置数据

```

---

## SQL 语句

### 新建数据表

```python
CREATE TABLE 数据表名 (字段名1 数据类型,字段名2 数据类型)
CREATE TABLE Users (name TEXT,age INTEGER)
```

### 插入数据

```python
'''INSERT INTO 数据表名 (字段名,字段名) VALUES ('数据值','数据值')'''
```

### 删除数据

```python
'DELETE FROM 数据表名 WHERE 字段名=? ',(变量, )
```

### 更新数据

```python
'UPDATE 数据表名 SET 字段名1="更新的值" WHERE 字段名2= ?',(变量, )
```

### 选中数据表

```python
'SELECT * FROM 数据表名'
```

### 选中数据表中的某一数据值

```python
'SELECT * FROM 数据表名 WHERE 字段名= ? ',(变量, )
```

### 数据表排序

```python
'SELECT * FROM 数据表名 ORDER BY 字段名'
```

### 判断数据表是否存在

> 如果存在 则不会新建此数据表

```python
'DROP TABLE IF EXISTS 数据表名'
```

[返回顶部](#Python学习笔记)

---

## 关系型数据库

### 一对多关系

> 在每一个字段中插入 主键 和 外键(多个)，通过  JOIN  ON 来连接

![image-20190413234402132](../截图/image-20190413234402132.png)

### 多对多关系

> 在两个数据表中，插入一张中间表作为连接使用，此中间表的主键即为两个或多个外键

![image-20190413234629277](../截图/image-20190413234629277.png)

---

## 简单的数据可视化（使用Google Map）

### 1. 创建地址数据库

 [where.data](where.data) 

### 2. 使用API获取JSON格式数据并存进数据库

```python
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
```

### 3. 对数据进行清洗

> 处理JSON格式数据，找出地理位置数据并将数据传到JS文件中

```python
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
```

---

