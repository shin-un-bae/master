import pandas as pd
import pyodbc
from openpyxl import Workbook
conn  = pyodbc.connect(  
        driver='{iSeries Access ODBC Driver}',
        system='192.168.1.3',      
        uid='woosung',
        pwd='kingstar')
try:
     
    code_gub =input("코드구분을 입력하세요>>")
    sql = "SELECT CCODE,CDESC1 FROM comlib.wmcode where ctype=? and ccode>'' "
    df = pd.read_sql(sql, conn, params=[code_gub])

    df.to_excel("db2_data.xlsx", \
        sheet_name='test_sheet_1',\
        header=None,\
        index=False)
except pyodbc.Error as e:
    print("Error:", e)

finally:
    # 연결 종료
    if conn:
        conn.close()