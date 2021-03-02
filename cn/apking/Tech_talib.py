import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import talib

# Pandas打印显示完整行列
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# df = ts.get_k_data('000300', index=True,  start='2001-02-01', end='2021-03-02')
# close = [float(x) for x in df['close']]
# # 调用talib计算指数移动平均线的值
# df['EMA12'] = talib.EMA(np.array(close), timeperiod=6)
# df['EMA26'] = talib.EMA(np.array(close), timeperiod=12)
#  # 调用talib计算MACD指标
# df['MACD'],df['MACDsignal'],df['MACDhist'] = talib.MACD(np.array(close),
#                             fastperiod=6, slowperiod=12, signalperiod=9)
# df.tail(12)
# print(df)

# KDJ指标计算
# 原理：计算N日RSV = （今日收盘 - N日最低）/(N日最高-N日最低) * 100
# K = (1-(1/M1))*前一日K值 + 1/M1 * RSV
# D = (1-(1/M1))*前一日D值 + 1/M1 * K值
# J = 3 * K - 2 * D
def KDJ(symbol, N , M1 , M2 ,end_time):
    '''
    计算KDJ指标公式
    输入： data <- dataframe，需包含开盘、收盘、最高、最低价
          N、M1、M2 <- int
          end_time <- str   结束时间
    输出： 将K、D、J合并到data后的dataframe
    '''

    # 取历史数据，取到上市首日
    data = ts.get_k_data(symbol, index=True,  start='2001-02-01', end='2021-03-02')

    # 计算前N日最低和最高，缺失值用前n日（n<N)最小值替代
    lowList = data['low'].rolling(N).min()
    lowList.fillna(value=data['low'].expanding().min(), inplace=True)
    highList = data['high'].rolling(N).max()
    highList.fillna(value=data['high'].expanding().max(), inplace=True)
    # 计算rsv
    rsv = (data['close'] - lowList) / (highList - lowList) * 100
    # 计算k,d,j
    data['kdj_k'] = rsv.ewm(alpha=1/M1, adjust=False).mean()     # ewm是指数加权函数
    data['kdj_d'] = data['kdj_k'].ewm(alpha=1/M2, adjust=False).mean()
    data['kdj_j'] = 3.0 * data['kdj_k'] - 2.0 * data['kdj_d']
    print(data[-10:])
    return data

# 测试一下
d = KDJ('000300',9,3,3,'2020-12-31')
