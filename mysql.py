# encoding: utf-8
#!/usr/bin/python

import MySQLdb


# 打开数据库连接
db = MySQLdb.connect("localhost","root","123456","chen" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

#-----------查看数据库版本
# 使用execute方法执行SQL语句
#cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据库。
#data = cursor.fetchone()
#print "Database version : %s " % data


#--------------创建表---------------
# 如果数据表已经存在使用 execute() 方法删除表。
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 创建数据表SQL语句
#sql = """CREATE TABLE EMPLOYEE (
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,  
#         SEX CHAR(1),
#         INCOME FLOAT )"""
#cursor.execute(sql)
#print 'Create Success'



#-------------插入数据------------
# SQL 插入语句
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, SEX, INCOME)
#         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
##sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
##       LAST_NAME, AGE, SEX, INCOME) \
##       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
##       ('Windows', 'chico', 21, 'M', 4000)	   
###例
###user_id = "test123"
###password = "password"
###con.execute('insert into Login values("%s", "%s")' % \
###             (user_id, password))
#try:
   # 执行sql语句
#   cursor.execute(sql)
   # 提交到数据库执行
#   db.commit()
#except:
   # Rollback in case there is any error
#   db.rollback()
#print 'Insert Success'


#--------------查询-------------
# SQL 查询语句
#sql = "SELECT * FROM EMPLOYEE \
#       WHERE INCOME > '%d'" % (1000)
#try:
   # 执行SQL语句
#   cursor.execute(sql)
   # 获取所有记录列表
#   results = cursor.fetchall()
#   for row in results:
#      fname = row[0]
#      lname = row[1]
#      age = row[2]
#      sex = row[3]
#      income = row[4]
      # 打印结果
#      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#             (fname, lname, age, sex, income )
#except:
#   print "Error: unable to fecth data"


#------------更新------------
# SQL 更新语句
#sql = "UPDATE EMPLOYEE SET AGE = 30 WHERE FIRST_NAME = '%s'" % ('Mac')
#try:
   # 执行SQL语句
#   cursor.execute(sql)
   # 提交到数据库执行
#   db.commit()
#except:
   # 发生错误时回滚
#   db.rollback()
#print 'Update Success'


#--------------删除-----------
# SQL删除记录语句
sql = "DELETE FROM EMPLOYEE WHERE AGE = '%d'" % (30)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 向数据库提交
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
print 'Delete Success'

# 关闭数据库连接
db.close()