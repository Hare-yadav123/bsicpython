from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass
            
class Child(Father):
    def disp1(self):
        print("this is a child class")
        print("Defining abtract Method") 
        print("************************") 
class Grandchild(Child):
    def disp2(self):
        print("this is a disp2 finction")
        print("Defining abtract Method" ) 

c = Grandchild()
c.disp1()
c.disp2()