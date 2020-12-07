#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script for gathering the historical data of the S&P500 index

Description of steps:
- Retrieve html page using pandas
- Select correct table
- Drop useless information
- Save to feather format
"""
__author__ = 'Dylan Van Parys'
__copyright__ = 'Copyright 2020'
__license__ = 'MIT'

import pandas as pd

sp500 = pd.read_html('https://en.wikipedia.org/wiki/S%26P_500_Index')
df = None
for t in sp500:
    if 'Change in Index' in t.columns:
        df = t
        break

df = df[['Change in Index', 'Year']]
#DETERMINE THE USEFUL ROWS: the ones containing the yearly return
mask = df['Year'].map(lambda s:s.isnumeric())

df = df[mask]
print(df)
#CONVERT THE PERCENTAGES TO USEFUL DECIMALS
def tryconvert(s):
    """ Function to fix incompatible '-' sign from html read in table"""
    try:
        return float(s)
    except:
        return float('-'+s[1::])
df['Change in Index'] = df['Change in Index'].apply(lambda s:s[:-1])
df['Change in Index'] = df['Change in Index'].apply(lambda s:tryconvert(s))
df['Change in Index'] = df['Change in Index'].apply(lambda s:float(s)/100)

print(df)
#WRITE TO FEATHER FILE
df.to_feather('S&P500_yearly_performance.ftr')