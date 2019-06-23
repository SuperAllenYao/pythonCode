#!/usr/bin/env python3
# -*- coding: utf-8 -*-


service_menu = {"1": "人民币转换美元",
                "2": "美元转换人民币",
                "3": "人民币转换欧元",
                "0": "结束程序"}

# 进入循环
while True:
    print('**********欢迎使用货币转换服务系统**********')
    # 从service_menu中输出服务项目
    for x, y in service_menu.items():
        print(x + '.' + y)
    # 用户选择服务
    user_input = input('请您选择需要的服务: ')
    try:
        Your_Choice = int(user_input)
    except:
        print('对不起,您输入了错误信息, 请更正后再试')
        continue
        # 判断用户的选择, 运行对应的程序
    if Your_Choice == 1:  # 人民币转美元程序
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('欢迎使用人民币转换美元服务')
        your_money = input("请输入您需要转换的人民币金额: ")
        RMB_money = int(your_money)
        print('您需要转换的人民币为: {}元'.format(RMB_money))
        RMB_to_US = RMB_money / 6.72
        print('兑换成美元为: {:.2f}$'.format(RMB_to_US))
        print('====================================')
    elif Your_Choice == 2:  # 美元转人民币程序
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('欢迎使用美元转换人民币服务')
        your_money = input("请输入您需要转换的美元金额: ")
        US_money = int(your_money)
        print('您需要转换的美元为: {}美元'.format(US_money))
        US_to_RMB = US_money * 6.72
        print('兑换成人民币为: {:.2f}¥'.format(US_to_RMB))
        print('====================================')
    elif Your_Choice == 3:  # 人民币转欧元程序
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('欢迎使用人民币转换欧元服务')
        your_money = input("请输入您需要转换的人民币金额: ")
        RMB_money = int(your_money)
        print('您需要转换的人民币为: {}元'.format(RMB_money))
        RMB_to_EUR = RMB_money * 0.13
        print('兑换成欧元为: {:.2f}欧元'.format(RMB_to_EUR))
        print('====================================')
    elif Your_Choice == 0:  # 退出服务
        print('感谢您的使用,祝您生活愉快,再见!')
        break
    else:  # 无对应的服务, 提示错误
        print('您的选择有误, 请重新选择')
        print('====================================')
