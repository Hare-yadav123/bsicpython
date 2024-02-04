a=20
b=0
for i in range(1,a):
    if i%2==0:
        b+=i
print(b)
        
        
a=20
b=0
c=0
for i in range(1,a):
    if i%2==0:
        b+=b
    elif i%2 !=0: 
        c+=i
print(c)


# v=0
# while v<=50:
#     v+=2
#     print(v)
#     #v+=2

# sum of digit
n=int(input("Enter your digit"))
s=0
while n !=0:
    r=(n %10)
    s=s+r
    n=n//10
print(s)
    
def sum(n):
    s=0
    while n!=0:
        s=s+n%10
        n=n//10
    return s
n=int(input("Enter your digit"))
a=sum(n)
print(a)
        
        
an=int(input("Enter your digit"))
x=0
t=an
while an !=0:
    r=an%10
    x=x+(r*r*r)
    an=an//10
if t==x:
    print('armstrong number')
else:
    print('it is not armstron')

#palidrome number
an=int(input("Enter your digit"))
x=0
t=an
while an !=0:
    r=an%10
    x=x*10+r
    an=an//10
if t==x:
    print('palidrom number')
else:
    print('it is not palo')
