"""
测试文件和环境配置路径

"""
import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

# 测试数据路径
TEST_DATA_PATH = os.path.join(BASE_DIR, 'testdata', 'cases.xlsx')

# 测试报告路径
TEST_REPORT_PATH = os.path.join(BASE_DIR, 'reports', 'index.html')
print(TEST_REPORT_PATH)


