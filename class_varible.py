#   class /static variable
# class variables are  the those varible whose single copy is available to all the instance of class
# if we modufy the copy variable in instance ,it wii effect all the copy in the other instance

# to access variable we need class method cls as first parameterthen we can access  class variable using cls.varible_name

'''class Mobile:
    r='god'  # class varible
    def __init__(self):
        self.model="realme11"
         
    def A(self):
        print(self.model)
        
    @classmethod
    def is_ram(cls):  
        cls.r
m=Mobile()
print(m.r)''' #cls.variable name(cls.r) and Mobile.variable name(Mobile.r)

# @classmethod
# class Mobile:
#     name="Haree"
#     @classmethod
#     def show(cls,t):
#         cls.time=t
#         print("we can see time in the",cls.time)
#         print(cls.name)
#         print("you are bestr friend")
        
# m=Mobile()
# m.show("watch")


# @staticmethod
'''class Mobile:
    name="Haree"
    @staticmethod
    def show(t,p):
        time=t
        price=p
        print("we can see time in the:*",time)
        print("there prise is:",price)
        print(Mobile.name)
        print("you are bestr friend")
        
m=Mobile()
m.show("watch",1000)'''


import math
import os
import random
import re
import sys
def hourglassSum(arr):
    currentMax = None
    for startArray in range(len(arr) - 2):
        for arrayPos in range(len(arr) - 2):
            newValue = arr[startArray][arrayPos] + arr[startArray][arrayPos +1] + arr[startArray][arrayPos + 2] \
                + arr[startArray + 1][arrayPos + 1] \
                + arr[startArray + 2][arrayPos] + arr[startArray + 2][arrayPos + 1] + arr[startArray + 2][arrayPos + 2]
            currentMax = newValue if currentMax is None or newValue > currentMax else currentMax
    print(currentMax)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
