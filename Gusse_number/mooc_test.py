#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from random import randint
from datetime import datetime


def guide_page(guide_word):
    """
    提示游戏进入
    参数: guide_word: 欢迎标题的文字
    """
    symbol = '********************'
    # 通过字符串格式化的操作,输出欢迎语
    print("{}{}{}".format(symbol, guide_word, symbol))


def all_num(num):
    """
    判断输入的时候为数字
    参数: num: 数字 类型str
    """
    # 判断字符串是否为数字
    if num.isdigit() is True:
        return True
    else:
        return False


def num_legal(ls: list):
    """
    判断指定数字区间是否合法
    参数: ls: 一个列表, 数据类型list
    返回值: 1 (用于判断)
    """
    # 将列表中第一和第二个元素转为int类型的数据
    start_num = int(ls[0])
    end_num = int(ls[1])
    # 比较第一和第二个元素
    if start_num == end_num:  # 相等, 提示报错且退出程序
        print("您输入的区间数字相同!! 请重新启动程序")
        sys.exit()
    elif start_num > end_num:  # 第一个元素小于第二个元素, 提示报错且退出程序
        print("您输入的区间数字大小有误!! 请重新启动程序")
        sys.exit()
    else:
        return 1


def set_final_num(num1, num2):
    """
    生成指定区间的随机数
    参数: num1: 第一个数字, num2: 第二个数字
    返回值: rest_ls: 随机数和设定的数字区间, 数据类型 list
    """
    ls = [num1, num2]
    num_ls = list(filter(lambda n: all_num(n) is True, ls))
    if len(num_ls) > 1:
        if num_legal(num_ls) == 1:
            random_num = randint(int(num_ls[0]), int(num_ls[1]) + 1)
            range_num = [int(num_ls[0]), int(num_ls[1]) + 1]
            print('所产生的随机数字区间为: {}'.format(num_ls))
            rest_ls = [random_num, range_num]
            return rest_ls
    else:
        print("您所输入的为非数字字符, 请重新启动程序")
        sys.exit()


def check_num_legal(num, range_num):
    """ 判断游戏进行中, 所输入的数字时候在区间内 """
    ls = range(range_num[0], range_num[1])
    if num in ls:
        return True
    else:
        return False


def write_record(times, value):
    """ 将用户的输入, 与游戏的本次的值, 写入日志 """
    file_name = 'record.txt'
    with open(file_name, 'a') as f:
        f.write('{}: 第{}次您猜测的数字为:{}'.format(str(times), value[0], value[1]))
        f.write('\n')


def main(rand1):
    """ 生成随机数, 并提示玩家输入, 判断输入的数字是否与随机数一致"""
    ls = [0, 0]
    count = 0
    while True:
        user_input = input('请继续输入您猜测的数字: ')
        count += 1
        if all_num(user_input) is True:
            user_num = int(user_input)
            ls[0] = count
            ls[1] = user_num
            if check_num_legal(user_num, rand1[1]) is True:
                now = datetime.now()
                write_record(now, ls)
                if user_num == rand1[0]:
                    print('***********')
                    print('恭喜你! 只用了{}次就赢得了游戏'.format(count))
                    sys.exit()
                elif user_num > rand1[0]:
                    print('***********' + '\n' + 'Higher than the answer')
                    continue
                elif user_num < rand1[0]:
                    print('***********' + '\n' + 'Lower than the answer')
                    continue
            else:
                print('对不起您输入的数字未在指定区间!!!')
                continue
        else:
            print('错误, 请输入数字!!!')
            continue


if __name__ == '__main__':
    guide_page("欢迎进入数字猜猜猜小游戏")
    i = input('数字区间起始值: ')
    j = input('数字区间终止值: ')
    temp = set_final_num(i, j)
    main(temp)
