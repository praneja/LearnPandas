import pandas as pd

dct1 = {"Id":[1,2,3,4,5],"Name":["Prateek","Rajat","Rahul","Anuj","Manish"],"Age":[28,42,15,67,43]}
dfr1 = pd.DataFrame(dct1)
print("Data Frame1 =")
print(dfr1)

dct2 = {"Id":[1,2,3],"Salary":[34000,50000,32000],"Month":[3,2,6]}
dfr2 = pd.DataFrame(dct2)
print("\nData Frame2 =")
print(dfr2)
print("\nSalary mean =", round(dfr2["Salary"].mean(), 3))

dfr3 = pd.merge(dfr1,dfr2,on="Id",how="left")
print("\nMerged Left DF =")
print(dfr3.fillna(0))

dfr4 = pd.merge(dfr1,dfr2,on="Id",how="right").fillna(0)
print("\nMerged Right DF =")
print(dfr4)

dfr5 = pd.merge(dfr1,dfr2,on="Id",how="outer").fillna(0)
print("\nMerged Outer DF =")
print(dfr5)

dfr5 = pd.merge(dfr1,dfr2,on="Id",how="inner").fillna(0)
print("\nMerged Inner DF =")
print(dfr5)
