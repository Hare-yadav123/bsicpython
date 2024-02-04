# Python Lambda function  :-

                   # Lambda function is a anonymous function
                   # Lambda function can take any number of arguments ,but can only have one expression
                   # one time use in lambda function
        # syntax :- lambda arguments :expression
        
def square(n):
    result=n*n
    print(result)
square(5)
square(2)

# lambda argument : expression
s=lambda n:n*n
s(5)
s(4)


sum1=lambda a,b,c:a+b+c
sum1(55,99,44)
# 
def sum(a,b,c):
  x=a+b+c
  print(x)

sum(30,60,10)
sum(30,60,77)

#
def f3(x,y):
    if x>y:
      print("largest number")
    else:
      print("Not largest number")
f3(44,77)

#
def f4(x,y):
    if x>y:
      print("largest number",num1)
    else:
      print("Not largest number",num2)
num1=int(input("enter a number 1---->"))
num2=int(input("enter a number 2---->"))
f4(num1,num2)

#

a=lambda a,b:u if (a>b) else b
print(a(23,34))

#

def add1():
    a=5
    b=8
    print(a+b)
add1()

#
x=lambda s,q:s+q
x(10,20)
x(60,50)

#
def even(no):
  if no %2==0:
    return True
  else:
    return False
a=[5,2,4,11,13,2,4]
f=tuple(filter(even,a))
print(f)

#
def even(no):
  if no%2!=0:
    return True
  else:
    return False
e=[5,2,4,11,13,2,4]
a=list(filter(even,e))
print(a)

#

def even(number):                               #[5,10,15,20,25]
    if number %2==0:
        return True
    else:
        return False
l=[5,10,15,20,25,30]
b=tuple(filter(even,l))
print(b)

#
def even(number):                               #[5,10,15,20,25]
    if number %2!=0:
        return True
    else:
        return False
l=[5,10,15,20,25]
b=list(filter(even,l))
print(b)

#
# syntax is set of rules/protocal is called syntax
# filter(function,sequence)
# lambda a:a%2==0