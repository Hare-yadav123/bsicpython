'''import csv 
with open('student.csv','w')as csvfile:
    wrt=csv.writer(csvfile)
    for i in range(3):
        n=input('Enter Name')
        dob=input('Enter dob')
        slry=int(input('Enter salary'))
        wrt.writerow([n,dob,slry])'''

# import csv
# with open('student.csv','r')as csvfile:
#     rd=csv.reader(csvfile,)
#     #next(rd)
#     for row in rd:
#         print(row)

import csv
# with open('raju.csv','w')as csvfile:
#     wr=csv.writer(csvfile)
#     print(wr)
    
# with open('rahul.csv','w')as csvfile:
#     rm=csv.writer(csvfile)
#     for i in range(3):
#         name=input('Enter Name:')
#         age=int(input('Enter Age:'))
#         addr=input('enter add')
#         rm.writerow([name,age,addr])
        
        
with open('rahul.csv','r')as csvfile:
    rd=csv.reader(csvfile)
    for i in rd:
        print(i)