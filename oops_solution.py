'''import numpy as np
ndarray=np.array([1,4,5,8,9,9])
print(ndarray)


func=lambda x,y:(x**y)
print(func(float(10),20))

class A():
    def __init__(self,a):
        self.num=a
    def mul_two(self):
        self.num *=2
class B(A):
    def __init__(self, a):
       super().__init__(a)
    def mul_three(self):
        self.num *=3
obs=B(4)
print(obs.num)
obs.mul_two()
print(obs.num)
obs.mul_three()
print(obs.num)


class Human():
    def __init__(self,name):
        self.Name=name
        
    def get_name(self):
        return self.Name
    def isEmployee(self):
        return False

class Employee(Human):
    def __init__(self, name,id):
        super().__init__(name)
        self.Emp_id=id
    def get_id(self):
        return self.Emp_id
    def isEmployee(self):
        return True
obj=Employee('Raju', 20035)
print(obj.get_name(),obj.get_id(),obj.isEmployee())

class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        
first_name='LMN'
obj=Person('JKL', 'ABC')
obj.last_name='PQR'
print(obj.first_name)
print(obj.last_name)

main_dict={}
def insert_i(item):
    if item in main_dict:
        main_dict[item] +=1
    else:
        main_dict[item]=1
#Driver code       
insert_i("key1")
insert_i("key2")
insert_i("key3")
insert_i("key1")
insert_i("key5")
insert_i("key1")
print(len(main_dict))


class X:
    def __init__(self):
        self.__x=1
        self.y=5
    def Display(self):
        print(self.__x,self.y)
class Z(X):
    def __init__(self):
        super().__init__()
        self.__x=7
        self.y=8
ab=Z()
ab.Display()'''

# creat a program in which bothe break and continou statement are used
'''a=[1,2,3,4,5,6,7,8,9,0]
for i in a:
    pass
    if i==0:
        same=i
        break
    elif i%2==0:
        continue
    print("i:",i)
print("same=",same)'''
        
# explain how to remove file in python
import os
# os.remove('memory.csv2')
# print("file remove")


cwd=os.getcwd()
print("curent working directry",cwd)
# get the list of all files and directry in root directry
path='/'
dir_path=os.listdir(path)
print("file and directry'",path,"' :")
print(dir_path)