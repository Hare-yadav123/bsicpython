#sum of first n prime number
a=10
s=0
i=3
for n in range(2,a+1):
    for i in range(2,n): 
        if n%i==0:
            i=n
            break
    if i is not n:
        s=s+n       
print(' the sum of first prime nummber \n',n)
            
#perfect number
'''num =int(input("Enter your number"))
result=0
for i in range(1,num):
    if num%i==0:
        result=result+i       
if result==num:
    print("perfect number")
else:
    print("not perfect number")
    
#fibonacci Number(0,1,1,2,3,5,8,13,21)
num=int(input("write no of fibanaci series"))
f=0
s=1
for i in range(num):
    print(f)
    a=f
    f=s
    s=a+s'''
    
#Find L.C.m

# def lcm(a,b):
#     if a>b:
#         grater=a
#     else:
#         grater=b
#         if grater%a==0 and grater%b==0:
#             lcm=grater
#         return lcm
# a=int(input("num1"))
# b=int(input("num2"))
# n=lcm(a, b)
#print(n)

#LCM AND HCF OR GCD
# a=int(input("num1:"))
# b=int(input("num2:"))

# if a>b:
#     s=a
# else:
#     s=b
# for i in range(1,s+1):
#     if a%i==0 and b%i==0:
#         hcf=i  
# lcm=(a*b)/hcf
# print(f'hcf is:{a}and {b}:',hcf)
# print(f'lcm is :{a} and {b}:',lcm)
      
# #LCLM USIN BY MATH MODUK=LE         
# import math       
# a=15
# b=20
# c=3
# d=8
# print(math.lcm(a,b,c,d))

#PALIDROM NUNBER
a=9
if a>1:
    for i in range(2,int(a/2)):
        if a%i==0:
            print('it is not prime')
else:
    print('prime num')
    