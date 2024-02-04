

# WRITE PYTHON PROGRAMN PRINT DUPLICATE PERSENT IN LIST

'''abc=['Raju',20,30,10,20,40,50,30,80]
cv=[]
for ele in abc:
    if abc.count(ele)>1 and ele not in cv:
        cv.append(ele)
print(cv)

#withou using Buil-in method
abc=['Raju',20,30,10,20,40,50,30,80]
cv=[]
for i in range(len(abc)):
    for j in range(i+1,len(abc)):
        if abc[i]==abc[j] and abc not in cv:
            cv.append(abc[i])      
print(cv)

# vowels counting logic
a=input('enter your name')
count=0
v=['a','e','i','o','u']
for i in a:
    #if i in v:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(count)


n=input('enter you word')
count=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j] and i not in count:
            count.append(n[i])
            
print(count)

n=input('enter you word')
count=[]
for i in n:
    if n.count(i)>1 and i not in count:
        count.append(i)
print(count)'''

# armstrong b/w 1-1000
'''for i in range(1,1001):
    num=i
    sum1=0
    n=len(str(i))
    while (i!=0):
        digit=i%10
        sum1=sum1+digit**n
        i=i//10
    if num==sum1:
        print(num)'''
        
        
def func(num):
    for i in range(1,num+1):
        am=i
        sum1=0
        n=len(str(i))
        while i!=0:
            digit=i%10
            sum1=sum1+digit**n
            i=i//10
        if am==sum1:
            print(am) 

func(1000)

# findout least positive number from the list

a=[-1,5,40,10,-9,4,20,30]

#com_list=range(len(a))
ab=sorted(a)
print(min(ab))
