#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="478890762",
        database="demo"
    )
    # 开始事务
    con.start_transaction()
    # 创建游标
    cursor = con.cursor()
    sql = """INSERT INTO t_emp(empno, ename, job, mgr, hiredate, sal, comm, deptno)
          VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (9600, "赵娜", "salesman",
                         None, "1985-12-1", 2500, None, 10))
    # 提交事务
    con.commit()

except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
finally:
    if "con" in dir():
        # 关闭数据库连接
        con.close()
