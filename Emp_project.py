# create table
import sqlite3
try:
    con=sqlite3.connect("data.db")

    con.execute('''
            create table practical(
                Emp_id INT AUTO_INCREMENT PRIMARY KEY,
                Emp_Name VARCHAR(20),
                Emp_Dprmt VARCHAR(30),
                Emp_Project VARCHAR(30)
                
        )
            ''')
except:
    print("exception handled")
con.close()

#inser data
import sqlite3
co=sqlite3.connect("data.db")
insr='''
    insert into practical(Emp_Name,Emp_dprmt,Emp_project) VALUES ('RAJU KUMAR','TESTING','BizzwebApp')
'''
co.execute(insr)
co.commit()
co.close()