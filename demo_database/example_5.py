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
    # con.start_transaction()
    cursor = con.cursor()
    # sql = "DELETE e,d FROM t_emp e JOIN t_dept d ON e.deptno=d.deptno WHERE d.deptno=20"
    sql = "TRUNCATE TABLE t_emp"
    cursor.execute(sql)
    print("操作成功")
    # con.commit()
except Exception as e:
    # if "con" in dir():
        # con.rollback()
    print(e)
