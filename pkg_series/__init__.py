import pandas as pd
import numpy as np

sr = pd.Series()
print("pd.Series() =", sr)

sr = pd.Series([1,4,2,5,3])
print("\nsr =")
print(sr)

sr1 = pd.Series([1,4,2,5,3],index=["a","b","c","d","e"])
print("\nsr1 =")
print(sr1)
print("sr1.loc[\"c\"] =",sr1.loc["c"])
print("sr1[\"c\"] =",sr1["c"])
print("sr1[[\"a\",\"c\",\"d\"]] =")
print(sr1[["a","c","d"]])
#print("sr1[\"g\"] =",sr1["g"])

lst_index = [1,2,3,4,5,6]
lst_names = ["Prateek","Ajay","Rahul","Arnab","Mukesh","Raafe"]
dct = dict(zip(lst_index,lst_names))
sr2 = pd.Series(dct,index = lst_index)
print("\nsr2 =")
print(sr2)
print("\nsr2[2] =", sr2[2])
print("\nsr2.iloc[3] =", sr2.iloc[3])
print("\nsr2[1:4] =")
print(sr2[1:4])
print("\nsr2[:3] =")
print(sr2[:3])
print("\nsr2[1:5:2] =")
print(sr2[1:5:2])


sr3 = pd.Series(5,index = lst_index)
print("\nsr3 =")
print(sr3)

sr4 = pd.Series([18,74,23,56,32])
print("\nsr4 =")
print(sr4)
print("sr4.sum() =",sr4.sum())
print("sr4.mean() =",sr4.mean())
print("sr4.std() =",sr4.std())
print("sr4.max() =",sr4.max())
print("sr4.min() =",sr4.min())
print("\nsr4.cumsum() =")
print(sr4.cumsum())

