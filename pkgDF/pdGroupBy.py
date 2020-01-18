import pandas as pd 
import numpy as np

dct = {"Id":[1,2,3,4,5,6],"Salary":[34000,43000,31000,25000,50000,32000],"Month":[6,3,4,3,2,6]}
dfr = pd.DataFrame(dct)
print("\nData Frame =")
print(dfr)
dfr1 = dfr.groupby("Month")
print("\n\ndfr.groupby(\"Month\") =\n")
for i,group in dfr1:
    print("Month =", i)
    print(group)
    print("\n")
    
print("\nGet Group 6 =")
print(dfr1.get_group(6))

print("\nMean =")
print(dfr1.agg(np.mean))

print("\nSum =")
print(dfr1.agg(np.sum))