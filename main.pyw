# coding=utf-8

# 第一个完整软件项目

# 班级管理

# 开始时间 2021.9.4 9:09
# 暂停时间 2021.9.12 20:32
# 开始时间 2021.9.12 21:40

import wx
from os import popen

try:
    import pymysql
    got_result = popen('mysql --help').readlines()
    assert len(got_result) > 0
except ModuleNotFoundError:
    from module_past import user_admin_p as user_admin
    from module_past import class_admin_p as class_admin
    from module_past import student_admin_p as student_admin
    from module_past import get_lesson_p as get_lesson
except AssertionError:
    from module_past import user_admin_p as user_admin
    from module_past import class_admin_p as class_admin
    from module_past import student_admin_p as student_admin
    from module_past import get_lesson_p as get_lesson
else:
    from module_new import user_admin_n as user_admin
    from module_new import class_admin_n as class_admin
    from module_new import student_admin_n as student_admin
    from module_new import get_lesson_n as get_lesson


class sign_window(wx.Frame):
    size = (400, 300)

    def __init__(self, parent=None, id=-1, debug_mode=False):
        self.dm = debug_mode
        if self.dm:
            self.run_new_window(self)
        wx.Frame.__init__(self, None, id, '六班通4.2.2 - 登录', size=self.size, pos=(750, 300))
        wx.Frame.SetMinSize(self, self.size)
        self.panel = wx.Panel(self)

        # 第一组控件
        self.title = wx.StaticText(self.panel, label='请登录')

        # 第二组控件
        self.tips_usr = wx.StaticText(self.panel, label='用户名:')
        self.input_user = wx.TextCtrl(self.panel, style=wx.TE_LEFT)

        # 第三组控件
        self.tips_pwd = wx.StaticText(self.panel, label='密码:')
        self.input_password = wx.TextCtrl(self.panel, style=wx.TE_LEFT | wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)

        # 第四组控件
        self.bt_sign = wx.Button(self.panel, label='登录')
        self.bt_clear = wx.Button(self.panel, label='清空')
        self.bt_quit = wx.Button(self.panel, label='退出')

        # 第五组控件
        self.tips_register = wx.StaticText(self.panel, label='没有账号？')
        self.bt_register = wx.Button(self.panel, label='注册')

        # 彩蛋
        self.surprise = wx.StaticText(self.panel, label=str(chr(23567))+str(chr(39759))+str(chr(22909))+str(chr(24069)), pos=(1800, 980))

        # 设置字体
        self.font_title = wx.Font(pointSize=22, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False, faceName='KaiTi')
        self.font_tips = wx.Font(pointSize=10, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.NORMAL, underline=False, faceName='SimHei')
        self.title.SetFont(self.font_title)
        self.tips_usr.SetFont(self.font_tips)
        self.tips_pwd.SetFont(self.font_tips)

        # 绑定事件
        self.bt_sign.Bind(wx.EVT_BUTTON, self.run_bt_sign)      # 登录
        self.bt_clear.Bind(wx.EVT_BUTTON, self.run_bt_clear)        # 清空
        self.bt_quit.Bind(wx.EVT_BUTTON, self.run_bt_quit)      # 退出
        self.bt_register.Bind(wx.EVT_BUTTON, self.run_bt_register_show_window)      # 注册
        self.input_password.Bind(wx.EVT_TEXT_ENTER, self.run_bt_sign)

        # 设置布局管理器
        # 第一组
        self.horizontal_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.horizontal_sizer_1.Add(self.title, proportion=0, flag=wx.ALIGN_CENTER)      # 标题

        # 第二组
        self.horizontal_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.horizontal_sizer_2.Add(self.tips_usr, proportion=1, flag=wx.ALIGN_CENTER)  # 提示1
        self.horizontal_sizer_2.Add(self.input_user, proportion=2, flag=wx.ALL | wx.ALIGN_CENTER, border=5)      # 用户名文本框

        # 第三组
        self.horizontal_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        self.horizontal_sizer_3.Add(self.tips_pwd, proportion=1, flag=wx.ALIGN_CENTER)      # 提示2
        self.horizontal_sizer_3.Add(self.input_password, proportion=2, flag=wx.HORIZONTAL | wx.ALIGN_CENTER, border=5)  # 密码文本框

        # 第四组
        self.horizontal_sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.horizontal_sizer_4.Add(self.bt_quit, proportion=1, flag=wx.HORIZONTAL | wx.ALIGN_CENTER, border=15)    # 退出按钮
        self.horizontal_sizer_4.Add(self.bt_clear, proportion=1, flag=wx.HORIZONTAL | wx.ALIGN_CENTER, border=15)    # 清空按钮
        self.horizontal_sizer_4.Add(self.bt_sign, proportion=1, flag=wx.HORIZONTAL | wx.ALIGN_CENTER, border=15)    # 登录按钮

        # 第五组
        self.horizontal_sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        self.horizontal_sizer_5.Add(self.tips_register, proportion=0, flag=wx.ALIGN_CENTER)
        self.horizontal_sizer_5.Add(self.bt_register, proportion=2, flag=wx.HORIZONTAL | wx.ALIGN_CENTER, border=15)

        # 纵向
        self.vertical_sizer = wx.BoxSizer(wx.VERTICAL)
        self.vertical_sizer.Add(self.horizontal_sizer_1, proportion=1, flag=wx.TOP | wx.ALIGN_CENTER, border=10)
        self.vertical_sizer.Add(self.horizontal_sizer_2, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER | wx.ALL, border=5)
        self.vertical_sizer.Add(self.horizontal_sizer_3, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER | wx.ALL, border=5)
        self.vertical_sizer.Add(self.horizontal_sizer_4, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER | wx.ALL, border=5)
        self.vertical_sizer.Add(self.horizontal_sizer_5, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER | wx.ALL, border=5)

        # 调用尺寸管理器
        self.panel.SetSizer(self.vertical_sizer)

        # 图标
        try:
            open('Image/icon.ico', 'rb')
        except FileNotFoundError:
            print("没有找到图标文件")
            wx.MessageBox("没有找到图标文件", "请导入图标文件")
        else:
            self.icon = wx.Icon(name="Image/icon.ico", type=wx.BITMAP_TYPE_ICO)
            self.SetIcon(self.icon)

    @staticmethod
    def run_bt_register_show_window(event, open_mode=False):
        class register_window(wx.Frame):
            size = (280, 180)

            def __init__(self, parent=None, id=-1):
                wx.Frame.__init__(self, None, id, '注册', size=self.size, pos=(860, 400))
                wx.Frame.SetMaxSize(self, self.size)
                wx.Frame.SetMinSize(self, self.size)

                panel = wx.Panel(self)

                # 第一行
                self.tip1 = wx.StaticText(panel, label='请设置用户名:', pos=(10, 10))
                self.input1 = wx.TextCtrl(panel, style=wx.TE_LEFT, pos=(110, 10))

                # 第二行
                self.tip2 = wx.StaticText(panel, label='请设置密码:', pos=(10, 40))
                self.input2 = wx.TextCtrl(panel, style=wx.TE_LEFT | wx.TE_PASSWORD, pos=(110, 40))

                # 第三行
                self.tip3 = wx.StaticText(panel, label='请输入注册代码:', pos=(10, 70))
                self.input3 = wx.TextCtrl(panel, style=wx.TE_LEFT | wx.TE_PASSWORD, pos=(110, 70))

                # 第四行
                self.bt4 = wx.Button(panel, label='注册', pos=(100, 100))

                # 绑定事件
                self.bt4.Bind(wx.EVT_BUTTON, self.run_bt4)

                # 图标
                try:
                    open('Image/icon.ico', 'rb')
                except FileNotFoundError:
                    print("没有找到图标文件")
                    wx.MessageBox("没有找到图标文件", "请导入图标文件")
                else:
                    self.icon = wx.Icon(name="Image/icon.ico", type=wx.BITMAP_TYPE_ICO)
                    self.SetIcon(self.icon)

            def run_bt4(self, event):
                run_register = user_admin.sign_register_user(user=self.input1.GetValue(), password=self.input2.GetValue(), primary_slogan=self.input3.GetValue(), user_form=user_admin.all_get_users_form(1))
                if run_register[0] is True:
                    wx.MessageBox('注册成功！\n请继续登录', '注册成功！')
                    frame_register.Close(True)

                    # 重新显示登录窗口
                    app_register_new = wx.App()
                    frame_sign_new = sign_window(parent=None, id=-1)
                    frame_sign_new.Show()
                    app_register_new.MainLoop()
                elif run_register[1] == 1:
                    pass

                elif run_register[1] == 0:
                    wx.MessageBox('注册代码无效'+str(run_register), '注册失败')
                elif run_register[1] == 1:
                    wx.MessageBox('用户名重复'+str(run_register), '注册失败')
                else:
                    wx.MessageBox('按[确定]退出程序'+str(run_register), '未知错误')
                    frame_register.Close()

        if open_mode:
            frame_sign.Close()
        app_register = wx.App()
        global frame_register
        frame_register = register_window(parent=None, id=-1)
        frame_register.Show()
        app_register.MainLoop()

    def run_bt_sign(self, event):
        """
        用于执行登录操作
        """
        user_form = user_admin.all_get_users_form(1)
        # 获取登录状态
        signing_state = user_admin.sign_admin__check_users(user=self.input_user.GetValue(), password=self.input_password.GetValue(), users_form=user_form)
        """
        [此记录往上一行]
        bug记录:
        导入模块后未对路径进行修改，导致bug
        解决方案:
        重新设置路径
        """

        # 如果用户名和密码匹配
        if signing_state[0] is True:
            self.run_new_window(None)
        elif signing_state[1] == 0:
            self.input_user.SetValue('')
            wx.MessageBox("用户名不存在"+str(signing_state), "登录失败")
        elif signing_state[1] == 1:
            self.run_bt_clear(None)
            wx.MessageBox('用户已被删除，请重新注册'+str(signing_state), '登录失败')
        elif signing_state[1] == 2:
            self.input_password.SetValue('')
            wx.MessageBox('密码错误'+str(signing_state), '登录失败')

    def run_bt_clear(self, event):
        self.input_user.SetValue('')
        self.input_password.SetValue('')

    @staticmethod
    def run_bt_quit(event):
        import sys
        sys.exit()

    def run_new_window(self, event):
        # 记录登录信息
        final_user = self.input_user.GetValue()
        final_pwd = self.input_password.GetValue()
        # 返回登录信息

        # 关闭旧窗口, 打开新窗口
        global app_new_window, frame_main
        if not self.dm:
            frame_sign.Close(True)
        app_new_window = wx.App()
        frame_main = main_window(parent=None, id=-1, past_user=final_user, past_pwd=final_pwd)
        frame_main.Show()
        app_new_window.MainLoop()

        return final_user, final_pwd


