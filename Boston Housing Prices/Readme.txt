The data set we are using is famous Boston Housing prices taken from Kaggle. Linear Regression models predict the Median value house prices.
Each record in the database describes a Boston suburb or town. The data was drawn from the Boston Standard Metropolitan Statistical Area (SMSA) in 1970.

The attributes are de?ned as follows (taken from the UCI Machine Learning Repository
1): CRIM: per capita crime rate by town 
2. ZN: proportion of residential land zoned for lots over 25,000 sq.ft.
3. INDUS: proportion of non-retail business acres per town.
4. CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
5. NOX: nitric oxides concentration (parts per 10 million) 1https://archive.ics.uci.edu/ml/datasets/Housing 123 20.2. Load the Dataset 124.
6. RM: average number of rooms per dwelling.
7. AGE: proportion of owner-occupied units built prior to 1940.
8. DIS: weighted distances to ?ve Boston employment centers.
9. RAD: index of accessibility to radial highways.
10. TAX: full-value property-tax rate per $10,000.
11. PTRATIO: pupil-teacher ratio by town.
12. B: 1000(Bk-0.63)2 where Bk is the proportion of blacks by town.
13. LSTAT: % lower status of the population.
14. MEDV: Median value of owner-occupied homes in $1000s We can see that the input attributes have a mixture of units.

The dataset consists of all the above mentioned attributes. But the Median value(MEDV) is mainly depends on CHAS, RM, TAX, PTRATIO, B, LSTAT.
Because these attributes are corelated with MEDV. So I chosed these as features and MEDV as target.

Mean absolute error is 3.555474556662593