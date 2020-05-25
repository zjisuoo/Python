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

plt.figure(figsize = (12, 7))
reason_list = list(patient['infection_case'].value_counts().sort_values(ascending = False).index)
reason_data = patient.infection_case.value_counts().rename_axis('Reason').reset_index(name = 'Count')
sns.barplot(x = 'Count', y = 'Reason', order = reason_list, data = reason_data, palette = sns.color_palette("pastel"))
plt.title('Reason of Infection', fontsize = 15)
plt.show()