class main_window(wx.Frame):
    def __init__(self, parent, id, past_user, past_pwd):
        # 记录登录的账号密码
        global user, pwd
        user = past_user
        pwd = past_pwd

        # 创建窗口
        wx.Frame.__init__(self, None, id, '班级管理系统', size=(800, 700), pos=(565, 170))
        # 尺寸
        wx.Frame.SetMinSize(self, size=(800, 700))
        wx.Frame.SetMaxSize(self, size=(800, 700))

        # 创建导航栏画板
        self.panel_bar = wx.Panel(self, pos=(0, 0), size=(240, 700))

        # 文字
        title_1 = wx.StaticText(self.panel_bar, label='初二(6)班 - 班级管理', pos=(20, 30))
        title_2 = wx.StaticText(self.panel_bar, label='（六班通4.2.2）', pos=(60, 60))
        tip = wx.StaticText(self.panel_bar, label='其他选项', pos=(63, 100))
        # 设置字体
        font_title = wx.Font(pointSize=15, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False, faceName='KaiTi')
        font_tip = wx.Font(pointSize=18, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False, faceName='SimHei')
        self.font_time = wx.Font(pointSize=12, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False, faceName='KaiTi')
        title_1.SetFont(font_title)
        title_2.SetFont(self.font_time)
        tip.SetFont(font_tip)
        # 显示时间
        self.timer = wx.PyTimer(self.show_time)
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.show_time()
        # 5个按钮
        bt_main = wx.Button(self.panel_bar, label='主页', pos=(32, 170), size=(170, 50))
        bt_StudentAdmin = wx.Button(self.panel_bar, label='学生管理', pos=(32, 260), size=(170, 50))
        bt_students = wx.Button(self.panel_bar, label='打开花名册', pos=(32, 350), size=(170, 50))
        bt_UserAdmin = wx.Button(self.panel_bar, label='账号管理', pos=(32, 440), size=(170, 50))
        bt_quit = wx.Button(self.panel_bar, label='退出', pos=(32, 530), size=(170, 50))
        # 绑定事件
        bt_main.Bind(wx.EVT_BUTTON, self.run_bt_main)
        bt_StudentAdmin.Bind(wx.EVT_BUTTON, self.run_bt_StudentAdmin)
        bt_students.Bind(wx.EVT_BUTTON, self.run_bt_students)
        bt_UserAdmin.Bind(wx.EVT_BUTTON, self.run_bt_UserAdmin)
        bt_quit.Bind(wx.EVT_BUTTON, self.run_bt_quit)

        # 创建其他画板
        self.panel_main = wx.Panel(self, pos=(241, 0), size=(559, 700))
        self.panel_StudentAdmin = wx.Panel(self, pos=(241, 0), size=(559, 700))
        self.panel_UserAdmin = wx.Panel(self, pos=(241, 0), size=(559, 700))

        # 首先打开主页
        self.run_bt_main(self)

        # 图标
        try:
            open('Image/icon.ico', 'rb')
        except FileNotFoundError:
            print("没有找到图标文件")
            wx.MessageBox("没有找到图标文件", "请导入图标文件")
        else:
            self.icon = wx.Icon(name="Image/icon.ico", type=wx.BITMAP_TYPE_ICO)
            self.SetIcon(self.icon)

    # 时间, 完成
    def show_time(self):
        # 获取时间
        import time
        got_time = time.localtime(time.time())
        showing_time = time.strftime('%Y-%m-%d %a %H:%M:%S', got_time)
        # 显示时间
        try:
            show_time = wx.StaticText(self.panel_bar, label=showing_time, pos=(18, 610))
            show_time.SetFont(self.font_time)
        except RuntimeError:
            pass

    # 退出, 完成
    @staticmethod
    def run_bt_quit(event):
        import sys
        sys.exit()

    # 主页, 完成
    def run_bt_main(self, event):
        # 删除其他面板
        if self.panel_main:
            self.panel_main.Destroy()
        if self.panel_StudentAdmin:
            self.panel_StudentAdmin.Destroy()
        if self.panel_UserAdmin:
            self.panel_UserAdmin.Destroy()
        # 创建新面板
        self.panel_main = wx.Panel(self, pos=(241, 0), size=(559, 700))

        # 创建内容
        title_all = wx.StaticText(self.panel_main, label='主页', pos=(220, 16))
        div_1_title = wx.StaticText(self.panel_main, label='基本信息:', pos=(40, 100))
        div_1_content_1 = wx.StaticText(self.panel_main, label='班主任：钟鑫', pos=(40, 150))
        div_1_content_2 = wx.StaticText(self.panel_main, label='班长：高佳', pos=(40, 190))
        div_1_content_3 = wx.StaticText(self.panel_main, label='学生人数: 49人', pos=(40, 230))
        div_2_title = wx.StaticText(self.panel_main, label='最新消息:', pos=(40, 310))
        div_2_content_1 = wx.StaticText(self.panel_main, label='………………………', pos=(40, 370))
        div_2_content_2 = wx.StaticText(self.panel_main, label='………………………', pos=(40, 410))
        div_2_content_3 = wx.StaticText(self.panel_main, label='………………………', pos=(40, 450))
        div_2_content_4 = wx.StaticText(self.panel_main, label='………………………', pos=(40, 490))
        div_2_content_5 = wx.StaticText(self.panel_main, label='………………………', pos=(40, 530))
        # 设置字体
        global font_all_title, font_div_content, font_div_title
        font_all_title = wx.Font(28, wx.DEFAULT, wx.NORMAL, wx.BOLD, False, 'Microsoft YaHei')
        font_div_title = wx.Font(pointSize=18, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.BOLD, underline=False, faceName='SimHei')
        font_div_content = wx.Font(pointSize=15, family=wx.DEFAULT, style=wx.NORMAL, weight=wx.LIGHT, underline=False, faceName='DFKai-SB')
        title_all.SetFont(font_all_title)
        div_1_title.SetFont(font_div_title)
        div_1_content_1.SetFont(font_div_content)
        div_1_content_2.SetFont(font_div_content)
        div_1_content_3.SetFont(font_div_content)
        div_2_title.SetFont(font_div_title)
        div_2_content_1.SetFont(font_div_content)
        div_2_content_2.SetFont(font_div_content)
        div_2_content_3.SetFont(font_div_content)
        div_2_content_4.SetFont(font_div_content)
        div_2_content_5.SetFont(font_div_content)

        # 课程表
        lesson_schedule_text = wx.StaticText(self.panel_main, label='今日课程表', pos=(320, 99))
        lesson_schedule_text.SetFont(font_div_title)
        # 获取课程
        got_lesson = get_lesson.lesson(get_lesson.get_weekday())        # 今天所有课程, 是一个list或(False, 'Today is weekend')
        if got_lesson is False:
            show_lesson = wx.StaticText(self.panel_main, label='今天是周末！', pos=(327, 160))
            show_lesson.SetFont(font_div_content)
        else:
            # 显示课程, 方式有点死, 但是没办法了
            show_line_1 = wx.StaticText(self.panel_main, label='-'*6 + '上午' + '-'*6, pos=(320, 150))
            show_lesson_1 = wx.StaticText(self.panel_main, label=got_lesson[0], pos=(364, 180))
            show_lesson_2 = wx.StaticText(self.panel_main, label=got_lesson[1], pos=(364, 220))
            show_lesson_3 = wx.StaticText(self.panel_main, label=got_lesson[2], pos=(364, 260))
            show_lesson_4 = wx.StaticText(self.panel_main, label=got_lesson[3], pos=(364, 300))
            show_line_2 = wx.StaticText(self.panel_main, label='-'*6 + '下午' + '-'*6, pos=(320, 330))
            show_lesson_5 = wx.StaticText(self.panel_main, label=got_lesson[4], pos=(364, 360))
            show_lesson_6 = wx.StaticText(self.panel_main, label=got_lesson[5], pos=(364, 400))
            show_lesson_7 = wx.StaticText(self.panel_main, label=got_lesson[6], pos=(364, 440))
            show_lesson_8 = wx.StaticText(self.panel_main, label=got_lesson[7], pos=(364, 480))
            # 字体
            font_line = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT, False, 'KaiTi')
            show_line_1.SetFont(font_line)
            show_line_2.SetFont(font_line)
            show_lesson_1.SetFont(font_div_content)
            show_lesson_2.SetFont(font_div_content)
            show_lesson_3.SetFont(font_div_content)
            show_lesson_4.SetFont(font_div_content)
            show_lesson_5.SetFont(font_div_content)
            show_lesson_6.SetFont(font_div_content)
            show_lesson_7.SetFont(font_div_content)
            show_lesson_8.SetFont(font_div_content)

        # 表情包
        img = wx.Image('Image/img_1.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self.panel_main, -1, img, (400, 523), (img.GetWidth(), img.GetHeight()))
        # 关于
        bt_about = wx.Button(self.panel_main, label='关于本软件', pos=(40, 600), size=(100, 40))
        bt_about.Bind(wx.EVT_BUTTON, self.run_bt_about)

    # 关于
    @staticmethod
    def run_bt_about(event):
        about = """
        本软件1.0版本2月23号发布，
        4.x于版本9月4日正式开发，现已进入4.2版本，耗时1个月
        
        目前除了MySQL数据处理，其他大部分功能没有bug，
        因各种原因，MySQL数据处理模块将不提供错误处理，本次版本也不支持编译
        相应功能在txt数据处理模块更为完善
        
        更新日志 4.2：
        新增MySQL数据处理模块，
        数据不易被篡改
        本项目已于10月11日停止主流开发，
        本软件将于10月16完全停止维护
        
        这个项目还是以学习和练习为主，
        下一个项目将注重用户体验进行开发
        
        六班通项目开发者        
        2021年10月12日"""
        wx.MessageBox(about, '关于本软件')

    # 学生管理, 完成
    def run_bt_StudentAdmin(self, event):
        # 删除其他面板
        if self.panel_main:
            self.panel_main.Destroy()
        if self.panel_StudentAdmin:
            self.panel_StudentAdmin.Destroy()
        if self.panel_UserAdmin:
            self.panel_UserAdmin.Destroy()
        # 创建新面板
        self.panel_StudentAdmin = wx.Panel(self, pos=(241, 0), size=(559, 700))

        # 上半部分
        # 标题
        title = wx.StaticText(self.panel_StudentAdmin, label='学生管理', pos=(180, 16))
        # 搜索框
        tip_search = wx.StaticText(self.panel_StudentAdmin, label='请输入学生的id:', pos=(40, 100))
        global input_search, show_student_information
        input_search = wx.TextCtrl(self.panel_StudentAdmin, style=wx.TE_CENTER | wx.TE_PROCESS_ENTER, pos=(240, 100), size=(60, 24))
        bt_search = wx.Button(self.panel_StudentAdmin, label='查询', pos=(310, 99), size=(60, 27))
        bt_change = wx.Button(self.panel_StudentAdmin, label='修改', pos=(379, 99), size=(60, 27))
        bt_delete = wx.Button(self.panel_StudentAdmin, label='删除', pos=(447, 99), size=(60, 27))
        # 具体内容
        show_student_information = wx.StaticText(self.panel_StudentAdmin, label='待查询', pos=(100, 160))
        # 字体
        title.SetFont(font_all_title)
        tip_search.SetFont(font_div_title)
        show_student_information.SetFont(font_div_content)
        # 绑定事件
        input_search.Bind(wx.EVT_TEXT_ENTER, self.get_information)
        bt_search.Bind(wx.EVT_BUTTON, self.get_information)
        bt_change.Bind(wx.EVT_BUTTON, self.change_information)
        bt_delete.Bind(wx.EVT_BUTTON, self.delete_information)

        # 下半部分
        # 内容
        tip = wx.StaticText(self.panel_StudentAdmin, label='其他选项：', pos=(40, 520))
        bt_add_information = wx.Button(self.panel_StudentAdmin, label='添加学生信息', pos=(40, 560), size=(110, 35))
        bt_show_students = wx.Button(self.panel_StudentAdmin, label='打开学生名单', pos=(40, 600), size=(110, 35))
        # 字体
        tip.SetFont(font_div_title)
        # 事件
        bt_add_information.Bind(wx.EVT_BUTTON, self.add_information)
        bt_show_students.Bind(wx.EVT_BUTTON, self.show_students)

        # 表情包
        img = wx.Image('Image/img_2.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self.panel_StudentAdmin, -1, img, (430, 523), (img.GetWidth(), img.GetHeight()))

    # 获取学生名单, 辅助, 完成, GUI
    def show_students(self, event):
        class show_students_window(wx.Frame):
            def __init__(self, parent=None, id=-1):
                # 创建窗口
                wx.Frame.__init__(self, None, id, '获取学生名单', size=(300, 400), pos=(765, 270))
                # 尺寸
                wx.Frame.SetMinSize(self, size=(300, 400))
                wx.Frame.SetMaxSize(self, size=(300, 400))
                # 画板
                pnl = wx.Panel(self)

                # 内容
                get_content_dict = class_admin.class_GetOrCheck_list(1)
                # 懂的
                get_content_str = """"""
                for i in get_content_dict.keys():
                    get_content_str += f'{i}：{get_content_dict.get(i)}\n'
                show_content = wx.StaticText(pnl, label=get_content_str, pos=(30, 30))
                # 打开文件的按钮
                bt_open_file = wx.Button(pnl, label='打\n开\n名\n单\n文\n件', pos=(220, 30), size=(40, 130))
                # 事件
                bt_open_file.Bind(wx.EVT_BUTTON, self.open_file)

                # 图标
                try:
                    open('Image/icon.ico', 'rb')
                except FileNotFoundError:
                    print("没有找到图标文件")
                    wx.MessageBox("没有找到图标文件", "请导入图标文件")
                else:
                    self.icon = wx.Icon(name="Image/icon.ico", type=wx.BITMAP_TYPE_ICO)
                    self.SetIcon(self.icon)

            @staticmethod
            def open_file(event):
                import os
                os.startfile(f'{os.getcwd()}\\Data\\StudentList.txt')

        app_StudentsWindow = wx.App()
        frame_AddWindow = show_students_window(parent=None, id=-1)
        frame_AddWindow.Show()
        app_StudentsWindow.MainLoop()

    # 添加学生信息, 辅助, 完成, GUI
    def add_information(self, event):
        class add_window(wx.Frame):
            def __init__(self, parent=None, id=-1):
                # 创建窗口
                wx.Frame.__init__(self, None, id, '添加学生信息', size=(300, 400), pos=(765, 270))
                # 尺寸
                wx.Frame.SetMinSize(self, size=(300, 400))
                wx.Frame.SetMaxSize(self, size=(300, 400))
                # 画板
                pnl = wx.Panel(self)

                # 控件
                tip_1 = wx.StaticText(pnl, label='请输入要添加的id：', pos=(20, 23))
                self.input_1 = wx.TextCtrl(pnl, style=wx.TE_CENTER, pos=(140, 20), size=(36, 22))
                tip_2 = wx.StaticText(pnl, label='请输入学生信息(标准格式)', pos=(20, 60))
                self.input_2 = wx.TextCtrl(pnl, style=wx.TE_MULTILINE, pos=(20, 80), size=(242, 230))
                bt = wx.Button(pnl, label='添加', pos=(100, 320))
                # 事件
                bt.Bind(wx.EVT_BUTTON, self.run_add)

                # 图标
                try:
                    open('Image/icon.ico', 'rb')
                except FileNotFoundError:
                    print("没有找到图标文件")
                    wx.MessageBox("没有找到图标文件", "请导入图标文件")
                else:
                    self.icon = wx.Icon(name="Image/icon.ico", type=wx.BITMAP_TYPE_ICO)
                    self.SetIcon(self.icon)

            # 处理
            def run_add(self, event):
                try:
                    adding_id = int(self.input_1.GetValue())
                except ValueError:
                    wx.MessageBox('id应为数字', '错误')
                    self.input_1.SetValue('')
                else:
                    adding_information = self.input_2.GetValue()
                    run = student_admin.student_add_information(adding_id, adding_information)
                    if run[0] is not True:
                        wx.MessageBox('id重复'+str(run), '错误')
                        self.input_1.SetValue('')
                    else:
                        wx.MessageBox('添加成功！', '成功')
                        frame_AddWindow.Close()

        app_AddWindow = wx.App()
        frame_AddWindow = add_window(parent=None, id=-1)
        frame_AddWindow.Show()
        app_AddWindow.MainLoop()

    # 修改学生信息, 辅助, 完成, GUI
    def change_information(self, event):
        changing_id_p = input_search.GetValue()

        class change_window(wx.Frame):
            def __init__(self, parent=None, id=-1):
                wx.Frame.__init__(self, None, id, '修改学生信息', size=(300, 400), pos=(765, 270))
                # 尺寸
                wx.Frame.SetMinSize(self, size=(300, 400))
                wx.Frame.SetMaxSize(self, size=(300, 400))
                # 画板
                pnl = wx.Panel(self)

                # 控件
                tip_1 = wx.StaticText(pnl, label='修改学生信息：', pos=(100, 20))
                tip_2 = wx.StaticText(pnl, label='请输入学生信息(标准格式)', pos=(20, 60))
                self.input_2 = wx.TextCtrl(pnl, style=wx.TE_MULTILINE, pos=(20, 80), size=(242, 230))
                bt = wx.Button(pnl, label='修改', pos=(100, 320))
                # 事件
                bt.Bind(wx.EVT_BUTTON, self.run_change)

                # 图标
                try:
                    open('Image/icon.ico', 'rb')
                except FileNotFoundError:
                    print("没有找到图标文件")
                    wx.MessageBox("没有找到图标文件", "请导入图标文件")
                else:
                    self.icon = wx.Icon(name="Image/icon.ico", type=wx.BITMAP_TYPE_ICO)
                    self.SetIcon(self.icon)

            # 处理
            def run_change(self, event):
                try:
                    changing_id = int(changing_id_p)
                except ValueError:
                    wx.MessageBox('请输入一个数字', '错误')
                else:
                    changing_information = self.input_2.GetValue()
                    run = student_admin.student_change_information(changing_id, changing_information)
                    if run is not True:
                        wx.MessageBox('id重复'+str(run), '错误')
                    else:
                        wx.MessageBox('修改成功！', '成功')
                        frame_ChangingWindow.Close()

        app_ChangingWindow = wx.App()
        frame_ChangingWindow = change_window(parent=None, id=-1)
        frame_ChangingWindow.Show()
        app_ChangingWindow.MainLoop()

    # 删除学生信息, 辅助, 完成, GUI
    @staticmethod
    def delete_information(event):
        deleting_id_p = input_search.GetValue()
        try:
            deleting_id = int(deleting_id_p)
        except ValueError:
            wx.MessageBox('id应为数字', '错误')
            input_search.SetValue('')
        else:
            run_1 = student_admin.student_delete_information(deleting_id)
            run_2 = class_admin.class_delete_student(deleting_id, class_admin.class_GetOrCheck_list(1))
            wx.MessageBox('删除成功！', '成功')

    # 获取学生信息, 辅助, 完成
    @staticmethod
    def get_information(event):
        try:
            int(input_search.GetValue())
        except ValueError:
            show_student_information.SetLabel('输入的内容应为数字')
        else:
            # 获取数据
            got_information = student_admin.student_get_information(student_id=int(input_search.GetValue()))
            # 处理获取到的数据
            if got_information is None:
                show_student_information.SetLabel('该id不存在')
            else:
                final_show = """"""
                for i in got_information.keys():
                    final_show += f'{i}: {got_information.get(i)}\n'
                #  显示内容
                show_student_information.SetLabel('得到的结果为:\n\n'+final_show)

    # 花名册, 完成
    @staticmethod
    def run_bt_students(event):
        # 设置文件
        import os
        file_dir = f'{os.getcwd()}\\Data\\StudentsFrom.xls'
        # 打开文件
        os.startfile(file_dir)

        wx.MessageBox(f'花名册位置：\n{file_dir}', '已打开文件')

    # 账号管理, 完成
    def run_bt_UserAdmin(self, event):
        # 删除其他面板
        if self.panel_main:
            self.panel_main.Destroy()
        if self.panel_StudentAdmin:
            self.panel_StudentAdmin.Destroy()
        if self.panel_UserAdmin:
            self.panel_UserAdmin.Destroy()
        # 创建新面板
        self.panel_UserAdmin = wx.Panel(self, pos=(241, 0), size=(559, 700))

        # 获取所有账号
        run = user_admin.all_get_users_form(3)
        show_run = """"""
        for i in run:
            show_run += f'  {i}\n'

        # 控件
        title = wx.StaticText(self.panel_UserAdmin, label='账号管理', pos=(180, 16))
        show_signed_user = wx.StaticText(self.panel_UserAdmin, label='当前账号：'+user, pos=(20, 85))
        show_user_list_title = wx.StaticText(self.panel_UserAdmin, label='当前所有用户：', pos=(52, 130))
        show_user_list = wx.StaticText(self.panel_UserAdmin, label=show_run, pos=(52, 170))
        tip_more = wx.StaticText(self.panel_UserAdmin, label='其他选项：', pos=(302, 130))
        bt_open_UserList_file = wx.Button(self.panel_UserAdmin, label='打开文件', pos=(307, 170), size=(100, 40))
        bt_register = wx.Button(self.panel_UserAdmin, label='注册用户', pos=(307, 220), size=(100, 40))
        bt_update_pwd = wx.Button(self.panel_UserAdmin, label='更改密码', pos=(307, 270), size=(100, 40))
        bt_delete_user = wx.Button(self.panel_UserAdmin, label='注销用户', pos=(307, 320), size=(100, 40))
        bt_change_sign_user = wx.Button(self.panel_UserAdmin, label='切换用户', pos=(307, 370), size=(100, 40))
        # 字体
        title.SetFont(font_all_title)
        show_signed_user.SetFont(self.font_time)
        show_user_list_title.SetFont(font_div_title)
        show_user_list.SetFont(font_div_content)
        tip_more.SetFont(font_div_title)
        # 事件
        bt_open_UserList_file.Bind(wx.EVT_BUTTON, self.run_bt_open_UserList_file)
        bt_register.Bind(wx.EVT_BUTTON, self.run_bt_register)
        bt_update_pwd.Bind(wx.EVT_BUTTON, self.run_bt_update_pwd)
        bt_delete_user.Bind(wx.EVT_BUTTON, self.run_bt_delete_user)
        bt_change_sign_user.Bind(wx.EVT_BUTTON, self.run_bt_change_sign_user)

        # 表情包
        img = wx.Image('Image/img_3.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self.panel_UserAdmin, -1, img, (375, 483), (img.GetWidth(), img.GetHeight()))

    # 打开文件, 辅助, 完成
    @staticmethod
    def run_bt_open_UserList_file(event):
        import os
        file_dir = f'{os.getcwd()}\\Data\\UserList.txt'
        os.startfile(file_dir)
        wx.MessageBox(f'文件位置：\n{file_dir}\n', '已打开文件')

    # 注册用户, 辅助, 完成, 引用GUI
    @staticmethod
    def run_bt_register(event):
        sign_window.run_bt_register_show_window(None, False)

    # 更新密码, 辅助, 完成, GUI
    def run_bt_update_pwd(self, event):
        class update_pwd_window(wx.Frame):
            def __init__(self, parent=None, id=-1):
                wx.Frame.__init__(self, None, id, '更改密码', size=(250, 200), pos=(860, 400))
                wx.Frame.SetMinSize(self, (250, 200))
                wx.Frame.SetMaxSize(self, (250, 200))

                # 画板
                pnl = wx.Panel(self)

                # 控件
                tip_pPwd = wx.StaticText(pnl, label='请输入原密码：', pos=(40, 20))
                self.input_pPwd = wx.TextCtrl(pnl, style=wx.TE_LEFT, pos=(40, 50))
                tip_nPwd = wx.StaticText(pnl, label='请输入新密码：', pos=(40, 85))
                self.input_nPwd = wx.TextCtrl(pnl, style=wx.TE_LEFT | wx.TE_PASSWORD | wx.TE_PROCESS_ENTER, pos=(40, 107))
                bt_enter = wx.Button(pnl, label='确\n定', pos=(180, 20), size=(25, 56))
                bt_cancel = wx.Button(pnl, label='取\n消', pos=(180, 85), size=(25, 56))
                # 事件
                self.input_nPwd.Bind(wx.EVT_TEXT_ENTER, self.run_update)
                bt_enter.Bind(wx.EVT_BUTTON, self.run_update)
                bt_cancel.Bind(wx.EVT_BUTTON, self.closeWindow)

                # 图标
                try:
                    open('Image/icon.ico', 'rb')
                except FileNotFoundError:
                    print("没有找到图标文件")
                    wx.MessageBox("没有找到图标文件", "请导入图标文件")
                else:
                    self.icon = wx.Icon(name="Image/icon.ico", type=wx.BITMAP_TYPE_ICO)
                    self.SetIcon(self.icon)

            def run_update(self, event):
                run = user_admin.admin_update_password(user, self.input_pPwd.GetValue(), user_admin.all_get_users_form(1), self.input_nPwd.GetValue())
                if run is False:
                    wx.MessageBox('原密码错误！'+str(run), '失败')
                    self.input_pPwd.SetValue('')
                elif run is True:
                    wx.MessageBox('修改成功！', '成功')
                    frame_updatePwd_window.Close()

            def closeWindow(self, event):
                frame_updatePwd_window.Close()

        app_updatePwd_window = wx.App()
        frame_updatePwd_window = update_pwd_window(parent=None, id=-1)
        frame_updatePwd_window.Show()
        app_updatePwd_window.MainLoop()

    # 注销用户, 辅助, 完成, GUI
    def run_bt_delete_user(self, event):
        class delete_user_window(wx.Frame):
            def __init__(self, parent=None, id=-1):
                wx.Frame.__init__(self, None, id, '注销', size=(230, 170), pos=(860, 400))
                wx.Frame.SetMaxSize(self, (230, 170))
                wx.Frame.SetMinSize(self, (230, 170))
                # 画板
                pnl = wx.Panel(self)

                # 控件
                tip_pwd = wx.StaticText(pnl, label='请输入当前账号的密码:', pos=(45, 10))
                self.input_pwd = wx.TextCtrl(pnl, style=wx.TE_CENTER | wx.TE_PROCESS_ENTER, pos=(50, 30))
                bt_delete = wx.Button(pnl, label='确认注销', pos=(67, 60))
                # 事件
                self.input_pwd.Bind(wx.EVT_TEXT_ENTER, self.delete)
                bt_delete.Bind(wx.EVT_BUTTON, self.delete)

                # 图标
                try:
                    open('Image/icon.ico', 'rb')
                except FileNotFoundError:
                    print("没有找到图标文件")
                    wx.MessageBox("没有找到图标文件", "请导入图标文件")
                else:
                    self.icon = wx.Icon(name="Image/icon.ico", type=wx.BITMAP_TYPE_ICO)
                    self.SetIcon(self.icon)

            def delete(self, event):
                primary_form = user_admin.all_get_users_form(1)
                primary_user = user
                primary_pwd = pwd

                # 如果密码不匹配
                if self.input_pwd.GetValue() != primary_pwd:
                    wx.MessageBox('密码错误', '失败')

                else:
                    run = user_admin.admin_delete_users(user_to_deleted=primary_user, password=primary_pwd, users_form=primary_form)
                    import sys
                    sys.exit()

        app_delete_user_window = wx.App()
        frame_delete_user_window = delete_user_window(parent=None, id=-1)
        frame_delete_user_window.Show()
        app_delete_user_window.MainLoop()

    # 切换用户, 辅助, 完成, 引用GUI
    @staticmethod
    def run_bt_change_sign_user(event):
        frame_main.Close()
        global app, frame_sign
        app = wx.App()
        frame_sign = sign_window(parent=None, id=-1, debug_mode=False)
        frame_sign.Show()
        app.MainLoop()


if __name__ == '__main__':
    app = wx.App()
    frame_sign = sign_window(parent=None, id=-1, debug_mode=False)
    frame_sign.Show()
    app.MainLoop()

# 结束时间 2021.9.22 20:32

# 终于写完了, 19天啊

# 正式结束开发时间 2021.10.11 22:34
# 项目总耗时 37天
# 项目总行数 1917行
# 项目总体积 68.5 KB (70,244 字节)
