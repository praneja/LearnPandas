import pandas as pd
import numpy as np

dt1 = {"id":[1,2,3],"Name":["Prateek","Amit","Rajat"],"Age":[28,33,21]}
df1 = pd.DataFrame(dt1)

df = pd.DataFrame({'Animal' : ['Falcon', 'Falcon',
                                'Parrot', 'Parrot'],
                    'Max Speed' : [380., 370., 24., 26.],
                    "Age":[1,2,3,4]})

newdf = df.groupby(['Animal'])["Max Speed","Age"].mean()
print(newdf)
# for key, item in newdf:
#     print(newdf.get_group(key))


dt2 = {"id":[1,2,3,4,5,6,7],"Salary":[34000,23000,34000,21000,19000,18800,32000],"Month":[2,5,2,3,2,3,1]}
df2 = pd.DataFrame(dt2)
df3 = df2.groupby(["Month"])
print("\nGroup by Month =\n", df3)

df3 = pd.merge(df1,df2,how="inner",on="id")
print("\n", df3)

df4 = pd.merge(df1,df2,how="outer",on="id")
print("\n", df4)

dt3 = {"id":[4,5,6],"Name":["Rajesh","Manish","Ajay"],"Age":[22,21,19]}
df5 = pd.DataFrame(dt3)

df6 = pd.concat([df1,df5])
print("\ndf6 =\n", df6)

df7 = pd.concat([df1,df5],axis=0)
print("\ndf7 =\n", df7)

gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],'Medals': [15, 13, 9]})
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],'Medals': [29, 20, 16]})
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],'Medals': [40, 28, 27]})

df3 = pd.concat([gold, silver,bronze]).fillna(0).groupby('Country').sum()                  
print(df3.sort_values(by='Medals', ascending=False).astype(float))

df_new = pd.concat([gold,silver,bronze])
print("\nNewDF =\n", df_new)
