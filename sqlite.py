'''
 1. SQL(structured  Query language) is a high performence language used to communicate with databases.
2. SQL is a programming language for storing and processing information in a relational databases .

3. Relatiopn database stores information in tabular form with rows nad columns representing different data attributes  and the various 
relationships the data value 

'''

# import sqlite3
# try:
#     con=sqlite3.connect("Raju.db")

#     con.execute('''
#             create table raju (
#                 st_id INT AUTO_INCREMENT PRIMARY KEY,
#                 st_name VARCHAR(50),
#                 st_class VARCHAR(30),
#                 st_email VARCHAR(20),
#                 st_phone 
#         )
            
#             ''')
# except:
#     print("exception handled")
# con.close()

#INCERT QUERY
# import sqlite3
# conn=sqlite3.connect("Raju.db")
# ins='''
#     insert into raju(st_name,st_class,st_email,st_phone) VALUEs('suman','9th','suman@452gamil.com',45669959)

# '''
# conn.execute(ins)
# conn.commit()
# conn.close()

#SELECT QUERY
# import sqlite3
# conn=sqlite3.connect("Raju.db")S
# data=conn.execute("SELECT * FROM raju  limit 0,1")
# print("student id","st_name","stu_class","st_email")
# for n in enumerate(data):
#     print(n)
    
#DELATE QUERY
# import sqlite3
# conn=sqlite3.connect("Raju.db")
# st_name=input("Enter student_name :-")
# conn.execute("DELETE FROM raju where st_name="+'st_name')
# conn.commit()
# conn.close()

#UPDATE QUERY

# import sqlite3
# conn=sqlite3.connect('Raju.db')
# conn.execute('''
#              update raju  set st_name='hareram',st_phone=6299816012 where st_name='Raj'
#              ''')
# conn.commit()
# conn.close()
   
#Ex show Table data in Terminal
# import sqlite3
# conn=sqlite3.connect("Raju.db")
# data=conn.execute("select * from raju")
# for i in data:
#     print(i)
# conn=sqlite3.connect('Raju.db')
# data1=conn.execute('select * from  raju ')
# for j in data1:
#     print(j)

    
# print("***********")
# prd_company=input("enter your prd COMPany:-")
# prd_name=input("enter your prd naame:-")
# #select * from mobile where prd_company='"+ prd_company+"'
# #  and 
# # or 
# data=conn.execute("select * from mobile where prd_company like '%"+ prd_company+"%' and prd_name='%"+ prd_name+"%'")
# for i in data:
#     print(i)
# conn.commit()
# conn.close()  

#7 JOIN METHOD IN SQL (left and inner query)

# import sqlite3
# conn=sqlite3.connect("name.db")
# data=conn.execute("SELECT * FROM children as c inner join student as s on c.st_id=s.st_id")
# for i in data:
#     print(i)
# conn.close()


# import sqlite3
# con=sqlite3.connect("Project.db")
# ins='''
#     insert into Project(Employee_Name,Employee_Dprmt,Employee_project)VALUES("Raju kumar","Testing","BizzWebApplication")
# '''
# con.execute(ins)
# con.commit()
# con.close()

# data base and table created 

import sqlite3
# conn=sqlite3.connect('mydata.db')
# c=conn.cursor() # cursor has been created
# # type of data types in sqlite 
# # Null .INTEGER,REAL(FLOAT),TEXT,BLOB
# c.execute("""CREATE TABLE custormer(c_name text,c_lastName text , c_email text)""")
# conn.commit()
# conn.close()

# # insert values in table
# conn=sqlite3.connect('mydata.db')
# c=conn.cursor()
# c.execute( "INSERT INTO custormer VALUES('pushspa','Raj','puspa123@gamil.com')")
# conn.commit()
# conn.close()

## insert multiple values in table
# conn=sqlite3.connect('mydata.db')
# c=conn.cursor()
# many_customer=[('Mukesh','kumar','mukesh123@gmail.com'),('Alok','kumar','alok123@gmail.com'),('Rmesh','kumar','ramesh123@gmail.com')]
# c.executemany(" INSERT INTO custormer VALUES(?,?,?) " , many_customer)
# conn.commit()
# conn.close()

#4 How to fetchin sql data in python using fetch commnand

'''conn=sqlite3.connect('mydata.db')
c=conn.cursor()
many_customer=[('Mukesh','kumar','mukesh123@gmail.com'),('Alok','kumar','alok123@gmail.com'),('Rmesh','kumar','ramesh123@gmail.com')]
# c.executemany(" INSERT INTO custormer VALUES(?,?,?) " , many_customer)

c.execute("SELECT  rowid, * FROM custormer where like ='sa' ")
# print(c.fetchone())
# print(c.fetchmany())
# print(c.fetchall())
items=c.fetchall()
for item in items:
    print('PRIMARY KEY:' ,item[0])
    print('first name:' ,item[1])
    print('last name:',item[2])
    print('Email:' ,item[3])
conn.commit()
conn.close()'''

#update Quey 
# import sqlite3
# conn=sqlite3.connect('mydata.db')
# c=conn.cursor()
# c.execute("""" UPDATE custormer SET c_name= 'kashish' WHERE c_name='Alok ' """)
# conn.commit()
# conn.close()

#5 delete Query from table
# import sqlite3
# conn=sqlite3.connect('mydata.db')
# c=conn.cursor()
# c.execute(" DELETE FROM custormer WHERE c_name='Alok' ")
# conn.commit()
# conn.close()

#oeder by
# import sqlite3
# conn=sqlite3.connect('mydata.db')
# c=conn.cursor()
# c.execute("""" SELECT rowid, * FROM custormer ORDER_BY rowid DESC  """)
# items=c.fetchall()
# for item in items:
#     print('rowid:-' ,item[0])
#     print('first name:-' ,item[1])
#     print('last name:-' ,item[2])
#     print('email:-' ,item[3])
#     print('........................')
# conn.commit()
# conn.close()


#create a new string  s3 use s1 and s2 
# s1='welhi'
# s2='come'
# s3=s1[0:3]+s2[0:4]+s1[3:6]
# print(s3)