import time
import random
from math import *
import operator
import pandas as pd
import numpy as np
import datetime as dt

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import warnings
warnings.filterwarnings('ignore')

import seaborn as sns
sns.set(rc = {'figure.figsize' : (12, 7)})
sns.set(style = 'white')

patient = pd.read_csv('./coronavirusdataset/PatientInfo.csv')
route = pd.read_csv('./coronavirusdataset/PatientRoute.csv')
time_series = pd.read_csv('./coronavirusdataset/Time.csv')

print(patient.head())
print('\n')
print(patient.info())
print('\n')
print(route.head())
print('\n')
print(route.info())
print('\n')
print(time_series.head())
print('\n')
print(time_series.info())
print('\n')


column = ['sex', 'country', 'city', 'province', 'infection_case', 'infection_order', 'state']

for col in column:
	print(patient[col].value_counts())
	print('\n')

patient['age'] = 2020 - patient.birth_year

def age_grp(age):
	if age > 0:
		if age % 10 != 0:
			lower = int(floor(age / 10) * 10)
			upper = int(ceil(age / 10) * 10) - 1
			return '{}-{}'.format(lower, upper)
		else:
			lower = int(age)
			upper = int(age) + 9
			return '{}-{}'.format(lower, upper)
	else:
		return np.nan

patient['age_group'] = patient.age.apply(age_grp)

sns.set(rc = {'figure.figsize' : (20, 7)})
ax = plt.subplot()
sns.set(style = 'white')
sns.countplot(patient.age.dropna().astype('int64'), orient = 'v', palette = 'Blues')
plt.title('Confirmed Cases by age', fontsize = 15)

for countplot in ax.xaxis.get_ticklabels() :
	countplot.fontsize = 3
	countplot.set_rotation(45)

plt.show()