# -*- coding: utf-8 -*-

# 为此项目的GUI模块提供

# 用于辅助GUI模块(提供算法,也就是后台)

# 开始时间 同GUI模块

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', database='class_admin_system')
cur = conn.cursor()


def student_get_information(student_id: int, debug_mode=False):
    """
    用于读取并返回学生详细信息, 或对文件进行排序
    :param student_id: int
    :@param debug_mode: bool
    :@return :学生详细信息
    """
    cur.execute(f'select * from student_info where id={student_id}')

    result = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        result.append(res)

    times = 0
    mat = 1
    final_res = {}
    for i in result[0]:
        if times == 0:
            final_res['id'] = i
        elif times == 1:
            final_res['name'] = i
        elif times == 2:
            final_res['age'] = i
        elif i is None:
            pass
        else:
            final_res[f'mation_{str(mat)}'] = i
            mat += 1
        times += 1

    return final_res


def student_add_information(adding_student_id, student_information):
    """
    用于添加学生的详细信息
    :@param adding_student_id: int
    :@param student_information: dict or str
    :@return : 运行状态(True or False)
    """
    if type(student_information) == dict:
        adding_information = student_information
    elif type(student_information) == str:
        adding_information = {}
        tmp_key = ''
        tmp_adding_key = ''
        tmp_value = ''
        state = 'write_key'
        for k in student_information:
            # 判断当前遍历到哪里
            if k == ':':
                tmp_value = ''
                state = 'write_value'
                continue
            elif k == '\n':
                tmp_adding_key = tmp_key
                tmp_key = ''
                state = 'write_key'
                adding_information[tmp_adding_key] = tmp_value
                continue
            # 判断是否便利到节点
            if state == 'write_key':
                tmp_key += k
            elif state == 'write_value':
                tmp_value += k
    else:
        return False, 2
    times = 0
    adding_info_list = [adding_student_id]
    for i in adding_information.keys():
        times += 1
        adding_info_list.append(adding_information.get(i))
    for j in range(0, 5-times):
        adding_info_list.append(None)
    adding_info_tuple = tuple(adding_info_list)
    adding_info_final = [adding_info_tuple]
    cur.executemany("insert into student_info values(%s,%s,%s,%s,%s,%s)", adding_info_final)

    conn.commit()


def student_delete_information(student_id):
    """
    用于删除学生详细信息
    :@param student_id:int
    :@return :None
    """
    cur.execute(f"delete from student_info where id={student_id}")

    conn.commit()


def student_change_information(student_id, new_information_p):
    """
    用于更改学生详细信息, 从id(不含)到__end__(不含)
    只能更改已有的所有信息，而不能增加新的信息
    :@param student_id : int
    :@param new_information_p: dict
    """
    student_delete_information(student_id)
    student_add_information(student_id, new_information_p)
