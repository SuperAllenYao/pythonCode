#!/usr/bin/env python3
# -*- coding: utf-8 -*-


############################### 题目 ################################
# 编写一个 INSRET 语句部门表插入两条记录                                #
# 每条记录都在部门原有最大主键值的基础上加10                              #
####################################################################


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
    sql = """INSERT INTO t_dept
          (SELECT MAX(deptno)+10,%s,%s FROM t_dept UNION
          SELECT MAX(deptno)+20,%s,%s FROM t_dept)
          """
    cursor = con.cursor()
    cursor.execute(sql, ("A部门", "北京", "B部门", "上海"))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
