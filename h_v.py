import pandas as pd 

Data1=pd.DataFrame({"Roll":range(1,5),
                    "roll code":range(10,6,-1),
                    "s":["a","b","c","d"],
                    "c code":range(26,22,-1)})
print(Data1)


Data2=pd.DataFrame({"x":range(2,8),
                    "g":["a","b","c","d","g","g"],
                    "roll code":range(12,1,-2)
                    })
print(Data2)