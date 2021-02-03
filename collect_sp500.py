#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script for gathering the historical data of the S&P500 index

Description of steps:
- Retrieve data using pandas datareader
- Calculate daily return from data
- Drop useless data points
- Save to feather format
"""
__author__ = 'Dylan Van Parys'
__copyright__ = 'Copyright 2020'
__license__ = 'MIT'

import datetime

import pandas as pd
import pandas_datareader.data as pdr

end = datetime.datetime.today()
start = datetime.datetime(end.year - 10, end.month, end.day, 0, 0, 0)
df = pdr.DataReader(['sp500'], 'fred', start, end)

df['sp500'] = df['sp500']/100

df['daily_return'] = (df['sp500']/ df['sp500'].shift(1))

df = df.dropna()

df = df.reset_index()
df = df.rename(columns={'sp500' : 'market'})
df.to_feather('S&P500_daily_performance.ftr')

#print(df['market'][9])

