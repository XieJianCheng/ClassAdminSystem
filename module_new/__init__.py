import pymysql

# 连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456')
cursor = conn.cursor()

# 如果没有, 则创建
cursor.execute("create database if not exists `class_admin_system`")

sql_make_UserList = """
create table if not exists `class_admin_system`.`user_list`(
user varchar(20) not null,
pwd varchar(16) not null 
);
"""
cursor.execute(sql_make_UserList)

sql_make_StudentList = """
create table if not exists `class_admin_system`.`student_list`(
id int(3) not null,
name varchar(15) not null 
);
"""
cursor.execute(sql_make_StudentList)

sql_make_StudentInformation = """
create table if not exists `class_admin_system`.`student_info`(
id int(3) not null ,
name varchar(5) not null ,
age int(3) not null,
mation_1 varchar(30),
mation_2 varchar(30),
mation_3 varchar(30)
);
"""
cursor.execute(sql_make_StudentInformation)

sql_make_lesson = """
create table if not exists `class_admin_system`.`lesson`(
day int(1) unsigned not null ,
class_1 varchar(4) not null ,
class_2 varchar(4) not null ,
class_3 varchar(4) not null ,
class_4 varchar(4) not null ,
class_5 varchar(4) not null ,
class_6 varchar(4) not null ,
class_7 varchar(4) not null ,
class_8 varchar(4) not null 
)
"""
cursor.execute(sql_make_lesson)
cursor.execute("use class_admin_system")
cursor.execute("truncate lesson;")
sql_add_lesson = "insert into lesson values (%s,%s,%s,%s,%s,%s,%s,%s,%s) "
adding_list = [(1, '语文', '英语', '物理', '地理', '政治', '生物', '其他', '其他'),
               (2, '数学', '英语', '数学', '体育', '历史', '其他', '语文', '英语'),
               (3, '英语', '政治', '历史', '其他', '体育', '地理', '数学', '地理'),
               (4, '地理', '数学', '语文', '英语', '英语', '生物', '历史', '语文'),
               (5, '地理', '历史', '数学', '语文', '语文', '生物', '政治', '英语')
               ]
cursor.executemany(sql_add_lesson, adding_list)

cursor.close()
conn.commit()
conn.close()
