#creating a dataframe/dataset

import pandas as pd
#how to convert dictionary to dataframes

data=pd.DataFrame({
    "name":["ali","khan","mahesh","vinit"],
    "age":[20,25,30,25],
    "branch":["cse","me","ise","ece"],
    "place":["banglore","delhi","mysore","porbandhar"]
})
print(data)

#saving the dataframes created as csv file
data.to_csv('id.csv',index=False)