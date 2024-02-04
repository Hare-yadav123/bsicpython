# import pandas as pd 

# Data={"Name":["Raju","prince","Karan","Haree","vishanu"],
      
#       "Address":["Patna","Chaapra","Devghar","Banka","Shivan"],
#       "Qualificatiion":["B-Tech","Diploma","Mca","Mba","Bcom"],
#       "Result":["Pass","Pass","Pass","Pass","Pass",]}

# # dp=pd.DataFrame (Data.loc[(Data.Name=="Raju") & 
# #                           (Data.Address & gt)] )
# # print(dp)
# dp=pd.DataFrame (Data.iloc[0,2])
# print(dp)

# n=5
# for i in range(5):
#       print(i*i)

if __name__ == '__main__':
    n = int(input())
    
for i in range(1,n+1):
    print(i,end='')

# list comprehention
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n)
    
    # runner score up 
    if __name__ == '__main__':
    n = int(input())# 1,2,4,5,6
    arr = map(int, input().split())
    arr1=set(arr)
    arr2=sorted(arr1)
    print(arr2[-2])
    
    #nasted list
    if __name__ == '__main__':
    alist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name,score])
second_highest= sorted(set([score for name,score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score==second_highest])))