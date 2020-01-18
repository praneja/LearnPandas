import pandas as pd

dct1 = {"Id":[1,2,3],"Name":["Prateek","Rajat","Rahul"],"Age":[28,42,15]}
dfr1 = pd.DataFrame(dct1)
print("DataFrame1 =")
print(dfr1)

dct2 = {"Id":[4,5,6],"Name":["Anuj","Manish","Ajit"],"Age":[67,43,32]}
dfr2 = pd.DataFrame(dct2)
print("\nDataFrame2 =")
print(dfr2)

drf3 = pd.concat([dfr1,dfr2])
print("\nDataFrame3 =")
print(drf3)

drf4 = pd.concat([dfr1,dfr2],keys=["A","B"])
print("\nDataFrame with Keys =")
print(drf4)

drf5 = pd.concat([dfr1,dfr2],ignore_index=True)
print("\nDataFrame with own index =")
print(drf5)

drf6 = pd.concat([dfr1,dfr2],axis=1)
print("\nDataFrame Concatenation along columns =")
print(drf6)

drf7 = dfr1.append(dfr2)
print("\ndfr1.append(dfr2) =")
print(drf7)

print("\nCurrent Time =", pd.datetime.now())

print("\nTimeStamp =", pd.Timestamp("2017-03-01"))

print("\nTime Range in minutes =", pd.date_range("11:00","13:30",freq="30min").time)

print("\nTime Range in minutes =", pd.date_range("11:00","11:05",freq="2min").time)

print("\nTime Range in hours =", pd.date_range("11:00","13:30",freq="H").time)

print("\nDate range in days =", pd.date_range("01/10/2019",periods=5).date)

print("\nDate range in months =", pd.date_range("01/10/2019",periods=5, freq="M").date)