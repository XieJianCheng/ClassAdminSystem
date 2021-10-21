# -*- coding: utf-8 -*-

# 为此项目的GUI模块提供

# 用于辅助GUI模块(提供算法,也就是后台)

# 开始时间 同GUI模块

# 总sql开始时间2021.10.9 21:05

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', database='class_admin_system')
cur = conn.cursor()


def all_get_users_form(return_mode):
    """
    用于读取文件内容
    :@param return_mode:1 or 2(1为字典，2为字符串，3为user_name（list）)
    :@return: {用户名: 密码}
    """
    cur.execute("select * from user_list")

    result_1 = {}
    result_2 = """"""
    result_3 = []
    while True:
        res = cur.fetchone()
        if res is None:
            break
        result_1[res[0]] = res[1]
        result_3.append(res[0])

    for i in result_1.keys():
        result_2 += f'{i}:{result_1.get(i)}\n'

    if return_mode == 1:
        return result_1
    elif return_mode == 2:
        return result_2
    elif return_mode == 3:
        return result_3
    else:
        return False, 0


def sign_admin__check_users(user, password, users_form):
    """
    用于检查用户名和密码是否匹配
    :@param user: 用户名
    :@param password: 密码
    :@param users_form: 用户名单(dict)
    :@return: True 或 False
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
    # 注册代码
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

    # 添加信息
    sql = "insert into user_list values (%s, %s)"
    data = [(user, password)]
    cur.executemany(sql, data)

    # 保存
    conn.commit()


def admin_delete_users(user_to_deleted, password, users_form):
    """
    用于删除用户信息，需要在已登录的情况下才能执行
    :@return:None
    """
    # 如果登录失败,直接返回False以结束运行
    if not sign_admin__check_users(user=user_to_deleted, password=password, users_form=users_form):
        return False

    # 直接执行操作
    cur.execute(f"delete from user_list where user='{user_to_deleted}'")

    # 保存
    conn.commit()


def admin_update_password(user_name, primary_password, user_form_p, new_password):
    """
    用于更新密码
    :@param user_name:str
    :@param primary_password:str
    :@return : True or False
    """
    user_form = user_form_p
    # 如果登录失败,直接返回False以结束运行
    if sign_admin__check_users(user=user_name, password=primary_password, users_form=user_form)[0] is False:
        return False

    # 执行
    cur.execute(f"update user_list set pwd='{new_password}' where user='{user_name}'")

    # 保存
    conn.commit()
