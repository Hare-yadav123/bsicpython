# positional argument

# def fuc1(*num1):
#     if num1%2==0:
#         print(f'this is a even number:{num1}')
#     else:
#         print(f'This is a odd number:{num1}')
        
# fuc1(20)

def even(num2): 
    if num2 % 2==0:
        return True
    else:
        return False
    
no=[4,5,8,12,9,6]
a=tuple(filter(even,no))
print(a)
  
# lambda func
lst=[4,5,8,20,30,9]  
ab=list(filter(lambda no:no%2==0,lst))
print(f'This is even number:{ab}')

#requared/position  

def position(num1,num2):
    sum=num1+num2
    print('sum of number{}'.format(sum))   
position(20,30)

def name(f1,l1):
    fn=f1+l1
    print('f name{} l name{}'.format(f1,l1,f1 + l1))
name('Raju','kumar')

#keyword argument

def keyword(n1,n2,n3,n4,n5):
    persentage=(n1+n2+n3+n5+n5)/5
    print('persentage of total number{}:'.format(persentage))
keyword(n1=70,n2=80,n3=75,n4=60,n5=50)

def myfunc(mes,nanu):
    print(' hi {} now days {}'.format(mes,nanu))
myfunc(mes=' raju ',nanu='How are u')


#default argumen

def defult(car='u drive car or not'):
    print(f'{car} ! yaa sure i can')
    
defult(car='i can drive the car')

#veriable lenth argument

def varlenth(*num):
    s=num[0]+num[1]+num[2]
    print(s)
    
varlenth(20,30,50)


# def sum(s,nu):
#     while nu>0:
#         r=nu%10
#         s=s+r
#         nu=nu//10
#     print(s)
# v=0
# n=int(input('Enetr your num'))
# sum(v,n)

 
def reverse(s,dig):
    e=dig
    while dig>0:
        r=dig%10
        s=(s*10)+r
        dig=dig//10
    if e==s:
        print(f'reverse is equal')
    else:
        print('not')
reverse(0,343)

#normal method
s=0
dig=121
av=dig
while dig>0:
    r=dig%10
    s=(s*10)+r
    dig=dig//10
if s==av:
    print(f'reverse is equal')
else:
    print('not')
    
#armstron
'''def armstrong(s,num):
    no=num
    le=len(str(num))
    while num>0:
        r=num%10
        s+=(s*10)+r**le
        num=num//10
    if s==no:
        print(f'palliondrom{s}')
    else:
        print('not')
armstrong(0,123)'''


# av=9
# if (av==1) or (av%2==0):
#     print('it is not prime')
# else:
#     print('it is prime')

def fun(n):
    if  n in [2,3]:
        return True
    if (n==1) or (n%2==0):
        return False
print(fun(9))

a=5
for i in range(2,a//2):
    if a%i==0:
        print('it is not prime num')
        break
else:
    print('itn is prime')