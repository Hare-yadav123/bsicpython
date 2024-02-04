# 1. Write a program to print the reverse of the given string.
# a='codecode'
# b=a[::-1]
# print(b)
a='codecode'
def myfunc(a):
    return a[::-1]
print('original string:')
print(myfunc('codecode'))
print('-------**********--------')

# 2 Given a number, check whether it is a prime number or not.

num=int(input('Enter your number:'))
if num>1:
    for i in range(2,int(num/2)+1):
        if num%i==0:
            print(num ,'it is not prime')
            break
    else:
        print(num,':it is prime ')
print('-------**********--------')
        
# 3. Given an array of numbers, arrange them in a way that it forms the largest value.      
a=[54, 546, 548, 60]
a.sort()
a.reverse()
print('Original number is:')
print('Arrange according to largest number:',a)
print('-------**********--------')
# sort_num=sorted(a)
# acc=sort_num[::-1]
# print(acc)

# 4. Given a number N, print reverse of number N.
number=988
print('Original num:',number)
revs=0
while number>0:
    c=number%10
    revs= 10*revs+c
    number=number//10

print( 'Reversed Number is :',revs)
print('-------**********--------')
    
# 5 Given an array of numbers, find the maximum and minimum element in the array.

No=[54, 546, 548, 60]
print('original num:',No)
print( 'Minimun Number is:',min(No))
print('Maximum number is that:',max(No))