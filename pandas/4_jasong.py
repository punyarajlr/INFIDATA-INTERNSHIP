#assuming a dataframe/dataset is already present,
#this is how we read/load it
import pandas as pd
#jason=javascript object notation
df=pd.read_json("data.json")
print(df)