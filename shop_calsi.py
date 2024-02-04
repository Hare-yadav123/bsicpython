s=0
choice=0
print('1 for continoue')
while choice!='q':
    price=float(input("enter your number:"))
    s=s+price
    print("the current cost=",s)
    choice=input("enter a for continue and end for q")
    print("the total cost is =",s)