'''import random
u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l="abcdefghijklmnopqrstuvwxyz"
n="1234567890"
s="!#$%^&*+/*-"
lenth=16
string=u+l+n+s
password=" ".join(random.sample(string,lenth))
print("************")
print("your passord is that:",password)
print("*************")'''


import random
'''num='1234567890'
len=4
print("******")
otp="".join(random.sample(num,len))
print(otp)
print("****")'''


u="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890=!#$%^&*+/*-"
len=10
pas=" ".join(random.sample(u, len))
print(pas)
import random
ac='abdhdgjejkeje'
sv=5
ad=' '.join(random.sample(ac,sv))
print(ad)

import keyword
print(keyword.kwlist)