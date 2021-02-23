import tushare as ts

import cn.apking.config as config

ts.set_token(config.token)
pro = ts.pro_api()

# wanke = ts.get_k_data('000002', start='2016-01-01', end='2019-01-31')
# print(wanke)

# df = pro.new_share(start_date='20210210', end_date='20210220')
# print(df)


from sqlalchemy import create_engine
import tushare as ts

df = ts.get_tick_data('600848', date='2014-12-22')
engine = create_engine('mysql://root:root@127.0.0.1/db_name?charset=utf8')

#存入数据库
df.to_sql(df,engine)

#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')
