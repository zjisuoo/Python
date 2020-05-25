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

# 성별 확진자 수 / 자가격리, 자가격리 해제, 사망자 수
plt.figure(figsize = (12, 7))
sns.countplot(patient.sex, palette = sns.color_palette('pastel'), hue = patient.state)
plt.title('Confirmed number by Gender', fontsize = 15)
plt.show()
