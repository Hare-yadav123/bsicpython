# operator precedence

esp=20+30*40
print(esp)

#precedence of 'or' & 'abd '
name='Haree'
age=0
if name=='Haree' or name=='Raju' and age >=2: # and precedece is high compaire to 
    print('Hello! Welcome')
else:
    print('Good bye ! !')
    

# parenthecis precedence is hogh compaire to and operatOr
name='Haree'
age=0
if (name=='Haree' or name=='Raju') and age >=2:
    print('Hello! Welcome')
else:
    print('Good bye ! !')
    
'''OPERATOR ASSOCCIATIVITY =if expression contain two or more operator with same precedence then operator associativity is used 
it LEFT TO RIGHT OR FROM RIGHT TO LEFT
'''

# LEFT TO RIGHT PRECEDENCE
print(100/10*10)
print((100/10)*10)
print(100*10/10)
print((10*10)/100)

print(100+200/10-3*10)