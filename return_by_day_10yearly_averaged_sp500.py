#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulation of dollar cost averaging advantage for S&P500 data over 10 year intervals sampled from the historical data
"""
__author__ = 'Dylan Van Parys'
__copyright__ = 'Copyright 2020'
__license__ = 'MIT'

import copy

import pandas as pd
import numpy as np
import datetime
from tqdm import tqdm

import collect_sp500
from simulation import *
from graphs import *

df = collect_sp500.df
min = df['DATE'][0]
possible_start_dates = [min + datetime.timedelta(days = i) for i in range(int(365.5*2))]
number_of_intervals = int(100*round(int(len(possible_start_dates)/4)/100))
intervals = np.random.choice(possible_start_dates, number_of_intervals)


days = ['0' + str(i) for i in range(1, 10)]
days += [str(i) for i in range(10, 29)]
average_return_by_day = {}
years = 10

for day in days:
    average_return_by_day[int(day)] = []
for start_date in tqdm(intervals):
    DF = copy.deepcopy(df)
    DF = DF[(DF['DATE'] >= start_date)]
    DF = DF.reset_index()
    end_date = (start_date + datetime.timedelta(days = int(365*years)))
    DF = DF[(DF['DATE'] < end_date)]
    DF = DF.reset_index()
    for day in days:
        average_return_by_day[int(day)].append(run_DCA_static(DF, day))

for day in days:
    average_return_by_day[int(day)] = np.mean(average_return_by_day[int(day)])

data = {'Average 8 year return': list(average_return_by_day.values()), 'Day of the month':list(average_return_by_day.keys())}

gdata = pd.DataFrame(data)
graph_barplot(gdata, yn='Average 8 year return', xn='Day of the month', title = str(years)+' year ROI for each day of the month averaged out over '+str(number_of_intervals)+' runs')



