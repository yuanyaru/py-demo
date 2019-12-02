# -*- encoding:utf-8 -*-

import sqlite3

# 连接到一个现有的数据库。如果数据库不存在，它就会被创建，最后将返回一个数据库对象
conn = sqlite3.connect('test.db')
print("Opened database successfully")

c = conn.cursor()
"""
# 创建表
c.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME            TEXT NOT NULL,
        AGE             INT NOT NULL,
        ADDRESS         CHAR(50) NOT NULL,
        SALARY          REAL);''')
print("Table created successful")
"""
"""
# INSERT 操作
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
"""
# SELECT 操作
cursor = c.execute("SELECT id, name, age, address, salary  from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("AGE = ", row[2])
   print("ADDRESS = ", row[3])
   print("SALARY = ", row[4], "\n")
print("Operation done successfully")
# conn.commit()
# print("Records created successfully")
conn.close()
