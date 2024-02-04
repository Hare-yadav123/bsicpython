# for i in range(65,91):
#     for j in range(65,i+1):
#         print(chr(j),end=' ')
#     print("\n")
# for i in range(0,7):
#     for j in range(-i,0):
#         print(j,end='')
#     print('\n')

# ascci=65  
# for i in range(0,5):
#     for j in range(0,i+1):
#         print(chr(ascci),end=' ')
#     ascci+=1
#     print("\n")

# a='python'
# x=''
# for i in a:
#     x+=i
#     print(x)
    
# a=int(input('enter nu u wnt to print'))
# for i in range(-a,0):
#     for j in range(i,0):
#         print('*',end=' ')
#     print('\n')
    
# ascci=97
# for i in range(97,122):
#     for j in range(97,i+1):
#         print(chr(j),end='')
#     ascci=+97
#     print('\n')

#right side increse   
# ascci=65  
# for i in range(0,6):
#     for j in range(0,i+1):
#         print(chr(ascci),end=' ')
#     ascci+=1
#     print("\n")




#right angle  tringle pattern
# ascci=65  
# for i in range(1,6):
#     for j in range(6-i,-1):
#         print(' ',end='')
#     for j in range(1,i+1):
#         print(chr(ascci),end=' ')
#     ascci+=1
#     print("\n")

ascci=65
for i in range(1,10):
    for j in range(10-i,-1):
        print(' ',end=' ')
    for j in  range(1,i+1):
        print(chr(ascci),end=' ')
    ascci +=1
    print('\n')
    
    
    
# ascci=65  
# for i in range(6):
#     for j in range(6-i-1):
#         print(' ',end='')
#     for j in range(i,-1,-1):
#         print(chr(ascci),end=' ')
#         ascci+=1
#     print("\n")