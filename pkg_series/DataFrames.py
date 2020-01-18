import pandas as pd
import numpy as np

lst_index = [1,2,3,4,5,6]
lst_names = ["Prateek","Ajay","Rahul","Arnab","Mukesh","Raafe"]
lst_age = [34,53,21,65,43,23]
dct = {"ID":lst_index,"Name":lst_names,"Age":lst_age}
df = pd.DataFrame(dct,index = lst_index)
print("df =")
print(df)
print(df)
print("\ndf.sum(0) =")
print(df.sum(0)) 
print("\ndf.sum(1) =")
print(df.sum(1)) 
print("\ndf.mean(0) =")
print(df.mean(0))
print("\ndf.mean(1) =")
print(df.mean(1))
print("\ndf.std(0) =")
print(df.std(0))
print("\ndf.std(1) =")
print(df.std(1))
a = 7
df11 = pd.DataFrame({"ID":7,"Name":"Manoj","Age":25},index = [a])
df = df.append(df11,sort=False)
print("\ndf =")
print(df)
df["age_id"] = df["ID"] + df["Age"]
print("\ndf after adding new column =")
print(df)
print("\ndf.iloc[1] =")
print(df.iloc[1])
print("\ndf.iloc[2:5] =")
print(df.iloc[2:5])
del df["ID"]

data = [{"ID":1,"Name":"Prateek","Age":26},{"ID":2,"Name":"Amit","Age":28},{"ID":3,"Name":"Amar","Age":24},{"ID":4,"Name":"Ajith"}]
df1 = pd.DataFrame(data)
print("\ndf1 =")
print(df1) 