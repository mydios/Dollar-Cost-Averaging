#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module containing graphing functions 
"""
__author__ = 'Dylan Van Parys'
__copyright__ = 'Copyright 2020'
__license__ = 'MIT'

import pandas as pd
import seaborn
import matplotlib.pyplot as plt

def graph_SP500_YROI():
    data = pd.read_feather('S&P500_yearly_performance.ftr')
    X = data['Year']
    Y = data['Change in Index']
    seaborn.lineplot(x = X, y = Y)
    plt.xticks(list(range(len(X)))[::5]) 
    plt.show()
