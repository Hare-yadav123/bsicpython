import pandas as pd 

Data={"Name":["Raju","prince","Karan","Haree","vishanu"],
      
      "Address":["Patna","Chaapra","Devghar","Banka","Shivan"],
      "Qualificatiion":["B-Tech","Diploma","Mca","Mba","Bcom"],
      "Result":["Pass","Pass","Pass","Pass","Pass",]}

dp=pd.DataFrame(Data)
print(dp)


#List using tuple
import pandas as pd 

Data=[('suman',20,'patna',20000),
      ('suman',20,'patna',20000),
      ('suman',20,'patna',20000),
      ('suman',20,'patna',20000),
      ('suman',20,'patna',20000),
      ('suman',20,'patna',20000),
      ('suman',20,'patna',20000),
      ]
dp=pd.DataFrame(Data,),'columns'(['Name','age','City','salary'])
print(dp)

