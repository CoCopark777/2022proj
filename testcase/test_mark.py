import pytest
import time

from common.common_util import CommonUtil
from common import conf
from common import read_excel


class TestCeshi(CommonUtil):
    time_age = 8

    @pytest.mark.smoke
    def test_demo1(self):
        print("测试第一条用例test_demo1")
        raise Exception("这条用例挂了")

    @pytest.mark.smoke
    def test_smoke(self):
        print("test_smoke")

    def test_demo2(self, exe_database_sql):
        print("测试第二条用例test_demo2"+ exe_database_sql)

    @pytest.mark.parametrize('caseinfo', read_excel.read_excel_dict(conf.TEST_DATA_PATH, "adminLogin"))
    def test_mark3(self, caseinfo):
        print("caseinfo['id']:{}".format(caseinfo['id']))

    @pytest.mark.skip(reason="无理由跳过")
    def test_demo3(self):
        print("测试第三条用例test_demo3")

    @pytest.mark.skipif(time_age < 10, reason="年龄小于10跳过")
    def test_demo4(self):
        print("测试第四条用例")

    def test_demo5(self):
        print("测试第五条用例")


if __name__ == '__main__':
    pytest.main(["-vs"])
