d=100
speed1=0.7 #speed per second covered distance c1
t1=d/speed1  #total time taken by c1 covered 100m
print(t1)

d=100
speed2=0.8  #speed per second covered distance c2
t2=d/speed2  #total time taken by c2 covered 100m
print(t2)
print(50/0.8)

import random
a='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%!~'
lth=10
password=''.join(random.sample(a, lth))
print('your passwor is:',password)