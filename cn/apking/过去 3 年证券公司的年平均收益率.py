import math

import baostock as bs
import matplotlib.pyplot as plt
import pandas as pd


def get_closeprice(code):
    #### 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节
    rs_open = bs.query_history_k_data(code, "open", start_date='2015-01-05', end_date='2015-01-05',
                                      frequency="d", adjustflag="1")

    data_list = []
    while (rs_open.error_code == '0') & rs_open.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs_open.get_row_data())
    result_open = pd.DataFrame(data_list, columns=rs_open.fields, index=[code])

    rs_close = bs.query_history_k_data(code, "close", start_date='2017-12-29', end_date='2017-12-29',
                                       frequency="d", adjustflag="1")

    data_list = []
    while (rs_close.error_code == '0') & rs_close.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs_close.get_row_data())
    result_close = pd.DataFrame(data_list, columns=rs_close.fields, index=[code])

    result = result_open.join(result_close)
    return result


def compute_Avg_EarningRate():
    # 登陆系统
    lg = bs.login()

    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    # 获取全部证券基本资料
    rs = bs.query_stock_basic()
    result = pd.DataFrame()
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        code = rs.get_row_data()[0]
        df = get_closeprice(code)
        if result.empty:
            result = df
        else:
            result = result.append(df)
    result = result[result['open'] != '']
    result['open'] = result['open'].astype(float)
    result['close'] = result['close'].astype(float)
    result['avgEarningRate'] = (result['close'] / result['open']).apply(lambda x: math.pow(x, 1 / 3) - 1)
    result = result.sort_values(by=['avgEarningRate'], ascending=False)
    result.to_csv("D:\\Avg_Earning_Rate_data.csv", encoding="gbk", index=False)

    result[:10]['avgEarningRate'].plot(title='Avg Earning Rate', kind='bar')
    plt.show()
    # 登出系统
    bs.logout()


if __name__ == '__main__':
    compute_Avg_EarningRate()