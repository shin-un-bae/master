import pandas as pd
import pyodbc
from openpyxl import Workbook
conn = pyodbc.connect(  
        driver='{iSeries Access ODBC Driver}',
        system='192.168.1.3',      
        uid='woosung',
        pwd='kingstar')

sql = "SELECT CCODE,CDESC1 FROM comlib.wmcode where ctype='11' and ccode>'' "
df = pd.read_sql(sql, conn)

df.to_excel("db2_data.xlsx", \
            sheet_name='test_sheet_1',\
            header=None,\
            index=False)

conn.close()