#create sqlite3 version
'''import sqlite3
try:
    conn=sqlite3.connect("temfile.db")
    print("database create and connect with sqlite3")
    print(sqlite3.sqlite_version)
except :
    print('OperationalError handle')
conn.close()'''


#create sqlite database programm  whiuch resides in the memory  python
"""import sqlite3
from sqlite3 import Error as Err
def SQlite_connection():
    try:
        conn=sqlite3.connect("temfile.db")
        conn=sqlite3.connect("memory")
        #cursor_ob=connection.cursor()
    except Err:
        print("Err")
    finally:
        conn.close()
SQlite_connection()'''
# write a python programm  to connect a database  and create a SQlite table
import sqlite3
from sqlite3 import Error
def sql_conn():
    try:
        conn=sqlite3.connect("mydatabase.db")
        return conn
    except Error:
        print("Error")
def sql_table(conn):
    try:
        conn.execute("CREATE TABLE  agent_Principle(agent_code char(6),agent_Name char(20),working_area char(30),commission decimal char(10,2),phone_no char(10), )")
        conn.execute()
        conn.commit()
    except:
        print(" no error")
    conn.close()
sql_co=sql_conn()
sql_table(sql_co)
inst(inst)"""
# if sql_conn:
#     sql_co.close()

import sqlite3
def inst():
    conn=sqlite3.connect("mydatabase.db")
    ins='''
            INSERT INTO agent_principle(agent_code chr(6),agent_Name chr(20),working_area chr(30),commission decimal chr(10,2),phone_no chr(10)) VALUES(20365,'RAMU ','MAINTAINENCE','CARE',3255655)
        '''
    conn.execute(ins)
    conn.commit()
    conn.close()
inst()







