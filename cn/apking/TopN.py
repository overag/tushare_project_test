import tushare as ts
import cn.apking.config as config

ts.set_token(config.token)


pro = ts.pro_api()

df = pro.top10_holders(ts_code='600000.SH', start_date='20200901', end_date='20210302')

print(df)

df = pro.top10_floatholders(ts_code='600000.SH', start_date='20200901', end_date='20210302')
print(df)

