import pandas as pd
from _operator import index
from _ast import Index
from attr.filters import include

df = pd.DataFrame()
print("pd.DataFrame() =", df)
print("pd.DataFrame().axes =", df.axes)

dt = [1,2,3,4,5]
df1 = pd.DataFrame(dt)
print("df1 =\n", df1)

#Writing column names in method
dt = [["Alex",10],["Bob",12],["Clarke",13]]
df2 = pd.DataFrame(dt,columns=["Name","Age"])
print("df2 =\n", df2)
print("df2.axes =\n", df2.axes)
print("df2.ndim =", df2.ndim)
print("df2.shape =", df2.shape)
print("df2.shape[0] =", df2.shape[0])
print("df2.shape[1] =", df2.shape[1])
print("df2.head(2) =\n", df2.head(2))
print("df2.tail(2) =\n", df2.tail(2))
print("df2.T =\n", df2.T)

#Writing column names in data set
dt = {"Name":["Tom","Jack","Steve","Ricky"],"Age":[28,34,29,42],"Rating":{3.21,5.32,6.21,4.23}}
df3 = pd.DataFrame(dt)
print("df3 =\n", df3)
print("df3.columns =\n", df3.columns)
print("df3.sum() =\n", df3.sum())
print("df3.sum(1) =\n", df3.sum(1))
print("df3[\"Name\"] =\n", df3[["Name","Age"]])

dt = {"Name":["Tom","Jack","Steve","Ricky"],"Age":[28,34,29,42]}
df4 = pd.DataFrame(dt,index = ["rank1","rank2","rank3","rank4"])
print("df4 =\n", df4)
print("df4.axes =\n", df4.axes)
print("df4.sum() =\n", df4.sum())
print("df4.mean() =\n", df4.mean())
print("df4.std() =\n", df4.std())
print("df4.shape =\n", df4.shape)
print("df4.count() =\n", df4.count())
print("df4.cumsum() =\n", df4.cumsum())
print("df4.cumprod() =\n", df4.cumprod(1))
print("df4.describe() =\n", df4.describe())
print("df4.describe(include = [\"object\"]) =\n", df4.describe(include = ["object"]))
print("df4.describe(include = [\"number\"]) =\n", df4.describe(include = ["number"]))

dt = [{"a":3,"b":4},{"a":5,"b":6,"c":7}]
df5 = pd.DataFrame(dt)
print("df5 =\n", df5)

dt = [{"a":3,"b":4},{"a":5,"b":6,"c":7}]
df6 = pd.DataFrame(dt,index = ["First","Second"])
print("df6 =\n", df6)

dt = [{"a":3,"b":4},{"a":5,"b":6,"c":7}]
df7 = pd.DataFrame(dt,index = ["First","Second"],columns=["a","b"])
df71 = pd.DataFrame(dt,index = ["First","Second"],columns=["a","b1"])
print("df7 =\n", df7)
print("df71 =\n", df71)

dt = {"one":pd.Series([1,2,3],index = ["a","b","c"])
      ,"two":pd.Series([1,2,3,4],index = ["a","b","c","d"])}

#Fetch one column
df8 = pd.DataFrame(dt)
print("df8 =\n", df8)
print("Column [\"one\"] =\n", df8["one"])

#Add one column
print ("\nAdding a new column by passing as Series:")
dt["three"] = pd.Series([10,20,30],index = ["a","b","c"])
df9 = pd.DataFrame(dt)
print("df9 =\n", df9)


print ("\nAdding a new column using the existing columns in DataFrame:")
dt["four"] = dt["three"] + dt["one"]
df10 = pd.DataFrame(dt)
print("df10 =\n", df10)

#Deleting columns
print ("\nDelete column [\"three\"]")
del dt["three"]
df11 = pd.DataFrame(dt)
print("df11 =\n", df11)

#Fetch Rows by label
print ("\nRow 'b' =\n")
row_data = df10.loc['b']
print(row_data)

#Fetch Rows by location
print ("\nRow '2' =")
row_data = df10.iloc[1]
print(row_data)

#Slice rows
print ("\nRow[1:3] =")
row_data = df10.iloc[1:3]
print(row_data)

#Adding row in Data Frame
print("\nAdding 2 rows")
df1 = pd.DataFrame([[1,2],[3,4]],columns=["a","b"])
df2 = pd.DataFrame([[5,6],[7,8]],columns=["a","b"])
df = df1.append(df2)
print("df =\n" , df)

#Delete rows
df.drop(0)
print("\n", df)

