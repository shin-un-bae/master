import os
import openpyxl
import time
from datetime import datetime

def recursive_search(dir):
    results = []
    filenames = os.listdir(dir)
    for filename in filenames:
        full_path = os.path.join(dir, filename)
        if os.path.isdir(full_path):
            recursive_search(full_path)
        else:
            a_time = os.path.getatime(full_path)
            m_time = os.path.getmtime(full_path)
            a_time_str = datetime.strptime(time.ctime(a_time), "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d %H:%M:%S")
            m_time_str = datetime.strptime(time.ctime(m_time), "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d %H:%M:%S")
            file_size = os.stat(full_path).st_size
            results.append((f"{full_path}", file_size, a_time_str, m_time_str))
    return results

filename = "save_excel.xlsx"
target_dir = "C:\\Users\\ubshin\\drmsys"
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "폴더목록"
results = recursive_search(target_dir)
for r, d in enumerate(results):
    for c, col in enumerate(d):
        sheet.cell(r+1, c+1).value = col

wb.save(filename)
