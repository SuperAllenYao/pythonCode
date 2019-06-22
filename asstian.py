#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

phone_number = "匪警[110],急救[120],红十字会[999],天气预报[121212]"
weather_str = "北京,2019年12月1日,多云,8度,-13度,南风三级～上海,2019年12月2日,阴天,16度,13度,北风一级"



# 生成双色球功能
def generate_unionLotto(number):
    num = 0
    for j in range(0, int(number)):
        num += 1
        setNum = "第{}注号码为:".format(num)
        print(setNum, end=" ")
        for i in range(0, 6):
            red = random.randint(1, 33)
            print(red, end=" ")
        blue = random.randint(1,16)
        print(blue)
    print("==双色球已生成，请如需要其他功能，请输入一下的功能代码==")

# 号码百事通
def find_phone(key_Word):
    phone_list = phone_number.split(',')
    for p in phone_list:
        if p.find(key_Word) != -1:
            print("结果已找到:", p)

# 查天气
def get_weather(city):
    city_list = weather_str.split("～")
    weather_data = {}
    for i in city_list:
        w = i.split(",")
        cityDict = {"city_name":w[0], "date":w[1], "weather":w[2], "tempMax":w[3], "tempMin":w[4], "windLevl":w[5]}
        weather_data[cityDict["city_name"]] = cityDict
    if city in weather_data:
        return weather_data.get(city)
    else:
        return {}


while (True):

    print('1-双色球随机选号')
    print('2-号码百事通')
    print('3-明日天气预报')
    print('0-退出服务')

    c = input('请输入您需要使用的服务：')
    if c == "1":
        n = input("您要生成几注双色球号码：")
        generate_unionLotto(n)
    elif c == "2":
        n = input("请输入您要查询的机构或者电话号码：")
        find_phone(key_Word=n)
    elif c == "3":
        n = input("请输入您要查询的城市：")
        w = get_weather(n)
        if "city_name" in w:
            print("{date} {city_name} {weather} {tempMax} {tempMin} {windLevl}".format_map(w))
        else:
            print("未找到{0}的天气数据".format(n))
    elif c == "0":	
        break
    else:
        print("没有此功能")
    print("========================================")
print('感谢您的使用，祝您生活愉快，再见～')