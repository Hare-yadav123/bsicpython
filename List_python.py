#List is a collection of data which ordered and mutuble .in the list we can add duplicat items.
# in the list we can add homoginius types of data

#exam of empty list
# a=[]
# print(a)

#Example of append method
lst1=['mango',45,'apple',25.5,'Ram']
lst1.append(45)
print(lst1)

#Example of remove method
lst1=['mango',45,'apple',25.5,'Ram']
lst1.remove(45)# in this method remove the item use item name not index number
print(lst1)

#Example of pop method 
lst1=['mango',45,'apple',25.5,'Ram']
lst1.pop(2) # use index number we can remove the items
print('popmethod in list',lst1)

#Example of clear method
lst1=['mango',45,'apple',25.5,'Ram']
lst1.clear()
print(lst1)

#Example of mutable method
lst1=['mango',45,'apple',25.5,'Ram']
lst1[2]='Hree'
print(lst1)


#Example of reverse method
lst1=['mango',45,'apple',25.5,'Ram']
lst1.reverse()
print('reverse method',lst1)

#Example of insert method
lst1=['mango',45,'apple',25.5,'Ram']
lst1.insert(4, 'Raju')
print(lst1)

#Example of append method
lst1=['mango',45,'apple',25.5,'Ram']
lst2=[20,50,'sameer']
#lst1.append(lst2)
lst3=lst1+lst2
#print(lst1)
print(lst3)


#Example oh we can access value using index method
lst1=['mango',45,'apple',25.5,'Ram']

print(lst1[3])

#Example of len method
lst1=['mango',45,'apple',25.5,'Ram']
l=len(lst1)
print(l)

#Example of copy method
lst1=['mango',45,'apple',25.5,'Ram']
l=lst1.copy()
print(l)
print('*********************')

# Remove the quama in list 
ad=[2,5,9,8,7,20]
av=''
for i in ad:
    av=av+str(i)
    print(i)
print('Removed quama from list ad:',av)

abc='hello Raju '
an=abc.replace(' ', '')
print(an)

lst1=[[5,9,7],[2,3,4]]

com_list=[ j for i in lst1 for j in i]
print(com_list)



a=[50,602,30,90,70]
rv=''
for i in a:
    rv=rv+str(i)
    print(rv)
b='how  are u'
c=b.replace(' ','')
print(c)

av=[45,62,20,3]
a=av.pop(2)
print(a)


# a=10
# for i in range(2,a//2):
#     if a%2==0:
#         print('not prime')
#         break
# else:
#     print(' prime')

com_l=[f for f in range(0,10)]
print(com_l)

z=lambda x,y:x*y
print(z(5,5))

a=10
b=10
c=10
print(id(a))

print(id(b))
print(id(c))
print(type(a))
print(type(b))
print(type(c))

