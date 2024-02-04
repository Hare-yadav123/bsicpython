class student:
    def __init__(self,name,roll,address):
        self.n=name
        self.r=roll
        self.a=address
        
    def disp(self):
        print(f"name : {self.n},Roll: {self.r},Address: {self.a}")