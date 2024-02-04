# If we write method in the both class, parent and child class then the parent class method's 
# is not accessible,in this case only child class is accessible to the child class which means child class replacing parant clss

'''class parant:
    def result(self,a,b):
        return a+b
class child(parant):
    def result(self,a,b):
        return a*b  
ob=child()
print(ob.result(5,6))  


# SUPER. METHOD(super(). method is used to call parent class's cuntructor  or method from the child class)
class parant:
    def result(self,a,b):
        return a+b
class child(parant):
    def result(self,a,b):
        super().result(10, 30)
        return a*b  
ob=child()
print(ob.result(5,6)) ''' 


#
'''class Train:
    # def __init__(self,name,fare,seats):
    #     self.name=name
    #     self.fare=fare
    #     self.seats=seats
        
    def get_status(self,name,seats):
        print(f"The name of the train is=",name)
        print(f"The availabel tiket in the train:",seats)
        print("************")
        
    def fare_info(self,fare):
        print(f"The price of the tiket is:",fare)
        
    def Book(self,seat):
        if (seat>0):
            print(f"your tiket has been book, your seat no is :",seat)
        else:
            print(f"This train has been full plrase try next time")
            
    def cancel_tiket(self,seatno):
        pass
                
class Tiket(Train):
    def get_status(self,name,seats):
        #super().get_status("Intersity",2000)
        print(f"The name of the train is:",name)
        print(f"The availabel seat in the train:",seats)
        print("************")
        
    def fare_info(self,fare):
        #super().fare_info(1500)
        print(f"The price of the tiket is:",fare)
                
    def Book(self,seat):
        #super().Book(30)
        
        if (seat>0):
            print(f"your tiket has been book, your seat no is :",seat)
        else:
            print(f"This train has been full plrase try next time")
        
    def cancel_tiket(self,seatno):
        pass

obj=Tiket() 
obj.get_status("Express",500)
obj.fare_info(1000)
obj.Book(100)'''    


class Train:
    def __init__(self,name,fare,seats,seat):
        self.name=name
        self.fare=fare
        self.seats=seats
        self.seat=seat
    def get_status(self):
        print(f"The name of the train is=",self.name)
        print(f"The availabel tiket in the train:",self.seats)
        print("************")
        
    def fare_info(self):
        print(f"The price of the tiket is:",self.fare)
        
    def Book(self):
        if (seat>0):
            print(f"your tiket has been book, your seat no is :",self.seat)
        else:
            print(f"This train has been full plrase try next time")
            
    def cancel_tiket(self,seatno):
        pass
                
class Tiket(Train):
    def __init__(self, name, fare, seats, seat):
        super().__init__("Intersity",2000,500,20)
        self.name=name
        self.fare=fare
        self.seats=seats
        self.seat=seat
        def get_status():
            #super().get_status()
            print(f"The name of the train is:",self.name)
            print(f"The availabel seat in the train:",self.seats)
            print("************")
        
        def fare_info(self):
            # super().fare_info(1500)
            print(f"The price of the tiket is:",self.fare)
                
        def Book(self):
            # super().Book(30)
        
            if (seat>0):
                print(f"your tiket has been book, your seat no is :",self.seat)
            else:
                print(f"This train has been full plrase try next time")
        
        def cancel_tiket(self,seatno):
            pass

obj=Tiket("Express",1000,500,100) 
obj.get_status()
obj.fare_info()
obj.Book()       
#obj.cancel_tiket()    










