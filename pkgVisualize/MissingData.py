import numpy as np
import pandas as pd
import copy as cp

df = pd.read_csv("C://Users/Prateek/Documents/ExcelDocs/melbourne.csv")
sm = df.isna().sum()
print("df.isna().sum() =", sm)

#any() = Columns having at least 1 null value
df1 = df.any()
print("\ndf.any() =\n", df1)

df1 = df.any().sum()
print("\ndf.any().sum() =", df1)

a = np.array([[4, 3, 1], [5, 7, 0], [9, 9, 3], [8, 2, 4]])
a[[0,2]] = a[[2,0]]
print("\na =\n", a)
print("abc")
print("mnc")