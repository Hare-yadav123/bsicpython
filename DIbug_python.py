# basic 3 type of Error:-(syntex error, Run time error , Logical Error)



import pdb
pdb.set_trace()  # pdn.set_trace() ,this code we can write any where inside the program we want
def Multiply(a,b):
    ans=a*b
    return ans
x=int(input("Enter your first number"))
y=int(input("Enter your second number"))  # c command use foe continoue your program
re=Multiply(x, y) # n  command use for goint to next line  
print(re)        # l command use cheak the code line by line 


