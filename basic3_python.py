# write python program to access and print a URLs content to the console
# from http.client import HTTPConnection
# conn=HTTPConnection("example.com")
# conn.request("GET", "https://www.w3resource.com")
# result=conn.getresponse()
# cont=result.read()
# print(cont)

# import requests
# data=requests.get("https://drive.google.com/file/d/1rpEhCVSytq_AXAiLsXenmrgEAEJOllFC/view")
# print(data.text)

#write the python program get the name of the host on which the routine is running
import socket
host_name=socket.gethostname()
print()
print("host name",host_name)
print()


# write python program to clear screen or terminal
import os
import time
# for window 
#os.system("cls")
os.system("is") 
time.sleep(2)
os.system("clear")


import datetime, time
print(time.ctime())

#
import traceback
def f1(): return abc()
def abc():traceback.print_stack()
a=f1()
# s=abc() 
print(a)
# print(s)

def test(one ,*two):
    print(type(two))
test(1,2,3,4)

def mest(n):
    if n<2:
        return n %2==0
    return mest(n-2)
print(mest(23))

# python program conver byte code string to list
a=b'Abcf'
print(list(a))
print(id(a))

# write puthon program get object identity
obs=object()
print(id(obs))

c=20
d=30
print(" befor swap  a=  %d and b = %d" %(c,d))
c,d=d,c
print(" \n after swap  c =  %d and d = %d"%(c,d))
print("%d+%d=%d"%(c,d,c+d))

# write python program get size of the file

# with open("text.text",'a')as f:
#     file=f.write(" how are you")
#     print(file)
    
import os
size=os.path.getsize("text.text")
print(size)

number=[]
om=1000
print(str(om).zfill(3))

