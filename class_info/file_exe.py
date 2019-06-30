#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from example import Course, Student, Teacher


def introduction(str):
    print('********************************{}********************************'.format(str))


def prepare_course():
    """ 创建课程信息初始化，并以列表形式返回所创建的8门课程对象 """
    course = {"01": "网络爬虫", "02": "数据分析",
              "03": "人工智能", "04": "机器学习",
              "05": "云计算",   "06": "大数据",
              "07": "图像识别", "08": "Web开发"}
    # 创建空列表
    l = []
    # 列表形式储存返回的课程对象
    for k, v in course.items():
        c = Course(k, v)
        l.append(c)
    return l


def create_teacher():
    """ 创建教师信息初始化，并以列表形式返回所创建的8名教师对象 """
    teacher_info = [["T1", "张亮", "13301122001"],
                    ["T2", "王朋", "13301122002"],
                    ["T3", "李旭", "13301122003"],
                    ["T4", "黄国发", "13301122004"],
                    ["T5", "周勤", "13301122005"],
                    ["T6", "谢富顺", "13301122006"],
                    ["T7", "贾教师", "13301122007"],
                    ["T8", "杨教师", "13301122008"]]
    # 创建一个空列表
    l = []
    # 把教师列表反转
    teacher_info.reverse()
    # 把每个教师都给实例化, 返回教师对象,并以列表形式储存
    for i in teacher_info:
        t = Teacher(i[0], i[1], i[2])
        l.append(t)
    return l


def course_to_teacher():
    """实现课程与教师逐一绑定（每一课程信息绑定倒叙的每一老师信息），并以列表形式返回所课程与教师的绑定结果"""
    # 创建一个空列表
    ls = []
    # 课程对象列表
    ls_course = prepare_course()
    # 教师对象列表
    ls_teacher = create_teacher()
    count = 0
    # 将课程与教师绑定,以列表的形式储存
    for course in ls_course:
        course_teacher = course.binding(ls_teacher[count])
        ls.append(course_teacher)
        count += 1
    return ls


def create_student():
    """创建学生信息初始化，并以列表形式返回所创建的8名学生对象"""
    ls_student = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    # 反转学生信息列表
    ls_student.reverse()
    # 生成学号列表
    ls_num = range(1000, 1008)
    # 创建一个空列表
    ls = []
    count = 0
    # 列表的形式储存返回的学生对象
    for i in ls_num:
        s = Student(i, ls_student[count])
        ls.append(s)
        count += 1
    return ls


if __name__ == '__main__':
    # 调用课程绑定教师函数, 并接收绑定结果
    c_to_t_rest = course_to_teacher()
    # 初始化学生信息并将接收
    student_oj_ls = create_student()
    # 打印欢迎标题
    introduction('慕课学院 (1) 班学生信息')
    # 创建一个学生名字的空列表, 后面用作key
    student_ls = []
    # 输出学生信息
    for student_info in student_oj_ls:
        print("name: {}, s_number: {}".format(student_info.__str__()[0], student_info.__str__()[1]))
        # 把学生名字加到上面的 student_ls 中
        student_ls.append(student_info.__str__()[0])
    introduction('慕课学院 (1) 班选课结果')
    count = 0
    # 创建一个空字典, 用来储存学生以及学生的选课结果
    f_rest = {}
    # 把课程与教师的绑定结果一个一个for出来
    for rest in c_to_t_rest:
        # 给学生设置课程
        student_oj_ls[count].add_course(rest)
        # 把学生的选课结果拿出来, 放到统一的结果字典里面
        for k, v in student_oj_ls[count].course_detail.items():
            dict = {'课程名称': None, '教师名称': None}
            dict['课程名称'] = k
            dict['教师名称'] = v
            f_rest[student_ls[count]] = dict
            count += 1
    # 输出最终的选课结果
    for k, v in f_rest.items():
        print('Name: {}, Selected: [{}]'.format(k, v))
