#INSTANCE VARIABLE= instance variable are those variable whose seprate copy created in every object
#instance varialbes are defined and initialized using a constructor with self parameter
#Example
class Mobile:
    def __init__(self):
        self.mobile='Realme11'   # instance variable
         
    def show_modle(self):
        return self.mobile
redame=Mobile()#instance variable are those variable whose seprate copy created in every object
realme=Mobile()
lava=Mobile()
print(redame.mobile)
print(realme.mobile)
print(lava.mobile)

#  ACCESSING INSTANCE VARIABLE 
#  WITH INSTANCE METHOD( To access instsnce variable , we need instance method  with self  as first 
#  parameter then we can access intance variable with self.variable _name)  

class mobile:
    def __init__(self):
        self.mobile='Realme pro13'  # instance variable
         
    def show_modle(self): # instance method
        return self.mobile # accessin intance varible
    
# object always live's  outside of class    
m=mobile()
print(m.mobile)
print(m.show_modle())


'''
variable=variable is a name of memory location where use can stored different types of data or value
a=10,20

type()=it return the data type of given value
'''
# a=20
# print(type(a))
# b=True
# print(type(b))
# c=None
# print(type(c))



# class human:
#     name=None
#     age=None
#     def get_name(self):
#         print('enter your name')
#         self.name=input()
#     def get_age(self):
#         print('enter your age')
#         self.age=input()
#     def put_name(self):
#         print('Name:',self.name)
#     def put_age(self):
#         print('age',self.age)
        
# p=human()
# p.get_name()
# p.get_age()
# p.put_name()
# p.put_age()

# class fruit:
#     def __init__(self):
#         print('I am fruits')
# class Anumals(fruit):
#     def __init__(self):
#         super().__init__()
#         print(' i am a tiger')
# a=Anumals()

import numpy as np
# a=np.array([1,2,3])
# print(a)

# import numpy as np
# b=np.array([[1,2,3],[ 4,5,6]])
# print(b) 

# a=np.array([1,2,3])
# b=np.array([6,4,5])
# print(np.sum(a+b,axis=0))

# How can u find "N" largest value from thr numpy array
import numpy as np
x=np.array([12,43,2,100,54,5,68])
print(np.argsort(x))
print(x[np.argsort(x)[-3:][::-1]])

b=(4,20,100,50,60,80,2) # this method allow both list and tuple
print(sorted(b)[-3:][::-1])

#give example of the list datfrome and dict dataframe
'''import pandas as dp
l1=[1,2,5,6,9]
print(dp.DataFrame(l1))'''

import pandas as pd
l={'fruit_name':['mango','apple','banana']}
dat2=pd.DataFrame(l)
print(pd.DataFrame(l))


# Read csv file
# import pandas as pd 
# red=pd.read_csv('dat2')
