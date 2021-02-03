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

def graph_lineplot(df, xn=None, yn=None):
    seaborn.lineplot(data = df, x=xn, y=yn)
    plt.show()

def graph_barplot(df, xn=None, yn=None, ylim=None, title=None):
    seaborn.barplot(data = df, x=xn, y=yn)
    if ylim is not None:
        plt.ylim(ylim)
    if title is not None:
        plt.title(title)
    plt.show()
