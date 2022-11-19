# 读取数据方法
import pytest

def read_yaml():
    return ['yasuo', 'gailun', 'mangwang']


@pytest.fixture(scope='function',autouse=False)
def exe_database_sql():
    print("执行sql查询")
    yield "success"
    print("关闭数据库连接")
