#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongo_db import client

try:
    # client.school.teacher.delete_one({"name": "李璐"})
    client.school.teacher.delete_many({})
except Exception as e:
    print(e)
