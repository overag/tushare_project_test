import pandas as pd
from sqlalchemy import create_engine
# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
engine = create_engine('mysql+pymysql://root:root@localhost:3306/datashare')


# 新建pandas中的DataFrame, 只有id,num两列
df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})
# 将新建的DataFrame储存为MySQL中的数据表，储存index列
df.to_sql('fff', engine, index=False, if_exists='replace')
print('Read from and write to Mysql table successfully!')


# 查询语句，选出employee表中的所有数据
sql = ''' select * from fff; '''
# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql, engine)
# 输出employee表的查询结果
print(df)