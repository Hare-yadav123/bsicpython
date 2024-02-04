# PICKLING=Pckling is process of convert class object into byte stream so that it can strode into file. this is also called object serialization

# we used pickle module for performing pickling and unpicling

# dump()function=This function is used to perform pickling. It returns the pickled representation of the objectas byte object, instesd  of writin itstead to na file 

# This methiod belond to pickle module

#UNPICKLING=Pckling is process of convert byte stream  INTO class object .it is inverse operation of pickling. this is also called object de-serialization
 
# pickling and unpicklin always support binory file sice they support byte stream.

#LOAD()FUNCTION=THIS FUNCTION USED TO READ  PICKLED OBJECT FROM A BINARY FILE AND RETURN IT INTO OBJECT

###    WHY NEED PICKLING AND UNPICKLING  ##
# when we store some structured data in the file and want to perfom calculation that time we need pickling unpickling


'''import pickle,pick
n=int(input("Enter number: "))
with open("student.text",mode="wb") as f:
    for i in range(n):
        name=input("Enter your name:")
        roll=int(input("Enter your roll:"))
        address=input("Enter your address:")
            
    stu=pick.student(name,roll,address)
    #stu2=pick.student("raju",105,"Bihar")
    #stu3=pick.student("vishanu",110,"Bihar")
    pickle.dump(stu,f)
    #pickle.dump(stu2,f)
    #pickle.dump(stu3,f)
    print("done ")
    
with open("student.text","rb") as f:
    while True:
        try:
            pickle.load(f)
            print(" unpickling done")
            stu.disp()
        except EOFError:
            print("Exception handle")
            break
    #stu2.disp()
    #stu3.disp()'''
#Example
# import pickle,pick
# data=['Aanshu',98,21,95]
    
# byte=pickle.dumps(data) # pickling
# print(byt)

# #unpickling
# data2=pickle.loads(byte)
# print(data2)




# import pickle,pick
# data=['Aanshu',98,21,95]
# f= open('sum.txt','wb')
# pickle.dumps(data,f) # pickling
# f.close()

# #unpickling
# f=open('sum.txt',mode='rb') 
# pickle.loads(data,f)
# f.close()


import pickle
# lst1=[4,5,8,9,1]
# file2=open("file.pkl","wb")
# pickle.dump(lst1,file2)
# file2.close()

file1=open('file.pkl','rb')
lb=pickle.loads(file1)
file1.close()
print(lb)