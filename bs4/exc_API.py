import urllib.request,urllib.parse,urllib.error
import json #导入JSON包

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?' #设置API的URL

while True:
    address = input('Enter location: ')
    if len(address) < 1: break #判断输入的字符串是否为空

    url = serviceurl + urllib.parse.urlencode({'address':address}) #先将用户输入的地址转码为UTF-8个数，再将API的URl和地址参数接合在一起
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
