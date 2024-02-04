# zip two list
# stu=['Raju','Haree','Vishanu'] 
# roll_no=[1,2,3]
# a=zip(stu,roll_no)
# mapp=set(a)
# print(mapp)

# zip enumarate
# stu=['Raju','Haree','Vishanu']
# roll_no=[1,2,3]
# for i in enumerate(zip(stu,roll_no)):
#     print(i)
l1=["hare","mera","sam"]
l2=[1,2,3]

print(set(zip(l1,l2)))
for i in enumerate(zip(l1,l2)):
    print(i)

# stu=['Raju','Haree','Vishanu']
# roll_no=[1,2,3]
# age=[20,22,25]
# mapped=zip(stu,roll_no,age)
# nap=list(mapped)
# print(nap)
# #unzipped 
# stuz,roll_noz,agez =zip(*nap)
# print(f"stdent name  {stuz} \n  stdent roll :{roll_noz} \n stdent age {agez}",end='')
# print(stuz)
# print("stdent roll \n",end='')
# print(roll_noz)
# print("stdent age \n",end='')
# print(agez)

players=["sachin","shikhar","pandya","rahul","dhonee"]
scored=[200,100,50,300,150]
for pl, sc in zip(players,scored):
    print(f'player:{pl} : score :{sc}')  
    
# #python program map two list into dictionary
# n=int(input("Enter your no of key:"))
# keys=[]
# values=[]
# for i in range(n):
#     elmt=input("Enter your no of elmt:")
#     keys.append(elmt)
# for i in range(n):
#     elmt=int(input("Enter your no of elmt:"))
#     values.append(elmt)
    
# d=dict(zip(keys,values))
# print(d)

# #python program create  map two list in dictionary
# # key=('name','saran','man
# # l=('haree','kumar','what')
# # print(dict(zip(key,l)))


# dic={2:1,5:2,8:6,4:0}
# for key in sorted(dic):
#     print(key,dic[key])

# # write python program get max and min value from dictionary  
# d1={2:1,5:2,8:6,4:0}
# m=max(d1.keys())
# n=min(d1.keys())   
# print("minimum",n) 
# print(m)

# # write python program remove duplicate item from dictionary
# d2={'id1':
#     {'name':'sar',
#      'class':'v',
#      'subject':'Hindi, English,Math'    
#     },
       
#     'id2':
#         {'name':'sar',
#      'class':'v',
#      'subject':'Hindi, English,Math'
#     },
#     'id3':
#         {'name':'sar',
#      'class':'v',
#      'subject':'Hindi, English,Math'
#     },    
# }
# result={}
# for key , value in d2.items():
#     print(key)
#     if value not in  result.values():
#         result[key]=value


# ...
# # print(result)

# # write python program adding value in same key
# from collections import Counter
# d3={"a":400,"b":200,"c":100}
# d4={"a":500,"b":800,"c":900}
# d5=Counter(d3)+Counter(d4)
# print(d5)


al=(10,2,3,4,1,4,5,5,7)
s=sorted(al)
t=tuple(s)
e=''
