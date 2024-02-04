#When more than one method with same name is define in asme class ,it is know as method overloading
#in python if the method is written such that it can perform more then one task

class over_loading:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
            return s
        elif a!=None and b!=None:
            s=a*b
            return s
        else:
            return "at least put two number"
am=over_loading()
print(am.sum(20))

class calculator:
    def root(self,num=None,num1=None,num2=None):
        if num!=None and num1!=None and num2!=None:
            print(f"The value of number of square root=",num**2,"or",num1*3,"or",num2*3)
        elif num!=None and num1!=None :
            print(f"The value of root of given number is=",num**0.5,"and second=",num1**0.5)
        else:
            print(f"The value of cube is given number=",num**3)
            
obj=calculator()
obj.root(81)

class student:
    def result(self,amar=None,op=None,shayam=None):
        if (amar != None and op !=None and shayam !=None):
            print(f'amar got:{amar} \n op got :{op} \n shayam go:{shayam} ')
            
        elif (amar != None and op !=None ):
            print(f'amar got:{amar} \n op got :{op}')
        else:
            print(f'shayam got: {shayam}')
            
ob=student()
ob.result(400)