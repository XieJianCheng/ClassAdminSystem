# -*- coding: utf-8 -*-

# 为此项目的GUI模块提供

# 用于辅助GUI模块(提供算法,也就是后台)

# 开始时间 同GUI模块


def student_get_information(student_id: int, debug_mode=False):
    """
    用于读取并返回学生详细信息, 或对文件进行排序
    :param student_id: int
    :param debug_mode: bool
    :return :学生详细信息
    """
    # 读取文件,分析数据结构并获取数据
    import re

    # StudentInformation_list 有几个元素就有几个学生信息
    StudentInformation_list = []
    re_str_1 = r'\w+:'
    re_str_2 = r':[\w|\s]+'
    if debug_mode:
        file_name = f'..\\Data\\StudentInformation.txt'
    else:
        file_name = f'Data\\StudentInformation.txt'
    with open(file_name, 'r+', encoding='utf-8') as file_object:
        words = file_object.readlines()

    temp_dict = {}
    for i in words:
        if i.strip() == '__start__':
            # 将临时字典清空
            temp_dict = {}
            continue
        elif i.strip() == '__end__':
            # 将临时的字典添加到列表
            StudentInformation_list.append(temp_dict)
            continue
        else:
            # 获取字典的键和值
            match_keys = re.findall(re_str_1, i)[0][0:-1]
            match_value = re.findall(re_str_2, i)[0][1:-1]

            # 写入字典
            # 保持 id 为[int]
            if match_keys == 'id':
                temp_dict[match_keys] = int(match_value)
            else:
                temp_dict[match_keys] = match_value

    # 返回学生详细信息
    for j in StudentInformation_list:
        got_id = j.get('id')
        if got_id == student_id:
            # 返回值为字典
            return j
    # 我觉得这是我写过的最具有含金量的一个函数


def student_add_information(adding_student_id, student_information):
    """
    用于添加学生的详细信息
    :param adding_student_id: int
    :param student_information: dict or str
    :return : 运行状态(True or False)
    """
    import re
    writing_word = """"""
    re_str = r':\d+'
    with open(f'Data\\StudentInformation.txt', 'r+', encoding='utf-8') as file_object_1:
        read_file = file_object_1.readlines()
        for j in read_file:
            match = re.findall(re_str, j)
            if len(match) != 0:
                temp_id = int(match[0][1:])
                if adding_student_id == temp_id:
                    # id重复
                    return False, 0
            writing_word += j

    # 判断信息是str还是dict
    if type(student_information) == dict:
        information_keys = student_information.keys()
        # 创建内容
        writing_word += '__start__\n'
        writing_word += f'id:{adding_student_id}\n'
        for i in information_keys:
            # 写入
            temp_string = f'{i}:{student_information.get(i)}\n'
            writing_word += temp_string
        writing_word += '__end__\n'
    elif type(student_information) == str:
        writing_word += f'__start__\nid:{adding_student_id}\n{student_information}\n__end__\n'
    else:
        return False, 1

    # 写入文件
    with open(f'Data\\StudentInformation.txt', 'w+', encoding='utf-8') as file_object_2:
        file_object_2.write(writing_word)

    return True, 0


def student_delete_information(student_id):
    """
    用于删除学生详细信息
    :param student_id:int
    :return :None
    """
    import re

    with open(f'Data\\StudentInformation.txt', 'r+', encoding='utf-8') as file_object_1:
        string_file_list_primary = file_object_1.readlines()

    # 分析数据
    start_state = False
    end_state = False
    delete_state = False
    re_str_id = r'\d+'

    # 设定删除
    string_file_list_new = string_file_list_primary
    tuple(string_file_list_primary)
    # 设定要删除的下标
    deleting_subscript_list = []
    # 记录下标
    subscript = 0
    for j in tuple(string_file_list_primary):
        # 当运行到 __start__ 或 __end__ 时
        if j.strip() == '__start__':
            start_state = True
            subscript += 1
            continue
        elif j.strip() == '__end__':
            delete_state = False
            end_state = True
            subscript += 1
            continue

        # 分析id
        if start_state:
            start_state = False
            end_state = False
            match_id = re.findall(re_str_id, j.strip())
            if len(match_id) == 0:
                subscript += 1
                continue
            final_id = int(match_id[0])
            if final_id == student_id:
                delete_state = True
                end_state = False

        # 结束条件
        if end_state:
            delete_state = False

        # 开始删除信息
        if delete_state:
            deleting_subscript_list.append(subscript)

        # 下一次循环的下标
        subscript += 1

    # 整理下标
    deleting_subscript_list.sort(reverse=True)
    temp_1 = deleting_subscript_list[0]+1
    temp_2 = deleting_subscript_list[-1]-1
    deleting_subscript_list.append(temp_1)
    deleting_subscript_list.append(temp_2)
    deleting_subscript_list.sort(reverse=True)

    # 真正的删除
    for k in deleting_subscript_list:
        del string_file_list_new[k]

    # 保存文件
    got_file = """"""
    for i in string_file_list_new:
        got_file += i
    with open(f'Data\\StudentInformation.txt', 'w+', encoding='utf-8') as file_object_2:
        file_object_2.write(got_file)

    # 这应该是我写过最久的一个函数了吧, 5天


def student_change_information(student_id, new_information_p):
    """
    于更改学生详细信息,用 从id(不含)到__end__(不含)
    只能更改已有的所有信息，而不能增加新的信息
    :param student_id : int
    :param new_information_p: dict
    """
    global final_dict
    import re

    # 将字符串转化为字典
    if type(new_information_p) == str:
        temp_str = ""
        temp_key = ""
        temp_value = ""
        final_dict = {}
        for i in new_information_p:
            if i == ':':
                temp_key = temp_str
                temp_str = ''
            elif i == '\n':
                temp_value = temp_str
                temp_str = ''
                final_dict[temp_key] = temp_value
                temp_key = ''
                temp_value = ''
            else:
                temp_str += i
    new_information = final_dict

    # 获取
    with open(f'Data\\StudentInformation.txt', 'r+', encoding='utf-8') as file_object_1:
        read_file_list = file_object_1.readlines()

    # 分析数据
    start_state = False
    end_state = False
    change_state = False
    re_str_id = r'\d+'

    # 设定要更改的下标
    changing_subscript_list = []

    # 记录下标
    subscript = 0
    for j in tuple(read_file_list):
        # 当运行到 __start__ 或 __end__ 时
        if j.strip() == '__start__':
            start_state = True
            subscript += 1
            continue
        elif j.strip() == '__end__':
            change_state = False
            end_state = True
            subscript += 1
            continue

        # 分析id
        if start_state:
            start_state = False
            end_state = False
            match_id = re.findall(re_str_id, j.strip())
            if len(match_id) == 0:
                subscript += 1
                continue
            final_id = int(match_id[0])
            if final_id == student_id:
                change_state = True
                end_state = False
                continue

        # 结束条件
        if end_state:
            change_state = False

        # 开始更改信息
        if change_state:
            changing_subscript_list.append(subscript+1)

        # 下一次循环的下标
        subscript += 1

    # 声明要写入的字符串
    writing_word = []
    # 设置内容
    for i in new_information.keys():
        writing_word.append(f'{i}:{new_information.get(i)}\n')

    # 计次
    times = -1
    for k in changing_subscript_list:
        times += 1
        read_file_list[k] = writing_word[times]

    # 写入文件
    writing_string = """"""
    for l in read_file_list:
        writing_string += l
    with open(f'Data\\StudentInformation.txt', 'w+', encoding='utf-8') as file_object_2:
        file_object_2.write(writing_string)

    return True


# 耗时5天，害
