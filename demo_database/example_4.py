#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector.pooling
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "478890762",
    "database": "demo"
}
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = "UPDATE t_emp SET sal=sal+%s WHERE deptno=%s"
    cursor.execute(sql, (200, 20))
    con.commit()
except Exception as e:
    if "con" in dir():
        # 回滚
        con.rollback()
    print(e)
