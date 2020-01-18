import pandas as pd
import numpy as np
from _operator import index

s = pd.Series()
print("pd.Series() =", s)
print("pd.Series().empty =", s.empty)

ls = [(i+1)**2 for i in range(5)]
print(ls)
s = pd.Series([(i+1)**2 for i in range(5)],index = range(1,6))
print("s.empty =", s.empty)
print("s.ndim =", s.ndim)
print("s.size =", s.size)

arr = np.array([1,2,3,4,5])
s = pd.Series(arr,dtype=np.int64)
print("pd.Series(arr) =", s)
print("s.apply(lambda x:x**2) =", s.apply(lambda x:x**2))
print("Axes =", s.axes)
print("pd.Series(arr).sum() =", s.sum())
print("pd.Series(arr).mean() =", s.mean())

arr = np.array(['a','b','c','d','e'])
s = pd.Series(arr)
print("pd.Series(arr) =", s)

arr = np.array(['a','b','c','d','e'])
s = pd.Series(arr,index=[10,20,34,56,77])
print("pd.Series(arr,index):\n", s, end = "")
print("Axes =", s.axes)

dct = {"Name":"Prateek","Age":27,"Education":"BE"}
s = pd.Series(dct)
print("\npd.Series(dct) =\n", s)

dct = {"Name":"Prateek","Age":27,"Education":"BE"}
s = pd.Series(dct,index = [11,"Name","Education","Age"])
print("\npd.Series(dct,index) =\n", s)

dct = {"Name":"Prateek","Age":27,"Education":"BE"}
s = pd.Series(dct,index = [11,"Name"])
print("\npd.Series(dct,index) =\n", s)

s = pd.Series(5,index=[0,1,2])
print("\ns =\n", s)

s = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print("\ns[\"a\"] =", s["a"])
print("s[0] =", s[0])
print("\ns[\"c\":] =\n", s["c":])
print("\ns[\"b\":\"e\":2] =\n", s["b":"e":2])
print("\ns[[\"a\",\"c\",\"e\"]] =\n",s[["a","c","e"]])
#print("s[\"f\"] =", s["f"])

s1 = pd.Series([i**2 for i in range(1,5)],index=[i for i in range(1,5)])
print(s1)