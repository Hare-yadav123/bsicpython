# Encapsulation provide security hiding the data outside of the world
# encupsulation refers to  wrapping up(lapetna,sametna) of data under a single unit
# it is machinism that bind code and data that it manipulates


class car:
    handle="round"
    bark="dogy"
    def __init__(self,pet,milk):
        self._pet=pet
        self.__mammel=milk
        self.__show()
    def _show(self):
        print(self._pet) 
        print(self.__mammel)
        self.__private_method()  
    def __private_method(self):
        print('how ra u')
s=car("cow", "goat") 
print(car.bark)
print(car.handle)
s.show()