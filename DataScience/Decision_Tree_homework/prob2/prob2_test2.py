import numpy as np
import pandas as pd
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.datasets import load_wine

wine = load_wine()
print(wine.head())
'''
   fixed acidity  volatile acidity   ...     alcohol  quality
0            7.4              0.70   ...         9.4        5
1            7.8              0.88   ...         9.8        5
2            7.8              0.76   ...         9.8        5
3           11.2              0.28   ...         9.8        6
4            7.4              0.70   ...         9.4        5

[5 rows x 12 columns]
'''
print(wine.tail())
'''
      fixed acidity  volatile acidity   ...     alcohol  quality
1594            6.2             0.600   ...        10.5        5
1595            5.9             0.550   ...        11.2        6
1596            6.3             0.510   ...        11.0        6
1597            5.9             0.645   ...        10.2        5
1598            6.0             0.310   ...        11.0        6

[5 rows x 12 columns]
'''
print(wine.shape) #(1599, 12)
print(wine.describe())
'''
       fixed acidity  volatile acidity     ...           alcohol      quality
count    1599.000000       1599.000000     ...       1599.000000  1599.000000
mean        8.319637          0.527821     ...         10.422983     5.636023
std         1.741096          0.179060     ...          1.065668     0.807569
min         4.600000          0.120000     ...          8.400000     3.000000
25%         7.100000          0.390000     ...          9.500000     5.000000
50%         7.900000          0.520000     ...         10.200000     6.000000
75%         9.200000          0.640000     ...         11.100000     6.000000
max        15.900000          1.580000     ...         14.900000     8.000000
​
[8 rows x 12 columns]
'''
print(wine.iloc[:,-1].value_counts())
'''
5    681
6    638
7    199
4     53
8     18
3     10
Name: quality, dtype: int64
'''

x_data = wine.iloc[:,:-1]
y_data = wine.iloc[:,-1]
print(x_data.shape) #(1599, 11)
print(y_data.shape) #(1599,)
x_data = x_data.values
y_data = y_data.values

####################

x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data, y_data, test_size=0.33)

estimator = DecisionTreeClassifier(criterion='gini', max_depth=None, max_leaf_nodes=None, min_samples_split=2, min_samples_leaf=1, max_features=None)

estimator.fit(x_train, y_train)

y_predict = estimator.predict(x_train) 
score = metrics.accuracy_score(y_train, y_predict)
print(score) #1.0

y_predict = estimator.predict(x_test) 
score = metrics.accuracy_score(y_test, y_predict)
print(score) #1.0