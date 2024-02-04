''' 
IDENTYFIER=identifier is a nothing but name in python programme. 
it can be class name ,function() name ,varieble name,module name.

RULE OF IDENTIFIER=
1 ALPHABET(upper or lower ) 2. digit(0-9) 3. underscore(_)

2. it should not be start with digit
3. it should be start always alphabetic char ,it may be upper or lower
4. we can use speceal charecter only underscore  (_)
5. we can't use reserved  word (keywor)
its may case sensetive
'''

var=20
VAR=10
print(var)
print(VAR)

class Om:
    def ankush(self):
        print('akhelish')
        print('haree')
o=Om()
o.ankush()
# code of cheak python and django version 
'''python --version
django-admin --version'''


######################PYTHON KEYWORDS##############################
'''
Keywords are the reserved word in python , whose meaning already define inthe interpreter.
According python version 3.7.0 ,33 keywords and python version 3.10.0 , 35 keywords 

#we can't use keyword as a variable name, method name,any others, idetifier,
python keywords are the . case sensetive
'''
import keyword
print(keyword.kwlist)

########################Variables#########################
'''variable=variable is a name of memory location where use can stored different types of data or value
a=10,20

type()=it return the data type of given value
'''
a=20
print(type(a))
b=True
print(type(b))
c=None
print(type(c))

''' 
1.True,False,None,as, assert,async,await,and,break ,class,contnoue, def, del,elif,except,else,for,from,finally, 
2.globle,import,in, is,if ,lambda,not,nonlocal, or,pass,return,raise,try,while,with,yield,
'''