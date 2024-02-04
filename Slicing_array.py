from array import*
stu_roll=array("i",[101,102,103,104,105,106,107])
print("original array")
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])
print(("***********************************"))

print(stu_roll[-2:])
a=stu_roll[2:2:2]
for i in a:
    print(i)