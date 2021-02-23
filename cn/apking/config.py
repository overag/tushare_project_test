import os

token = '26688436f2ac630d514d480577d9784817a46dc42bc916e7a4ad9bba'
PROJECT_NAME = 'tushare_project_test'
CUR_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = CUR_PATH[:CUR_PATH.find(PROJECT_NAME)+len(PROJECT_NAME+"\\")]  # 获取myProject，也就是项目的根路径
DATA_FILE =ROOT_PATH+"data\history_k_data.csv"


