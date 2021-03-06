# -*- coding: utf-8 -*-
"""Boston_Housing_prices.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DqdvlhogU5OZouSINLHEHKCkdPo8k-S2
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matlpotlib inline
from sklearn import metrics

names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data_frame = pd.read_csv('housing.csv', delim_whitespace =True, names = names)
data_frame.head(10)

data_frame.drop(['CRIM','ZN','INDUS','NOX','AGE','DIS','RAD'], axis = 1)
prices = data_frame['MEDV']
features = data_frame.drop(['MEDV'],axis =1)

x_train, x_test, y_train, y_test = train_test_split(features, prices, test_size =1/3, random_state=0)

reg = LinearRegression()
reg.fit(x_train, y_train)

y_pred = reg.predict(x_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df

from sklearn import metrics
print("Mean absolute error", metrics.mean_absolute_error(y_test, y_pred))
print("Mean squared error", metrics.mean_squared_error(y_test, y_pred))
print("Root Mean squared error", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

plt.figure(figsize =(12,8))
plt.scatter(y_test, y_pred, color='red')
#plt.plot(x_test, y_pred,color ='blue')
plt.xlabel("Prices")
plt.ylabel("Predicted Prices")
plt.show()

