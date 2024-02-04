# n=int(input("enter! how many eows u wnat to print:"))
# for r in range(n):
#     for c in range(r+1):
#         print(c+1,end=' ')
#     print('\n')

# n=int(input("enter! how many eows u wnat to print:"))
# for i in range(n):#0,1,2,3,4,5
#     for j in range(i,-1,-1):
#         print(j+1,end=' ')
#     print('\n')

# n=int(input("enter! how many eows u wnat to print:"))
# for i in range(0,n):#0,1,2,3,4,5
#     for j in range(0,i+1):
#         print(n-i,end=' ')
#     print('\n')

# n=int(input("enter! how many eows u wnat to print:"))
# for i in range(n):
#     for j in range(i,-1,-1):
#         print(n-j,end=' ')
#     print('\n')


#right angle shape
# n=int(input("enter! how many eows u wnat to print:"))
# for i in range(n):#0,1,2,3,4,5
#     for j in range(n-i):
#         print('', end=' ')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print('\n')
# display reverce number pattern
# a=5
# for i in range(a):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print('\n')

#display desending order of number
'''a=5
for i in range(a,0,-1):   
    for j in range(0,i): 
        print(i,end=' ')   #'*'
    print('\n')'''
    
#double the number
# a=5
# for i in range(0,a):
#     for j in range(i,-1,-1):
#         print(2**j,end=' ')
#     print('\n')

#incring pattern
# a=5
# for i in range(a):
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print('\n')

# decrising pattern

# a=5
# for i in range(a):
#     for j in range(i,a):
#         print('*',end=' ')
#     print('\n')

# Right side tringle
# a=5
# for i in range(a):
#     for j in range(i,a):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')  
#     print('\n')

# left side tringle
# a=5
# for i in range(a):
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(i,a):
#         print(' ',end=' ')  
#     print('\n')

#hill pattern
# s=6
# for n in range(s):
#     for m in range(n,s):
#         print(' ',end=' ')
#     for m in range(0,n+1):
#         print('*',end=' ')
#     print('\n')
#   
# s=6
# for n in range(s):
#     for m in range(0,n+1):
#         print('*',end=' ')
#     for m in range(n,s):
#         print(' ',end=' ')
#     print('\n')
#
  
# hill    
'''s=6
for n in range(s):
    for m in range(n,s):
        print(' ',end=' ')
    for m in range(n):
        print('*',end=' ')
    for m in range(n+1):
        print('*',end=' ')
    print('\n')
    
s=6
for n in range(s):
    for m in range(n):
        print(' ',end=' ') 
    for m in range(n,s):
        print('*',end=' ')
    for m in range(n,s+1):
        print('*',end=' ')
    print('\n')
    

s=6
for n in range(s):
    for m in range(n,s):
        print('*',end=' ') 
    for m in range(n):
        print(' ',end=' ')
    for m in range(n,s):
        print('*',end=' ')
    print('\n')
    
    
r=5
for i in range(r,-1,-1):
    c=1
    for j in range(1,i):
        print(c,end=' ')
        c=c+1
        print('*',end=' ')
    print('\n')
   
a=65
for i in range(7):
    for j in range(i+1):
        print(chr(a),end=' ')
        a+=1
    print('\n')
    
    
a=65
for i in range(7):
    for j in range(i,7):
        print(' ',end=' ')
    for j in range(i+1):
        print(chr(a),end=' ')
        a+=1
    print('\n')
    
s='harendra'
g=''
for i in s:
    g+=i
    print(g,end=' ')'''


'''for row in range(7):
    for col in range(5):
        if ((col==0 or col== 4)and row !=0) or ((row==0 or row==3) and (col>0 and col<4)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()'''
    
    
'''for row in range(10):
    for col in range(8):
        if (col==0 )or (col==7 and( row!=0 and row!=4 and row !=9)) or ((row==0 or row==4 or row==9) and (col>0 and col<7)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()'''
    
for row in range(10):
    for col in range(8):
        if (col==0) or (( row==0 or row==4 or row==9)and (col>0 and col<7)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()