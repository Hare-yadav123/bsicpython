print("which calculation want to you do")
print("addtion for :1")
print("subtraction for :2")
print("multiplication for :3")
print("divition for :4")

choise=int(input("enter your choise:"))

if choise==1:
    num1=int(input("enter first no"))
    num2=int(input("enter second no"))

    print("addtion of number=",num1+num2)

elif choise==2:
    num1=int(input("enter first no"))
    num2=int(input("enter second no"))

    print("subtration of number=",num1-num2)
    
elif choise==3:
    num1=int(input("enter first no"))
    num2=int(input("enter second no"))

    print("addtion of number=",num1*num2)

elif choise==4:
    num1=int(input("enter first no"))
    num2=int(input("enter second no"))

    print("addtion of number=",num1/num2)
    
else:
    print("press exit for 5") 
    
# import keyword
# print(keyword.kwlist)