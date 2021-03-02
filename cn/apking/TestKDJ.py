# -*- coding: utf-8 -*-
import os, sys
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib

code = '000300'

df = ts.get_k_data(code, index=True,  start='2001-02-01', end='2021-03-02')

kdj(df,9,3,3)

def kdj(df,n,m1,m2):
    for i in range(len(df)):
        if i < n-1: continue
        df.ix[i, 'rsv'] = (df.close.values[i]-df.low.values[i-n+1:i+1].min()) / (df.high.values[i-n+1:i+1].max()-df.low.values[i-n+1:i+1].min())*100
        df = getSMA(df,m1,1,'rsv','K')
        df = getSMA(df,m2,1,'K','D')
    for i in range(len(df)):
    df.ix[i, 'J'] = 3*df.K.values[i] - 2*df.D.values[i]
    return df

def getMA(df,n):
    for i in range(len(df)):
        if i >= n:
            df.ix[i,'ma'] = df.close.values[i-n:i].mean()
    return df

def getEMA(df,n):
    for i in range(len(df)):
        if i==0:
            df.ix[i,'ema']=df.ix[i,'close']
        if i>0:
            df.ix[i,'ema']=(1-n)*df.ix[i-1,'close']+n*df.ix[i,'close']
    return df

def getSMA(df,n,m):
    for i in range(len(df)):
        if i==0：
            df.ix[i,'sma'] = df.ix[i,'close']*m/n
        else:
            df.ix[i,'sma'] = [df.ix[i,'close']*m + (n-m)*df.ix[i-1,'sma']]/n
    return df

def getDMA(df,m):
    for i in range(len(df)):
        if i == 0:
            df.ix[i,'dma'] = df.ix[i,'close']/m
        else:
            df.ix[i,'dma'] = df.ix[i,'close']/m + (1-m)*df.ix[i-1,'dma']
    return df

def getTMA(df,n,m):
    for i in range(len(df)):
        if i==0：
            df.ix[i,'sma'] = df.ix[i,'close']*m
        else:
            df.ix[i,'sma'] = df.ix[i,'close']*m + df.ix[i-1,'sma']*n
    return df

def getWMA(df,n):
    weight = 0
    for i in range(n):
        weight += i
    for i in range(len(df)):
        if i >= n:
            sum = 0
            for j in range(n):
                 sum += (j+1)*df.ix[i-n+j,'close']
            df.ix[i,'wma'] = sum/weight