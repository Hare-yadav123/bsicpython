# digit=123566
# sum=0
# while digit>0:
#     r=digit%10
#     sum=sum+r
#     digit=digit//10
#     print(sum)
d=121
sum=0
a=d
# while d>0:
#     r=d%10
#     sum=sum+r 
#     d=d//10
#     print(sum,'sum digit')
    
#     #pqllindron number
while d>0:
    r=d%10
    sum=(sum*10)+r
    d=d//10
    if sum==a:
        print('palidrom number')
    else:
        print('not pallindrom number')
    
    
# d=121
# s=0
# a=d
# while d>0:
#     r=d%10
#     s=(s*10)+r
#     d=d//10
#     if s==a:
#         print('palindrone numner',s)
#     else:
#         print('not palliondron number',s)
        
# #armstrong number
# n=371
# c=n
# l=len(str(n))
# s=0
# while n>0:
#     r=n%10
#     s=s+(r**l)
#     n=n//10
#     if c==s:
#         print('armstrong:',s)
#     else:
#         print('not armstrong:',s)
        
# #table of number

# num=int(input('enter your number'))
# z=10
# for i in range(1,z+1):
#     print(f'{num}*{i}:{num*i}')
    
# #odd number
# num=int(input('enter your number'))
# for i in range(2,(num//2)+1 ):
#     if i%2==0:
#         print('not ')
#     else:
#         i%2!=0
#         print('it is odd number',i)