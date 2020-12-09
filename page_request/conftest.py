import  pytest
from _pytest import runner
from common import login
'''
# 对应源码
def pytest_runtest_makereport(item, call):
    """ return a :py:class:`_pytest.runner.TestReport` object
    for the given :py:class:`pytest.Item` and
    :py:class:`_pytest.runner.CallInfo`.
    """
'''




# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     print('------------------------------------')
#
#     # 获取钩子方法的调用结果
#     out = yield
#     # print('用例执行结果', out)
#
#     # 3. 从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#     if report.when == "call":
#         print('测试报告：%s' % report)
#         print('步骤：%s' % report.when)
#         print('nodeid：%s' % report.nodeid)
#         print('描述:%s' % str(item.function.__doc__))
#         print(('运行结果: %s' % report.outcome))
#
# @pytest.fixture(scope="session", autouse=True)
# def fix_a():
#     print("setup 前置操作")
#     yield
#     print("teardown 后置操作")





@pytest.fixture()
def loginssid():
    aa=login.Login1
    return aa()

