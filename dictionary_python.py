# A dictionary is collection which is orderd,but it  can changeble  and we cant add duplicate items. 
# dictionry contain items in key or value pairs, can't contain duplicate items

# dict={
#     'Name':'Haree',
#     'num':4525522,
#     'frt':'apple',
#     'class':'12th',   
# }
# print(dict)
# dict['num']=102030
# print(dict)
# print(dict.keys())
# print(dict.values())
# dict.update({'age':'apple','class':5})
# print(dict)
# az=len(dict)
# print(az)

# del dict
# print(dict)
#we can access value using keys name
# mobile={
#     'Name':'Haree',
#     'num':4525522,
#     'frt':'apple',
#     'class':'12th',    
# }
# x=mobile['num']
# print(x)


# #we can chanege the  value using key name
# dict={
#     'Name':'Haree',
#     'num':4525522,
#     'frt':'apple',
#     'class':'12th',
    
# }
# dict['num']=6299816012
# print(dict)

# #we want to get lenth of dict
# dict={
#     'Name':'Haree',
#     'num':4525522,
#     'frt':'apple',
#     'class':'12th',
    
# }
# a=len(dict)
# print(a)
# print(len(dict))


# #we can add new items in dct
# dict={
#     'Name':'Haree',
#     'num':4525522,
#     'frt':'apple',
#     'class':'12th',
    
# }
# dict['gender']='female'
# print(dict)


# #we remove and pop
# dict={
#     'Name':'Haree',
#     'num':4525522,
#     'frt':'apple',
#     'class':'12th',
    
# }
# dict.pop('frt')
# print('pop dict' ,dict)


# #we can delet value usinf del
# dict={
#     'Name':'Haree',
#     'num':4525522,
#     'frt':'apple',
#     'class':'12th',
    
# }
# del dict['frt']
# print(dict)

# # update method
# mydict={
#     'Queen':'Bihar',
#     'name':'maharani janaki'
# }

# dict={
#     'Name':'Haree',
#     'num':4525522,
#     'frt':'apple',
#     'class':'15th',
    
# }
# mydict.update(dict)
# print(mydict)

import pandas as pd    
az=pd.DataFrame([1,2,34,0],[4,7,8,])
print(az[2,3])
