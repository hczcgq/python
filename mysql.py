# encoding: utf-8
#!/usr/bin/python

import MySQLdb


# �����ݿ�����
db = MySQLdb.connect("localhost","root","123456","chen" )

# ʹ��cursor()������ȡ�����α� 
cursor = db.cursor()

#-----------�鿴���ݿ�汾
# ʹ��execute����ִ��SQL���
#cursor.execute("SELECT VERSION()")
# ʹ�� fetchone() ������ȡһ�����ݿ⡣
#data = cursor.fetchone()
#print "Database version : %s " % data


#--------------������---------------
# ������ݱ��Ѿ�����ʹ�� execute() ����ɾ����
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# �������ݱ�SQL���
#sql = """CREATE TABLE EMPLOYEE (
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,  
#         SEX CHAR(1),
#         INCOME FLOAT )"""
#cursor.execute(sql)
#print 'Create Success'



#-------------��������------------
# SQL �������
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, SEX, INCOME)
#         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
##sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
##       LAST_NAME, AGE, SEX, INCOME) \
##       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
##       ('Windows', 'chico', 21, 'M', 4000)	   
###��
###user_id = "test123"
###password = "password"
###con.execute('insert into Login values("%s", "%s")' % \
###             (user_id, password))
#try:
   # ִ��sql���
#   cursor.execute(sql)
   # �ύ�����ݿ�ִ��
#   db.commit()
#except:
   # Rollback in case there is any error
#   db.rollback()
#print 'Insert Success'


#--------------��ѯ-------------
# SQL ��ѯ���
#sql = "SELECT * FROM EMPLOYEE \
#       WHERE INCOME > '%d'" % (1000)
#try:
   # ִ��SQL���
#   cursor.execute(sql)
   # ��ȡ���м�¼�б�
#   results = cursor.fetchall()
#   for row in results:
#      fname = row[0]
#      lname = row[1]
#      age = row[2]
#      sex = row[3]
#      income = row[4]
      # ��ӡ���
#      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#             (fname, lname, age, sex, income )
#except:
#   print "Error: unable to fecth data"


#------------����------------
# SQL �������
#sql = "UPDATE EMPLOYEE SET AGE = 30 WHERE FIRST_NAME = '%s'" % ('Mac')
#try:
   # ִ��SQL���
#   cursor.execute(sql)
   # �ύ�����ݿ�ִ��
#   db.commit()
#except:
   # ��������ʱ�ع�
#   db.rollback()
#print 'Update Success'


#--------------ɾ��-----------
# SQLɾ����¼���
sql = "DELETE FROM EMPLOYEE WHERE AGE = '%d'" % (30)
try:
   # ִ��SQL���
   cursor.execute(sql)
   # �����ݿ��ύ
   db.commit()
except:
   # ��������ʱ�ع�
   db.rollback()
print 'Delete Success'

# �ر����ݿ�����
db.close()