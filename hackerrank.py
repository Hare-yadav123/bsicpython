# if __name__ == '__main__':
#     s = input()
#     print(any(map(str.isalnum, s)))
#     print(any(map(str.isalpha, s)))
#     print(any(map(str.isdigit, s)))
#     print(any(map(str.islower, s)))
#     print(any(map(str.isupper, s)))
    
'''width=30
print('Harendra'.ljust(width))
print('Harendra'.rjust(width,'-'))
print('Harendra'.center(width,'-'))

#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
'''

# Wrap function
# import textwrap

# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)
    

# if
# __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# N, M = map(int, input().split())
# for i in range(1, N, 2):
#     print (str('.|.' * i).center(M, '-'))
# print ('WELCOME'.center(M, '-'))
# for i in range(N-2, -1, -2):
#     print (str('.|.' * i).center(M, '-'))# Enter your code here. Read input from STDIN. Print output to STDOUT

'''def print_formatted(number):
    pad = number.bit_length()
    for i in range(1,number+1):
        print(str(i).rjust(pad),oct(i).split("o")[1].rjust(pad),hex(i).split("x")[1].upper().rjust(pad),bin(i).split("b")[1].rjust(pad))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)'''
    
# import math
# import os
# import random
# import re
# import sys
# def solve(s):
#     return " ".join([name.capitalize() for name in s.split(" ")])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()

#10
def minion_game(string):
    # your code goes here
    s=len(string)
    vowel = 0
    consonant = 0
     
    for i in range(s):
        if string[i] in 'AEIOU':
           vowel+=(s-i)
        else:
           consonant+=(s-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')

s = input('Enter your input')
minion_game(s)

#11
'''def merge_the_tools(string, k):
    # your code goes here
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print (''.join(temp))
            temp = []
            len_temp = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)'''
    
    
#12
# from itertools import product
# a = map(int, input().split())
# b = map(int, input().split())

# print(*product(a, b))

#13
# import itertools

# ll, n = input().split()

# for i in itertools.permutations(sorted(ll),int(n)):
#     print("".join(i))


#15
# from itertools import combinations_with_replacement

# S,k = input().split()
# k = int(k)

# print ('\n'.join(sorted(''.join(sorted(c)) for c in combinations_with_replacement(S,k))))

# 16 importing the groupby method
# from itertools import groupby

# # using for loop to iterate through the string
# for k, c in groupby(input()):
        
#     #printing the output
#     print("(%d, %d)" % (len(list(c)), int(k)), end=' ')