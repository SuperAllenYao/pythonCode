#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
con = mysql.connector.connect(host="localhost",
                              port="3306",
                              user="root",
                              password="478890762",
                              database="demo")
cursor = con.cursor()
sql = "SELECT empno,ename,hiredate FROM t_emp;"
cursor.execute(sql)
for one in cursor:
    print(one[0], one[1], one[2])
con.close()
