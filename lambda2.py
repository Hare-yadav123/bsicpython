def table(n):
    for i in range(1,11):
        print(n*i)
table(2)
table(10)



q=lambda x:x**x
print(q(3))


m=lambda n,l,k:n*l*k
print(m(20,30,40))


def mul(n,l,k):
    r=n*l*k
    return r
p=mul(20,30,40)
print(p)


def result(x,y):
    if x>y:
        print('x is big number')
    else:
        print('y is a big number')
result(20,40)

r=lambda b,c:b if (b>c) else c 
print('The greater number showing here:',r(10,0))

def even(n):
    if n%2==0:
        return True
    else:
        return False   
a=[20,30,50,9,11,2]
print('with function',tuple(filter(even,a)))


v=[10,5,2,40,30,9]
s=list(filter(lambda a:a%2==0,v))
print('with lambda function:',s)


# s='my name is haree is '
# for i in range(len(s)):
#     print(s[i],'=',i)
    
# print(s.index('is'))
# print(s.rindex('is'))
