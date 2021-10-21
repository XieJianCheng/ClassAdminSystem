# -*- coding: utf-8 -*-

# 为此项目的GUI模块提供

# 用于辅助GUI模块(提供算法,也就是后台)

# 开始时间 同GUI模块

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', database='class_admin_system')
cur = conn.cursor()


def get_weekday():
    """
    返回今天星期几
    """
    from datetime import datetime
    week_day = datetime.now().weekday() + 1
    return week_day


def lesson(weekday):
    """
    获取今天有什么课
    :@param weekday: int
    """
    # 查询操作
    cur.execute(f"select * from lesson where day={weekday}")
    # 处理
    res = cur.fetchone()
    # 返回
    if res is not None:
        return list(res[1:])
    elif res is None:
        return False

# sql总结束时间2021.10.11 21:32
