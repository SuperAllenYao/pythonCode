import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# 在此输入API的key，如果有的话
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # 请用户输入的地址，用空格隔开，若地址为空，则退出循环
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()  # 创建一个空字典，用来存放address和key
    parms['address'] = address  # 将address存入"address"key中
    if api_key is not False:
        parms['key'] = api_key  # 如果API是False的话，则将默认的api_key存入“key”中
    url = serviceurl + urllib.parse.urlencode(parms)  # 对地址后的参数进行编码
    uh = urllib.request.urlopen(url, context=ctx)  # 打开此URl并读取数据
    data = uh.read().decode()  # 对此URL获取来的数据进行解码（此时data对象仍然为JSON格式）

    try:  # try-except语句
        js = json.loads(data)  # 将JSON格式的数据转换为Python可以处理的对象
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':  # 检查数据是否正常
        print('===================== 接收失败 =====================')
        continue

    place_id = js["results"][0]["place_id"]  # 输出目标位置的数据
    print(place_id)
