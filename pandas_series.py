import pandas as pd 
a=pd.__version__
print(a)

lst_s=[1,2,-3,4,"data base"]
series=pd.Series(lst_s)
print(series)

#short tric
series2=pd.Series([1,2,38,'hsree'])
print(series2)

#Empty series
empty_s=pd.Series([])
print(empty_s)

#data series with manual index value
series4=pd.Series([1,2,3,4],['a','b','c','d'],dtype=float, name='data value')
print(series4)

# same value copy only write index
scalar_s=pd.Series(0.5,index=[1,2,3,4])
print(scalar_s)

# we can access the series value using index
series2=pd.Series([1,2,38,'hree'])
print(series2)
print(series2[0])

# we can slice and uyse conditional statemnent
series2=pd.Series([1,2,38,5,8])
print(series2[0:3])
print("*****")
k=series2[series2>2]
print(k)

# we can add two series
series6=pd.Series([1,2,3,4])
series7=pd.Series([1,2,3,4,5])

print(series6+series6)

