# tuple is aslo bultin data types in the python or collection of both data or homogenius data
# it is unmutable but it is orderd and allow duplicate items

#example of orderd items
tpl1=('mango',45,'apple',25.5,'Ram') 
print(tpl1)

#example of not changeble items 
# tpl1=('mango',45,'apple',25.5,'Ram') 
# tpl1[1]='Haree'
# print(tpl1)


#example of get lenth of tuple
tpl1=('mango',45,'apple',25.5,'Ram') 
l=len(tpl1)
print(l)

#example of join two tuple using + operater
tpl1=('mango',45,'apple',25.5,'Ram') 
tpl2=('pen','book','ink')
tpl3=tpl1+tpl2
print(tpl3)

#example of count method a perticuler items tuple
tpl1=('mango',45,'apple',25.5,'Ram',45,45,45) 
c=tpl1.count(45) # we can  get lenth of perticuler items
print(c)


#example of index method 
tpl1=('mango',45,'apple',25.5,'Ram',45,45) 
i=tpl1.index(45) # usin items name find out items index number
print(i)

#copy methiod not applicable
# tpl1=('mango',45,'apple',25.5,'Ram',45,45) 
# i=tpl1.copy 
print(i)


def haree():
    global x
    x='ramu'
    print(x)
    
haree()
print(x)


