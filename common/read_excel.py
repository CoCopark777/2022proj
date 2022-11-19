"""
读取excel数据

"""

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


def read_excel_dict(file_path, sheet_name):
    # 打开excel
    load_wb = openpyxl.load_workbook(file_path)
    # 读取工作页
    sheet: Worksheet = load_wb[sheet_name]
    # 读表的数据
    rows = list(sheet.values)
    # 取第一行表头
    title = rows[0]
    # 取后面的全部数据
    rows_all = rows[1:]
    # 数据拼接
    new_rows = [dict(zip(title, row))for row in rows_all]
    return new_rows


if __name__ == '__main__':
    from common import conf

    aa = read_excel_dict(conf.TEST_DATA_PATH, "adminLogin")
    print(type(aa),aa)
    print(aa)
