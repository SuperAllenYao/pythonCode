#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "478890762",
    "database": "vega"
}
con = mysql.connector.connect(**config)
username = '1 OR 1=1'
password = '1 OR 1=1'
# 预编译sql语句
sql = "SELECT COUNT(*) FROM t_user WHERE username=%s AND AES_DECRYPT(UNHEX(password),'Helloworld')=password%s"
cursor = con.cursor()
cursor.execute(sql, (username, password))
print(cursor.fetchone()[0])

con.close()
