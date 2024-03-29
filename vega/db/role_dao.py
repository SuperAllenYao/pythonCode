#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from db.mysql_db import pool


class RoleDao:
    # 查询角色列表
    def search_role_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = """SELECT id, rolename FROM t_role"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
