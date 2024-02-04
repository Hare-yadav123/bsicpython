# Write python program Add key and value in dictionary
num=int(input("no of input"))
d={}
for i in range(num):
    key =input("Enter your key :")
    value =int(input("Enter your value:"))
    d.update({key:value})
    print("update dictionary is:",d) 

# # concatenate two dictionaryd1={"a":5,"B":10}
# d2={"C":15,"D":20}
# d1.update(d2)
# print(d1)

# # write python program given key exist in dictionary or nit
# # d1={"a":5,"B":10}
# # key=input("Enter key to check")
# # if key in d1.keys():
# #     print("key persent in dict:",d1[key])
# # else:
# #     print("key is not persent")
    
# #write program generate a dictionary that contain (1,n+1) in form of x:x*x
# n=int(input("enter number"))
# m={x:x*x for x in range(1,n+1)}
# print(m)

# # sum of all value in dict4

# d3={"a":50,"B":100,"c":300}
# s=sum(d3.values())
# print(s)


# # multiply dict value
# d4={"a":50,"B":100,"c":300}
# mul=1
# for i in d4:
#     print(i)
#     mul=mul*d4[i]
# print(mul)

# # python program remove key from dictionary
# d5={"a":50,"B":100,"c":300}
# print("original dict")
# print(d5)
# key=input(" which key u want to remove:")
# if key in d5:
#     del d5[key]
# else:
#     print("key not found")
#     exit(0)
# print("update dict ")
# print(d5)

# # python program  to from a dictionary to object of a class
# class H:
#     def __init__(self):
#         self.a=5
#         self.b=7
# ob=H()
# print(ob.__dict__)


# #write python program to print dictionary in table from
# my_dict={"c1":[1,2,3],"c2":[4,5,6],"c3":[7,8,9]}
# for row in my_dict:
#     print(my_dict[row])
    
# # write python program conver string to dictionary
# from collections import defaultdict,Counter
# str1='harendra '
# d1={}
# for i in str1:
#    d1[i]=d1.get(i,0)+1
# print(d1)

# # write python program count the value of key in dictionary
# dic={"id":1,"k":2,"g":5}
# sum=0
# for i in dic:
#     sum=sum+dic[i]
#     print(sum)
    
    
my_di={"c1":[1,2,3],"c2":[4,5,6],"c3":[7,8,9]}
for i,j in my_di.items():
    # a=my_di.sorted()
    print(i,':',j)