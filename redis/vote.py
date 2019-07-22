#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模拟随机投票的功能
from redis_db import pool
import redis
import random

con = redis.Redis(
    connection_pool=pool
)

try:
    # 新建一个有序集合
    con.zadd("Candidate", {"马云": 0, "丁磊": 0, "张朝阳": 0, "马化腾": 0, "李彦宏": 0})
    # 把候选人的名字单独拿出一个列表
    names = ["马云", "丁磊", "张朝阳", "马化腾", "李彦宏"]
    for i in range(0, 300):
        # 生成一个随机数
        name_int = random.randint(0, 4)
        # 向有序集合中的一名候选人,分数加1
        con.zincrby("Candidate", 1, names[name_int])
    # 连同分数结果保存到一个变量中
    result = con.zrevrange("Candidate", 0, -1, withscores=True)
    # 循环输出结果
    for one in result:
        print(one[0].decode("utf-8"), int(one[1]))
except Exception as e:
    print(e)
finally:
    del con
