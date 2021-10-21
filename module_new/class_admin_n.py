# -*- coding: utf-8 -*-

# 为此项目的GUI模块提供

# 用于辅助GUI模块(提供算法,也就是后台)

# 开始时间 同GUI模块

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', database='class_admin_system')
cur = conn.cursor()


def class_GetOrCheck_list(return_mode=1, debug_mode=False):
    """
    :@param return_mode: 1 or 0
    :@return : dict
    获取文件，
    并检查文件写入规范,hhh遗留产物
    """
    cur.execute('select * from student_list')

    result = {}
    while True:
        res = cur.fetchone()
        if res is None:
            break
        result[res[0]] = res[1]

    return result


def class_add_student(student_id, student_name):
    """
    用于添加学生
    """
    # 直接操作
    cur.execute(f"insert into student_list values ({student_id},'{student_name}')")
    conn.commit()


def class_delete_student(student_id, student_form=None):
    """
    用于删除学生
    :@param student_id: int
    :@param student_form: dict
    """
    # 直接操作
    cur.execute(f"delete from student_list where id={student_id}")
    conn.commit()


def class_change_student(student_id, new_student_name, student_form=None):
    """
    用于修改学生
    :@param student_id: int
    :@param new_student_name: str
    :@param student_form: dict
    """
    # 直接操作
    cur.execute(f"update student_list set name='{new_student_name}' where id={student_id}")
    conn.commit()
