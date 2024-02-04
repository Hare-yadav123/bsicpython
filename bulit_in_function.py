# zip = ZIP() TAKES ITERABLE CONTAINERS(LIST,STRING) AND RETURN SINGLE ITREBLE OBJECT
'''
zip(*itrators)
parameters:python itrables(list,string)
return values
'''
# zip with set
'''name=['Raju','harendra','Neha','sonu']
roll_no=[2,3,4,5]
mapped=zip(name,roll_no)
print(set(mapped))'''

#zip with list

'''name=['Raju','harendra','Neha','sonu']
roll_no=[2,3,4,5]
mapped=zip(name,roll_no)
print(list(mapped))'''

#zip with dict
'''name=['Raju','harendra','Neha','sonu']
roll_no=[2,3,4,5]
mapped=zip(name,roll_no)
print(dict(mapped))'''


# name=['Raju','harendra','Neha','sonu']
# score=[200,300,400,500]
# for na,sc in zip(name,score):
#     print('name:',na,  ',' 'score:',sc)
    
    
# n=10
# s=0
# while True:
#     s+=n
#     n -=1
#     if n==0 :
#         break
# print(f" sum of the 10 number :{s} ")  
# exit() 

f='how  are you ram*'
h=f.replace(' ','' )
print('remove space:',h)

l=[5,8,3,6]
s=''
for i in l:
    s=s+str(i)
    print('remove quima:',s)
    
#sum of digit 
d=45701
s=0
while d!=0:
    r=d%10
    s=s+r
    d=d//10
    print(f'sum of digit:{s}')
    
#pali
    