# coding=utf-8

# 为此项目的GUI模块提供

# 用于辅助GUI模块(提供算法,也就是后台)

# 开始时间 同GUI模块


def all_get_users_form(return_mode):
    """
    用于读取文件内容
    :param return_mode:1 or 2(1为字典，2为字符串，3为user_name（list）)
    :return: {用户名: 密码}
    """
    # 读取用户名单文件(io)
    file_name_list_read = open(f'Data\\UserList.txt', 'r')
    # 获取内容(list)
    list_name_list = file_name_list_read.readlines()

    # 获取所有用户名和密码信息(->list)
    import re
    re_str = r'\w+'
    new_list = []
    for i in list_name_list:
        new_list.append(re.findall(re_str, i))

    # 将所获取的用户名和密码转化为字典(dict)
    users_form = {}
    for j in new_list:
        users_form[j[0]] = j[1]

    # 将所获取的用户名和密码转化为字符串(str)
    returning_str = """"""
    for k in list_name_list:
        returning_str += k

    if return_mode == 1:
        return users_form
    elif return_mode == 2:
        return returning_str
    elif return_mode == 3:
        return list(users_form.keys())
    else:
        return False, 0


def sign_admin__check_users(user, password, users_form):
    """
    用于检查用户名和密码是否匹配
    :param user: 用户名
    :param password: 密码
    :param users_form: 用户名单(dict)
    :return: True 或 False
    """
    user_password = users_form.get(user, 'NotFound')
    # 判断用户名是否存在(未存在过)
    if user_password == 'NotFound':
        print("用户名不存在")
        return False, 0

    # 判断用户名是否存在(存在过,但已经被删除)
    elif user_password == 'deleted':
        print("用户已被删除")
        return False, 1

    # 判断用户名和密码是否匹配(成功)
    elif password == user_password:
        print("登录成功")
        return True, -1

    # 判断用户名和密码是否匹配(失败)
    elif password != user_password:
        print("密码错误")
        return False, 2


def sign_register_user(user, password, primary_slogan, user_form):
    """
    用于添加用户
    """
    slogan = 'xwhs'

    # 检查注册代码是否正确
    if primary_slogan != slogan:
        print("注册代码无效")
        return False, 0

    # 检查用户名是否重复
    name = user_form.get(user)
    if name is None:
        pass
    else:
        print("用户名重复")
        return False, 1

    word = f'#{user}#:{password}\n'        # 添加用户的信息

    # 打开文件
    file = open(f'Data\\UserList.txt', 'a')

    # 写入新数据
    file.write(word)

    # 关闭文件
    file.close()

    # 检查用户名是否已被删除
    form = all_get_users_form(1)
    state = sign_admin__check_users(user, password, form)
    if state[1] == 1:
        return False, 1
    return True, 0


def admin_delete_users(user_to_deleted, password, users_form):
    """
    用于删除用户信息，需要在已登录的情况下才能执行
    :return:None
    """
    # 如果登录失败,直接返回False以结束运行
    if not sign_admin__check_users(user=user_to_deleted, password=password, users_form=users_form):
        return False

    import re

    # 第一次打开文件->读取原数据
    file_form_1 = open(f'Data\\UserList.txt', 'r+')

    # 获取原数据
    list_file = file_form_1.readlines()
    new_word = """"""
    # 将获取的数据转化为字符串
    for i in list_file:
        find_deleting_user = re.findall(r'#'+user_to_deleted+r'#', i)
        if len(find_deleting_user) > 0:
            continue
        else:
            new_word += i

    # 关闭原先打开的文件对象
    file_form_1.close()

    # 打开新的文件对象->写入新数据
    file_form_2 = open(f'Data\\UserList.txt', 'w')

    # 写入新数据
    file_form_2.write(new_word)


def admin_update_password(user_name, primary_password, user_form_p, new_password):
    """
    用于更新密码
    :return : True or False
    """
    user_form = user_form_p
    # 如果登录失败,直接返回False以结束运行
    if sign_admin__check_users(user=user_name, password=primary_password, users_form=user_form)[0] is False:
        return False

    # 直接在字典更改密码
    user_form[user_name] = new_password

    # 创建新数据
    new_word = """"""
    for i in user_form.keys():
        new_word += f'#{i}#:{user_form.get(i)}\n'

    file_form_2 = open(f'Data\\UserList.txt', 'w')

    # 写入新数据
    file_form_2.write(new_word)

    return True
