import numpy as np
import pandas as pd

example3_data=pd.DataFrame({'x':[-5,-4,-3,-2,-1,0,1,2,3,4,5],'y':[0,0,0,0,0,1,1,1,1,1,1]})
print(example3_data)

x=example3_data['x'].values.reshape(-1,1)
y=example3_data['y'].values.reshape(-1,1)

from sklearn.linear_model import LinearRegression
linear_regressor=LinearRegression()
linear_regressor.fit(x,y)
print('[info] linear regression model training complete..')

m=linear_regressor.coef_
c=linear_regressor.intercept_

print(f"m value is :{m}")
print(f"c value is:{c}")
print(f"equation of line is : y={m}x+{c}")

new_user_input=float(input("enter value of x:"))
new_user_input=[[new_user_input]]
new_output=linear_regressor.predict(new_user_input)[0]
print(f"when x={new_user_input},y={new_output}")

sigma=1/(1+np.exp(-new_output[0]))
print(f"sigma value={sigma}")