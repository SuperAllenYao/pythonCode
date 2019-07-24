#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from db.type_dao import TypeDao


class TypeService():
    __type_dao = TypeDao()

    # 查询新闻类型列表
    def search_type_list(self):
        result = self.__type_dao.search_type_list()
        return result
