# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:24:20 2023

@author: ianri
"""

import pandas as pd
import pickle

import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.available[:20]
plt.style.use('seaborn')

YT = pd.read_csv('Bananas.csv')

YT['Bananas price per lb'].describe().apply("{0:.2f}".format)
YT['Date Sold']=pd.to_datetime(YT['DATE'], infer_datetime_format=True)

plt.scatter(YT['Date Sold'],YT['Bananas price per lb'], label='Banana Prices in US', color='orange', marker="^")
plt.ylabel('Price Per Pound, Bananas')
plt.xlabel('Date Sold')
plt.axis(1/1/2019, 12/1/2022, 0.56, 0.65)
plt.legend(loc='upper right', shadow = 'True', fontsize = 'large' )
