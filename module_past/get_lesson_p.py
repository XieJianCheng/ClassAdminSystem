# -*- coding: utf-8 -*-

# 为此项目的GUI模块提供

# 用于辅助GUI模块(提供算法,也就是后台)

# 开始时间 同GUI模块

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
    :param weekday: int
    """
    global found_state, today_lesson_str

    # 数字对应的课程
    lessons = {
        1: '语文',
        2: '数学',
        3: '英语',
        4: '物理',
        5: '政治',
        6: '历史',
        7: '地理',
        8: '生物',
        9: '体育',
        0: '其他'
    }

    # 读取文件
    with open(f'Data\\Lesson.txt', 'r+') as file_object_1:
        got_content_list = file_object_1.readlines()

    # 获取今天的课程
    for i in got_content_list:
        if int(i[0]) == weekday:
            found_state = True
            today_lesson_str = i[2:-1]
            break
        else:
            found_state = False

    # 分析
    if found_state:
        today_lesson_list = []
        for j in today_lesson_str:
            today_lesson_list.append(lessons.get(int(j)))
        return today_lesson_list
    else:
        return False
