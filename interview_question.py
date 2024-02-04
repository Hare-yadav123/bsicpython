# ANAGROM 
'''def Anagrom(w1,w2):
    if len(w1)==len(w2) and sorted(w1)==sorted(w1):
        print('it is anagrom ')
    else:
        print('it is not anagrom')
        
a=Anagrom('listen','silent')'''


# convert decimal number into binary num 
# dec_num=int(input('Enter your nium'))
# bin_num=0
# i=0
# while dec_num!=0:
#     r=dec_num/2
#     bin_num=bin_num+r*(10**i)
#     dec_num=dec_num/2
#     i=i+1
#     print('binary num',bin_num)

# a=[1,2,3,4]
# b=['x','y','z']
# c=a+b
# print(c)

# d=[10,12,10,20,60,70]
# v=[10,12,10,20,60,70]
# d.remove(60)
# v.pop(4)
# print(d)
# print(v)
  
  
# a=173
# s=0
# l=len(str(a))
# tem=a
# while tem!=0:
#     r=tem%10
#     s+=r**l
#     tem=tem//10
# if s==a:
#     print('armstrong')
# else:
#     print('not armstrong number')

# a=153
# s=0
# l=len(str(a))
# tem=a
# while tem!=0:
#     r=tem%10
#     s+=r**l
#     tem=tem//10
# if s==a:
#     print('armstrong')
# else:
#     print('not armstrong')
    

# import math
# class part:
#     def __init__(x,z):
#         self.x=x
#         self.z=z
#     def distance(self,other):
#         math.sqrt((self.x-other)**2 +(self.z-other)**2)
# p1=part(0,0)
# p2=part(2,4)
# print(p1.distance(p2))

# prime number
# import math
def prime_num(n):
    if n>1:
        for i in range(2,int(n/2)): # we can use sqrt(n)
            if n%i==0:
                print('this is not prime nu')
                break
        else:
            print('it is  prime number')

prime_num(19)
 
# p_num=int(input('numbr'))
# if p_num>0:
#     for i in range(2,p_num//2):
#         if p_num%i==0:
#             print('it is not primr')
#             break
#     else:
#         print('it is prime num')

# def armstrong_num(n):
#     temt=n
#     sum=0
#     l=len(str(n))
#     while temt!=0:
#         digit=temt%10
#         sum+=digit**l
#         temt=temt//10
#     if sum==n:
#         print('it is armstrong')
#     else:
#         print('it not armtrong')
# armstrong_num(153)

#fibonic number 
# a=0
# b=1
# for i in range(7): 
#     c=a
#     a=b
#     b=a+c
#     print(c)
    
# #fectorials number
# result=1
# for i in range(5,0,-1):
#     result=result*i
# print(result)

# #perfect Number
# n=10
# c=0
# v=n
# for i in range(1,int(v/2)):
#     c+=i
# if n==c:
#     print('perfect number')
# else:
#     print('not perfect number')
    
# lcm 
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
    

#PALIDROME NUMBER 
'''a=int(input('enter your number:'))
b=a
s=0
while b!=0:
    r=b%10
    s=s*10+r
    b=b//10
if a==s:
    print('palidrome number')
else:
    print('not palidrome number')'''
    
    
# sum of the digit
# a=int(input('enter your number'))
# s=0
# while a!=0:
#     r=a%10
#     s+=r
#     a=a//10
# print('sum of digit:',s)

# ANAGRAM WORD
# w1=input('enetryour word')
# w2=input('enter your word')

# if len(w1)==len(w2) and sorted(w1)==sorted(w2):
#     print('it is anangram word')
# else:
#     print('not anagrame')