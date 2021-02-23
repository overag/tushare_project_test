import pandas as pd
from sqlalchemy import create_engine

import cn.apking.config as config

# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:root, 端口：3306,数据库：datashare
engine = create_engine('mysql+pymysql://root:root@localhost:3306/datashare')
# 方法一：默认读取第一个表单
df = pd.read_csv(config.DATA_FILE)  # 这个会直接默认读取到这个CSV的第一个表单
# data = df.head()  # 默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))  # 格式化输出
df.to_sql('history_k_data', engine, index=False, if_exists='replace')
print('Read from and write to Mysql table successfully!')




