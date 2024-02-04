# String means group of character , its enclose single quotes or double quotes.

#Multiple line string
# str= '''hello 
# ram ,how are you,
# tell me about yopu'''
# print(str)

# Memory allocation or location
# sr="haree a good boy"
# sw="haree a good boy"
# sq="python"
# print(id(sr))
# print(id(sw))
# print(id(sq))

# Index repersent the position of number of character in string
'''rs=" i belong to Bihar"
print(rs[-1])'''

# replace function
'''rs=" i belong to Bihar"
z=rs.replace("Bihar", "patna")
print(z)

# Lenth method
rs=" i belong to Bihar"
c=len(rs)
print(c)

# Split method seprate with comma and inverted comma convert in list
rs="i belong to Bihar"
n=rs.split()
print(n)'''


# Join method
rs=(" i belong to Bihar","i got job")
cs=" ,hello! ".join(rs)
print(cs)

rs="i belong to Bihar"
n=rs[2:5]
print(" i  am do slicing:",n)

ac=[4,5,6,8,9,7,]
nm=ac[-3:]
print(nm)