# -*- coding: utf-8 -*-

# 为此项目的GUI模块提供

# 用于辅助GUI模块(提供算法,也就是后台)

# 开始时间 同GUI模块


def class_GetOrCheck_list(return_mode, debug_mode=False):
    """
    :param return_mode: 1 or 0
    :param debug_mode: True or False
    获取文件，并检查文件写入规范
    """
    import re
    if not debug_mode:
        file_name = f'Data\\StudentList.txt'
    else:
        file_name = '../Data/StudentList.txt'
    with open(file_name, 'r+', encoding='utf-8') as file_object_1:
        file_content_list = file_object_1.readlines()
    student_dict = {}
    re_str1 = r'\d+'
    re_str2 = r'[\u4e00-\u9fa5]+|[a-zA-Z]+'
    for i in file_content_list:
        if i == '\n':
            continue
        student_dict[int(re.findall(re_str1, i)[0])] = re.findall(re_str2, str(i))[0]
    id_list_new = []
    for j in student_dict.keys():
        id_list_new.append(str(j))
    id_list_final = []
    for k in id_list_new:
        id_list_final.append(int(k))
    id_list_final.sort()
    writing_word = """"""
    for l in id_list_final:
        writing_word += str(l) + ':' + student_dict.get(l) + '\n'
    with open(file_name, 'w', encoding='utf-8') as file_object_2:
        file_object_2.write(writing_word)
    if return_mode == 1:
        return student_dict


def class_add_student(student_id, student_name):
    """
    用于添加学生
    """

    # 设置要添加的学生
    writing_word = str(student_id) + ':' + student_name + '\n'

    # 打开文件并写入新
    with open(f'Data\\StudentList.txt', 'a+', encoding='utf-8') as file_object:
        file_object.write(writing_word)


def class_delete_student(student_id, student_form):
    """
    用于删除学生
    :param student_id: int
    :param student_form: dict
    """
    # 如果登录失败

    primary_List = student_form
    # 删除
    del primary_List[student_id]

    # 将字典化为储存在文件中的字符串
    final_List = """"""
    for i in primary_List.keys():
        final_List += f'{str(i)}:{primary_List.get(i)}\n'

    # 写入新数据
    with open(f'Data\\StudentList.txt', 'w', encoding='utf-8') as file_object:
        file_object.write(final_List)

    # 规范文件
    class_GetOrCheck_list(0)


def class_change_student(student_id, new_student_name, student_form):
    """
    用于修改学生
    :param student_id: int
    :param new_student_name: str
    :param student_form: dict
    """
    # 设置要修改的数据
    primary_student_form = student_form
    primary_student_form[int(student_id)] = new_student_name
    writing_word = """"""
    for i in primary_student_form.keys():
        writing_word += f'{str(i)}:{primary_student_form.get(i)}\n'

    # 写入
    with open(f'Data\\StudentList.txt', 'w+', encoding='utf-8') as file_object:
        file_object.write(writing_word)

    class_GetOrCheck_list(0)
