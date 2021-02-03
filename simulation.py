#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulation of dollar cost averaging advantage
"""
__author__ = 'Dylan Van Parys'
__copyright__ = 'Copyright 2020'
__license__ = 'MIT'

from os import error
import pandas as pd
import numpy as np
import datetime

def run_DCA_static(df, day, monthly_investment = 500, start = 0):
    """
    Runs a simulation of a monthly investment on the same day each month using the market data provided

    Input:
        df : Pandas DataFrame, market day 
            - column 'DATE' : dates of format '1970-01-01 00:00:00'
            - column 'daily_return : floats indicating the return of that day
            - column 'market' : floats indicating the market price of the product that date
        day : str, which day of the month to invest on in format '0X'/'XX'
        monthly_investment : float, amount to be invested each month
        start : float, starting asset value

    Output:
        float : compound ROI value
    """
    if type(day) is not str:
        raise error("Wrong type for argument 'day', expected " + str(type("")) + " but got "+str(type(day)) +" instead")

    returns = np.array(df['daily_return'])

    monthly_investment = np.zeros(len(returns)) + monthly_investment

    investment_days = np.array( list( map( lambda date : (str(date).split(' ')[0][-2::]) == day , df['DATE'] ) ) )
    investments = investment_days * monthly_investment
    total_investment = sum(investments)
    leftover = 0
    for i in range(len(investments)):
        if investments[i]>0:
            shares = (investments[i] + leftover)/df['market'][i]
            to_buy = np.floor(shares)
            leftover = (investments[i] + leftover)*(shares-to_buy)/shares
            investments[i] = df['market'][i]*to_buy
    
    value_invested_capital = start
    for i in range(len(returns)):
        value_invested_capital *= returns[i]
        value_invested_capital += investments[i]
    
    assert(sum(investments) <= total_investment)
    assert(sum(investments) > 0)

    return value_invested_capital/sum(investments)

def run_DCA_dynamic(df, investment_days, monthly_investment = 500, start = 0):
    """
    Runs a simulation of a monthly investment on certain days using provided market data

    Input:
        df : Pandas DataFrame, market data 
            - column 'DATE' : dates of format '1970-01-01 00:00:00'
            - column 'daily_return : floats indicating the return of that day
            - column 'market' : floats indicating the market price of the product that date
        investment_days : numpy.ndarray, mask with same shape as 'DATE' column indicating which days to invest on 
        monthly_investment : float, amount to be invested each month
        start : float, starting asset value

    Output:
        float : compound ROI value
    """
    returns = np.array(df['daily_return'])

    monthly_investment = np.zeros(len(returns)) + monthly_investment

    investments = investment_days * monthly_investment
    total_investment = sum(investments)
    leftover = 0
    for i in range(len(investments)):
        if investments[i]>0:
            shares = (investments[i] + leftover)/df['market'][i]
            to_buy = np.floor(shares)
            leftover = (investments[i] + leftover)*(shares-to_buy)/shares
            investments[i] = df['market'][i]*to_buy

    value_invested_capital = start
    for i in range(len(returns)):
        value_invested_capital *= returns[i]
        value_invested_capital += investments[i]
    
    assert(sum(investments) <= total_investment)
    assert(sum(investments) > 0)

    return value_invested_capital/sum(investments)









