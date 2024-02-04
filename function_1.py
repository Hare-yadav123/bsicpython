# -*- coding: utf-8 -*-



#(without function)
# 1.--------
# 2.--------
# 3.-------
# 500.-------   time wast

## Built in function ( ) :-

 # float ():-
n=89
print(float(n))

# int ( ):-
a=55.8
print(int(a))

# Id :-
a="python"
id(a)

# max( ):-
x=max(3,7,9,6,5)
print(x)

## Type of function

 # 1) Built in function ( )
  #2) user define function ( )

 # 1) Built in function :-  The function ( ) which are coming along with python software
                                             #      at automatically is called as built in function

                                  # inputz
                                  # int
                                  # length
                                  # list
                                  # max
                                  # min


   # 2) User define function ( ) :-
                                     # The function are developed by programmer explictiy according to
                                          #                    bussiness requirement are called user define function

#   user define function are  created using "def" keyword

# hello pooja your age is 29 =OUTPUT
# name=pooja
# age=29

# 5colour



# min ( ):-
x=min(2,7,9,6,7)
print(x)

# range ( ):-
x=range(1,12,5)
for i in x:
  print(i)

# zip ( ):-
a=("apple","kivi","orange","pink")
b=("red","green","yellow","kk")
c=("a","b","c","d")
x=zip(a,b,c)
print(tuple(x))

## User define function :-

def my_function(country = "Norway"):
    print("I am from " + country)


my_function("india")
my_function()

## User define function :-

def demo (country = "Norway"):
    print("I am from " + country)

demo( )
demo("india")



def raj(company="RB"):
    print("i am from "+ company)
raj()
raj("IBM")

def demo(fname, lname):
  print(fname + "  &   "+ lname)

demo("email", "Refsnes")

# With parameter

# def f2(a,b):
#   c=a+b
#   print(c)
# f2(10,10)
# f2(50,50)

def sum(a,b):
      return a*b
print(sum(5,5))

# Return Statement
# def f3(a,b):
#   d=a+b
#   s=a-b
#   m=a*b
#   p=a/b
#   return d,s,m,p

# d,s,m,p=f3(10,2)
# d,s,m,p=f3(5456,767)
# print('addition is',d)
# print('sub',s)
# print('multiply',m)
# print('division',p)

# def f3(a,b):
#     d=a+b
#     s=a-b
#     m=a*b
#     p=a/b
#     return d,s,m,p

# demo=f3(10,2)
# print(demo)
# print(type(demo))
# for i in demo:
#   print(i)

# # Type of variable
#  # 1) Requiment / positional Argument
#  # 2) keyword Arguments
#  # 3) Default Argument
#  # 4) veriable length Argument

# # Required / positional Argumant


# def marks(sub1,sub2,name):
#   avg=((sub1+sub2)/2)
#   print("Hello {} your marks score is {}".format(name,avg))

# marks(55,88,'sagar')

def av(a,b,c,d,name):
    mark=(a+b+c+d/2)
    print('hello {} my score is'.format(name,mark))
av(4,5,8,9,'raju')

# # def marks(sub1,sub2,name):
# #   avg=((sub1+sub2)/2)
# #   print("Hello {} your marks score is {}".format(name,avg))

# # marks('apurva',66,88)

# ## keyword Argument ##

# def marks(sub1,sub2,name):
#     avg=((sub1+sub2)/2)
#     print("Hello {} your marks score is {}".format(name,avg))

# marks(name='apurva',sub1=66,sub2=77)

# def marks(sub1,sub2,name):
#   avg=((sub1+sub2)/2)
#   print("Hello {} your marks score is {}".format(avg,name))

# marks(sub1=78,name='apurva',sub2=66)

# def marks(sub1,sub2,name):
#     avg=((sub1+sub2)/2)
#     print("Hello {} your marks score is {}".format(name,avg))

# marks(sub1=66,sub2=77,name='apurva')

# def marks(sub1,sub2,name):
#     avg=((sub1+sub2)/2)
#     print("Hello {} your marks score is {}".format(name,avg))

# marks(sub1=66,name='apurva',sub2=77)

# ##  Required and Keyword Argument  ##


# def marks(sub1,sub2,name):
#       avg=((sub1+sub2)/2)
#       print("Hello {} your marks score is {}".format(avg,name))

# marks(sub1=55,sub2=66,name='apurva')
# marks(sub1=5,name="pooja",sub2=66)
# marks(66,55,name="apurva")
# marks(name='apurva',sub1=55,sub2=66)

def num(s1,s2,s3,s4,nam):
      mark=(s1+s2+s3+s4/2)
      print('use of formate {} and score{}'.format(nam,mark))
num(s1=10,s2=20,s3=50,s4=30,nam='Haree')

# def marks(sub1,sub2,name):
#     avg=((sub1+sub2)/2)
#     print("Hello {} your marks score is {}".format(name,avg))

# marks(name='apurva',sub1=55,sub2=66)

# ##  Default Argument  ##
# def getting(name,msg="how are you"):
#   print(f"good morning {name},{msg}")

# getting("payal")

# getting("pooja","where are you")

# def gretting(name,msg='How are you'):
#     print(f"Good moring {msg},{name}")

# gretting("pooja","where are you")

# def gretting(name,msg='How are you'):
#     print(f"Good moring {msg},{name}")

# gretting("apurva","what is your name")
# gretting("apurva")

# def gretting(name,msg='How are you'):
#     print(f"Good moring {msg},{name}")


# gretting(name='pooja',msg="god bless you")

def defaul(name,msg='hey bro how are you'):
      print(f'hey bru{name} u get')
    
defaul('monu')

# ##  Variable Length Argument

# def subject(*marks):
#     a=marks[0]+marks[1]+marks[2]
#     print(a)

# subject(44,55,77)
# print( )
# subject(77,435,954,456,4455)

# ##  Variable Length Argument

# def subject(*marks):
#     all1=marks[0]+marks[1]+marks[2]+marks[3]+marks[4]
#     print(all1)

# subject(44,55,77,99,667)

# ### variable length Keyword arguement ###

# def subject(*marks):
#     sum1=marks[0]+marks[1]+marks[2]+marks[3]
#     print(sum1)
# subject(55,88,99,33,40)

def var(*num):
      su=num[0]+num[1]+num[3]+num[4]
      
      print(f'varieble lenth argument{su}')
      
var(12,30,40,50,70)

ac=[20,50,40,2,3]
ac.clear()
print(ac)