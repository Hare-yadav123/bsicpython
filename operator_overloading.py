class add:
    def __init__(self,x):
        self.add=x
    def __add__(self,other):
        return self.x +other.x   
# class B():
#     def __init__(self,x):
#         self.x=x
        
a=add(100)
#v=B(10)
print(a.add)
#