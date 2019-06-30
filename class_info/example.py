#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    """学生类"""

    def __init__(self, study_num, student_name, course=None):
        """构造方法"""
        self.study_num = study_num
        self.student_name = student_name
        self.__course = course

    @property
    def course_detail(self):
        """以属性的方式返回学生的已选课程信息"""
        return self.__course

    def add_course(self, cour_info):
        """实现添加课程信息至学生对象的已选课程属性"""
        self.__course = cour_info

    def __str__(self):
        """返回学生信息表的学生姓名，学生学号"""
        return [self.student_name, self.study_num]


class Teacher(object):
    """教师类"""

    def __init__(self, teach_num, teach_name, phone_num):
        """构造方法"""
        self.teach_num = teach_num
        self.teach_name = teach_name
        self.phone_num = phone_num

    @property
    def __str__(self):
        """返回教师编号与教师姓名属性"""
        info = [self.teach_num, self.teach_name]
        return info


class Course(Student, Teacher):
    """课程类"""

    def __init__(self, course_num, course_name, teach_name=None):
        """构造方法"""
        self.course_num = course_num
        self.course_name = course_name
        self.teach_name = teach_name

    def binding(self, teacher):
        """实现课程绑定授课教师功能"""
        if isinstance(teacher, Teacher) is True:
            teach_name = teacher.__str__
            # 绑定课程名称与教师名称,返回一个字典
            course_teacher = {self.course_name: teach_name[1]}
            return course_teacher
        else:
            return None
