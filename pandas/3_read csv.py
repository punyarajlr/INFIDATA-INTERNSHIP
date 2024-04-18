#assuming a adatframes/dataset is already present
#this is how we read/load it

import pandas as pd #for creating and handling dataframes
#loading id.csv into pandas dataframes
data=pd.read_csv("diabetes.csv")
print(data)#displaying the dtaframe

print("display secific columns")
print(data['Glucose'])#displaying single column
print(data[["Glucose","BMI"]])#displaying multiple column

print(data.shape)#displays shape of dataset

print(data.size)#displays size of data

#indexing
print(data.head())#prints first 5 rows of data

print(data.tail())#prints last 5 rows of data