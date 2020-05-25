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

# 검사 결과 / 검사 횟수, 양성, 음성
time_series = time_series.set_index('date')

sns.set(style = 'whitegrid')
fig, ax = plt.subplots(figsize = (16, 7))
ax.plot(time_series['test'], label = 'test', linestyle = 'dashed', color = '#FFC300', linewidth = 3, markersize = 6)
ax.plot(time_series['negative'], label = 'negative', linestyle = 'dotted', color = '#B6FF33', linewidth = 3, markersize = 6)
ax.plot(time_series['confirmed'], label = 'confirmed', color = '#FF5733', linewidth = 4, markersize = 6)
plt.title("Number of Checks and Confirmed Discriminations", fontsize = 16)

ax.set_xticklabels(time_series.index, rotation = 45, fontsize = 5)
plt.xlabel('Date', fontsize = 16)
plt.ylabel('Number of Check', fontsize = 16)
plt.legend(loc = 'upper left', fontsize = 15, fancybox = True, ncol = 3, shadow = True)
plt.show()