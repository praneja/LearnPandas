import pandas as pd

lst_index = [1,2,3,4,5,6]
lst_names = ["Prateek","Ajay","Rahul","Arnab","Mukesh","Raafe"]
lst_age = [34,53,21,65,43,23]
dct = {"ID":lst_index,"Name":lst_names,"Age":lst_age}
df = pd.DataFrame(dct,index = lst_index)
print("df =")
print(df)

lst_index1 = [7,8,9]
lst_names = ["Manish","Rohit","Sharan"]
lst_age = [34,53,21]
dct = {"ID":lst_index1,"Name":lst_names,"Age":lst_age}
df2 = pd.DataFrame(dct,index = lst_index1)
print("\ndf2 =")
print(df2)
newdf = pd.concat([df,df2])
print("\nnewdf =")
print(newdf)

lst_salary = [49000,32000,45000,32000,22000,12000,56000,43000,23000]
lst_mnth = [3,4,1,4,6,7,2,4,2]
dct = {"ID":lst_index+lst_index1,"Salary":lst_salary,"Month":lst_mnth}
df1 = pd.DataFrame(dct,index = lst_index+lst_index1)
print("\ndf1 =")
print(df1)

df2 = pd.merge(newdf,df1,on="ID",how="inner")
print("\ndf2 =")
print(df2)