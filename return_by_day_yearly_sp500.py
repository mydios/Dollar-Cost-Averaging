#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulation of dollar cost averaging investment in S&P500 for years 2011-2019, checking every possible day of the month as possible investment day for the monthly investment
"""
__author__ = 'Dylan Van Parys'
__copyright__ = 'Copyright 2020'
__license__ = 'MIT'

import copy

import pandas as pd
from graphs import *
from simulation import *

days = ['0' + str(i) for i in range(1, 10)]
days += [str(i) for i in range(10, 29)]

returns = {}
for i in range(1,10):
    returns['201'+str(i)] = []

df = pd.read_feather('S&P500_daily_performance.ftr')
for i in range(1,10): 
    f = lambda d : ('201'+str(i)) in str(d)
    DF = copy.deepcopy(df) 
    DF = DF[DF['DATE'].apply(f)]
    for day in days:
        returns['201'+str(i)].append(run_DCA_static(DF, day, 50000))
days = list(map(lambda s : int(s), days))


for y in returns.keys():
    data = {'1 year return':returns[y], 'day of the month':days}
    graph_barplot(pd.DataFrame(data), xn = 'day of the month', yn = '1 year return', title = y)
