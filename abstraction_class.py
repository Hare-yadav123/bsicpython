# The process by which data and function define and we can seen only essential data and uneccessary implementation are hiding is called absractuin
# we can't create object of the father class
# we used @abstacr method
'''from abc import ABC ,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    
    def show(self):      # concrete method
        print(" concrete method")
        
class child(Father):
    def disp(self):
        print("this is a child class")
        print("Defining abtract Method")       
c = child()
c.disp()
c.show()'''

from abc import ABC,abstractmethod
class Principle(ABC):
    @abstractmethod
    def subjct(self):
        pass
    def subp(self):
        print("You have to  handle all things")
        
class Teacher(Principle):
    def subjct(self):
        print("you have to tech hindi")
        
class Scit(Principle):
    def subjct(self):
        print("you have to teach science")
#p=Principle() #can't initiate class principle withw abstract method       
t=Teacher()
s=Scit()
t.subjct()
t.subp()
print()
s.subp()
s.subjct()
print(id(t))
print(id(s))


       














