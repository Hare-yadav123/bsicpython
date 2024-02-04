#python copy method return shallow copy of list
# shallow copy means : a new list can't reflected original list after modification
'''list.copy() syntax
The copy methiod does not take any paramerter
'''
#list.copy example
lst1=[4,5,6,'Ramu','Aama']
lst2=lst1.copy()
print('create new lst2:',lst2)
lst2.append(8)
print('after copy and modification new list',lst2)
print("***********************************")

print('original or old list1=',lst1)

#Deep copy in python
import copy
lst4=[7,8,90,[11,14,15],200,300]
print("lst4=",lst4)
lst5=copy.deepcopy(lst4)
lst5[2]=18
print("after copy.deepcopy=",lst5)

# shallow copy means if we change the new list then reflected original list
lst6=[70,80,90,50]
print('original list6: ',lst6)
lst7=copy.copy(lst6)
lst7.append(100)
print("****************")
print('new list7:',lst7)