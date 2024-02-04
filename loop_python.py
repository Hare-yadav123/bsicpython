'''
LOOP IS IMPORTANT PROGRAMMING CONCEPT AND EXIST IN ALMOST EVERY PROGRAM. IT IS USED TO  REPEAT A PERTICULAR OPRATION(S) SEVERAL TIME UNYIL THE SPECIFUC CONDITION IS MET

'''
a=[20,50,60]
for i in a:
    print(a[::-1])
# example ATM MACHINE FOR TRANSACTION
#YOU PUT YOUR SONG ON REPEAT MODE
#MOBILE PASSWORD
#produsin output and searchuing  information

# for loop is a programming conditional itrative statement for used to cheak certain condition then repeatedaly excicute until that condition is met
# for loop=a for loop  used in python itrating over the sequence(list, tupkle dict, sect)
####use

''' WHILE LOOP=WHILE LOOP IS PROGRAMMING conditional itrative statement FOR USED TO EXICUTE  BLOCK OF  STSTIMEMT UNTIL THAT CONDITION IS TRUE
 IT IS ALSO CALLED INFINITY LOOP'''
# c=0
# while c <=10:
#     print(c)
#     c+=1

#Break statement= break statement terminate the itration of loop
# but continue statement terminate the current itration and again itrate the next statememnt


''''
(1)for key word is used but while key word is used
(2) Number of itration alrady known but No prior information on the number of itration
(3)range function used for itrate but while loop no function used
(4)for loop  can be itrate generator in python but while loop can not
(5)for loop is exicute fast compaire to while loop
(6) in for loop initialization is done staring but in while loop can be done anywhwre in loop body

'''
# Range function=The function return sequnce of numbers,starting from 0(by defult),incriment 1 value(by defult)
# and stop befor specifid number
'''
(1)python range function  dose not  support the floatpoint number  and non integer value like string

x=5
for i in range(0.5,0,0.5):
    print(i) # show typeerror can't be interpreted'''
    
# but we can exicute another way
def floarange(start,stop,step):
    j=start
    while j<stop:
        yield j
        j+=step
for k in floarange(0.4,0.8,0.1):
    print(k)
 #also we can add two range function through chain method
from itertools import chain

for l in chain(range(1,5),range(5,-1,-1)):
    print(l)
    
    
# we can access the value through index value
val=range(5)
print(val[0])
print(val[2])
print(val[3])
print(val[4])