# python code to train pockmon
'''powers=[4,3,2,1]
maxi,mini=0,0
for power in powers:
    if mini==0 and maxi==0:
        mini,maxi=powers[0],powers[0]

        print(mini,maxi)
    else:
        mini=min(mini,power)
        maxi=max(maxi,power)
        print(mini,maxi) '''

'''a=int(input('enter number:'))

if a%2 !=0:
    print(' prime')

elif a==0 or a==1:
    print(' no prime ')'''

# fibonacci series    
'''m=int(input('enter number:'))
a=0
b=1
for i in range(m):
    print(a)
    c=a+b
    a=b
    b=c''' 
    
'''def fibonaci(n):
    if n<0:
        print('incprrect fibonacci no')
    elif n==0 :
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci( n-2)
print(fibonaci(10))
    
    
def feb(n) :
    a=0
    b=1
    if n<0:
        print('incorrect')
    elif n==0:
        return 0
    elif n==1:
        return b
    else:
        for i in range(1,10):
            c=a+b
            a=b
            b=c
        return b
    
print(feb(9))'''

'''a=[5,8,6,0,8,9,7,2]
a.sort()
print(a)

c=['haree','ram','Shayam','Raju','vishanu','karan']
c.sort()
print(c)


c=['haree','ram','Shayam','Raju','vishanu','karan']
c.sort(reverse=True)
print(c)


def my_fun(lst1):
    return lst1
lst1=['haree','ram','Shayam','Raju','vishanu','karan']

lst1.sort(key=len)
print(lst1)'''

# a=65
# for i in range(7,0,-1):
#     for j in range(i,7):
#         print('',end=' ')
#     for j in range(i):
#         print(chr(a),end='')
#         a+=1
#     print('\n')


# v=7
# for i in range(v,0,-1):
#     for j in range(i,v):
#         print('' , end=' ')
#     for j in range(i):
#         print(j ,end=' ')
#     for j in range(i+1):
#         print(j ,end=' ')
#     print('\n')

# m=5
# for i in range(m):
#     for j in range(i,m):
#         print('',end=' ' )
#     for j in range(i):
#         print(' *',end=' ')
#     print('\n')
    
'''for row in range(6):
    for col in range(5):
        if ((col==0 or col==4 ) and row !=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print('\n')'''
    
    
# s=5
# a=1
# for i in range(1,s):
#     a =a*i
# print(a)


'''for row in range(6):
    for col in range(5):
        if ((col==0 or col==3) and row !=0)or ((row==0 or row==3 or row ==5) and (col>0 and col<3)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
    
