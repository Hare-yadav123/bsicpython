#import array as arr 
a=[1,2,3,4,5,6]
cars=['volvo','hundai','tata','fortuner','toyata']
print(a)
print(cars)

b=len(cars) 
print(b)
c=cars.pop(3)
print(c)
d=cars.remove('tata')
print(d)
e=cars.clear()
f=cars.reverse() 
print(f)
g=cars.append('mahindra')
print(g)

#syntex array 
# from array import* 
# cars=array.array( 'f',[2.5,6.2,8.4,7.1,9.2])
# print(cars)

from array import*
roll_stu=array('i',[101,102,103,104,105,106])
print(roll_stu[1])

# # Empty Array
# from array import*
# roll_stu=array('i',[])
# print(roll_stu)


#with index or for loop
# from array import*
# roll_stu=array('i',[101,102,103,104,105,106])
#print(roll_stu[2])# index by index
# n=len(roll_stu)
# for i in range(n):
#     print(i,"=",roll_stu[i])
 
 # used while loop   
# from  array import*
# cars=array( 'f',[2.5,6.2,8.4,7.1,9.2])
# c=len(cars)
# j=0
# while j<=c:
#     print(cars[j])
#     j +=1
    
#Array after append   
# from array import*
# roll_stu=array('i',[101,102,103,104,105,106])
# roll_stu.append(107,108)
# n=len(roll_stu)
# print(roll_stu[n])  

#count of frequency of number in array
'''from array import*
a=array("i",[4,9,9,5,5,5,5,51,6,8,])
count={}
for s in a:
    if s in count:
        count[s]+=1 
    else:
        count[s]=1
for key ,value in count.items():
    print(key,"=",value) 
#print(count)'''
    
# from array import*
# a=array("i",[4,9,9,5,5,5,5,51,6,8,])   
# v=len(a) 
# print(v)
# print(a)
# a.reverse()
# print("...reverse...")
# print(a)
# print("..append ..items") 
# a.append(220)
# print(a)
# print('pop method')
# a.pop(7)
# print(a)


#getting Array input from user ,using for loop
# from array import*
# a=array("i",[])
# n=int(input("Enter No of element"))
# for i in range(n):
#     b=int(input("Enter your element"))
#     a.append(b);
# for j in range(len(a)):
#     print(a[j])

import abc
print(c)












