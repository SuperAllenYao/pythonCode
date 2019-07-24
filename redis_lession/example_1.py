#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from redis_db import pool
import redis
import time

con = redis.Redis(
    connection_pool=pool
)
con.set("country", "英国")
con.set("city", "伦敦")
city = con.get("city").decode('utf-8')
print(city)
del con
