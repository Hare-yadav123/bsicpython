# example of lower and upper method
str1="My name is Harendra Yadav"
u=str1.upper()
print(u)

# python program remove the nth index character fron non-empty string
'''def rem(string,n):
    f=string[:n]
    l=string[n+1:]
    return f,l

string=input("Enter sfrting")
n=int(input("Enter index nof sring for removing"))
print(rem(string, n))'''
 
# Anagaram (ulta)
'''s1=input("Enter 1st str")
s2=input("Enter 1st str")
if sorted(s1)==sorted(s2):
    print("anagaram")
else:
    print("non anagaram")'''
    
#python program to from new string where the first char and last char have been exchange
'''def conn(s):
    string=s[-1:]+s[1:-1]+s[:1]
    return string
s=input("enter sring")
print(conn(s))'''


s3="hare"
c=s3[-1:]
d=s3[1:-1]
e=s3[:1]
print(c+d+e)

# find vowels from given string string
'''vowels=input("Enter your string:")
char=''
for i in vowels:
    if i=='a' or i=='i' or i=='o' or i=='u' or i=='e':
        char=char+i 
    print(char)'''

# replace apace with hypen(-)   
# sen=input("Enter your string")
# rep=sen.replace(' ',"-")
# print(rep)

# find lenth of strinf without library fun mean len()
'''sen=input("Enter your string")
count=0
for i in sen:
    count=count+1
print(count)'''

# Remove odd index char given string
'''def odd_str(char):
    store=''
    for i in range(len(char)):
        if i%2==0:
            store=store+char[i]
    return store       
char=input("enter string")
print(odd_str(char))'''

# count the char and word persenr in string by programm
'''string=input("enter string")
char=0
word=1
for i in (string):
    char=char+1
    if i==' ':  # one space(" ") means 1
        word=word+1
print("character=",char)
print("word =",word)'''

# write program between two string who is big
'''string1=input("enter string1:")
string2=input("enter string2:")
count1=0
count2=0
for i in string1:
    count1=count1+1
for j in string2:
    count2=count2+1
if count1>count2:
    print(" it is Larger stringis:")
elif count1==count2:
    print("Bothe are equal")
else:
    print("count2 is larger")'''
    
# write python program and count how many lower and upper  case string persent
'''string=input("enter string:")
count1=0
count2=0
count3=0
for i in string:
    if i.islower():
        count1=count1+1
    elif i.isupper():
        count2=count2+1
    elif i.isdigit():
        count3=count3+1
print("Lower letter:",count1) 
print("upper letter",count2)
print(count3)'''
# check given string is a palidrome or not
'''string=input("enter string")
if string==string[::-1]:
    print("This is a palidrom string")
else:
    print("This is not palidrom string")'''
    

# lst=[n for n in input("enter input").split("-")]
# lst.sort()
# print("-".join(lst)

#display first two & last two letter in string
# string=input("enter string:")
# b=string[:2]+string[-3:]
# print(b)

# find sub string
'''string=input("enter string:")
sub_str=input("enter")
if (string.find(sub_str)==-1):
    print("it is find ")
else:
    print("it is not find")'''
    
    
#permutation of list
'''def perml(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return [lst]
    else:
        l=[]
        for i in range(len(lst)):
            x=lst[i]
            sx=lst[:i]+lst[i+1:]
            for j in perml(sx):
                l.append([x]+j)
            return l
    
data=list('ABC')
for p in perml(data):
    print(p)'''
    
    
#python program cheak whetherbstring start with specific charactor
'''s="Vipmarsal.com"
print(s.startswith("Vip"))
print(s.endswith(".com"))'''

#python program toi illustrate caesar cipher Technique
'''def Encrypt(text,s):
    re=' '
    for i in range(len(text)):
        char=text[i]
        # in uppercase 
        if char.isupper():
            re+= chr((ord(char) + s-65) % 26 + 65)
        # lowercase
        else: 
            re += chr((ord(char) + s-97) % 26 + 97)
    return re
text="haree"
s=4
ob=Encrypt(text, s)
print(ob)'''
#
import textwrap
sample_text='''
python is a widely used high-level, general-purpose,interpreted ,dynamic
programing language. Its design philosopyemphasize code readibility, and its syntax allows 
programmers to express concepts in fewer lines of code than possible in language such as c++ or java.

'''
withot_indentation=textwrap.dedent(sample_text)
final_result=textwrap.indent(sample_text, ">")
print("originsal=")
print(sample_text)
print("after  wraps")
print(textwrap.fill(sample_text , width=50))
print("**********************************")
print(withot_indentation)

print(textwrap.fill(final_result , width=50))

#writebpython program to print folloeing number upto 2 decimal place
x=5.6839
y=3.105689
z=567
print("original value",x)
print("original valu{:.2f}".format(x))
print("original value",y)
print("original value{:.2f}".format(y))
print('{:.0f}'.format(y))  # No decimal place


#write python program print follopwing intwrger with zero on the left of specific width
z=567
print('{:0<5d}'.format(z))  

#write python program to display  integer value with quama
c=2000000000
d=536334656656533
print('{:,}'.format(c))
print('{:,}'.format(d))

#
d=55
print('{:<10d}'.format(d))
print('{:10d}'.format(d))
print('{:>10d}'.format(d))

#count
s1='dqjhwiuijk  kjhaaaaaa'
print(s1.count('a'))

#reversed 
s2="My name is Harendra yadav"
print(" ".join(reversed(s2)))

#reversed word in string
s2="My name is Harendra yadav"
#i=s2.split()
#print(i)
for i in s2.split():
    print(i)
    print(' '.join(i.split()[::-1]))