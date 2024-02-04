#E
# for row in range(7):
#     for col in range(6):
#         if (col==0) or ((row== 6 or row==3 or row==0)and (col>0 and col<5)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()
    
#L    
'''for row in range(7):
    for col in range(6):
        if (col==0) or ((row== 6)and (col>0 and col<5)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()

#f   
for row in range(7):
    for col in range(6):
        if (col==0) or ((row==0 or row==3) and (col>0 and col<5)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
#H   
for row in range(7):
    for col in range(6):
        if (col==0 or col==5) or ((row==3)and (col>0 and col<5)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()

#M   
for row in range(7):
    for col in range(7):
        if (col==0 or col==6) or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
    
#K    
for row in range(7):
    for col in range(5):
        if (col==0) or (row==1 and col==3) or (row==2 and col==2) or (row==3 and col==1) or (row==4 and col==1) or (row==5 and col==2) or (row==6 and col==3):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
#N   
for row in range(7):
    for col in range(7):
        if (col==0 or col==6) or ((row==col )and (col>0 and col<6)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
    
#Z    
for row in range(7):
    for col in range(6):
        if (row==0 or row==6) or ((row==1 and col==5 ) or(row==2 and col==4) or (row==3 and col==3)or (row==4 and col==2) or (row==5 and col==1) and (col>0 and col<6)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()'''


# for row in range(7):
#     for col in range(6):
#         if ((col==1 or col==4) and (row<2 or row >4))or((row==col and col>0 and col<5) or (col==3 and row==2) or(col==2 and row==4)):
#             print('*',end=' ')
#         else:
#             print(end='  ')
#     print()


for row in range(7) :
    for col in range(8):
        if (col==0 or col==5 or row==3 and(col>0 and col<3)):
            print('*',end=' ')
        else:
            print(end=' ')
    print(' ')