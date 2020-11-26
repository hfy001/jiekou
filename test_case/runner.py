from _pytest import runner

# 对应源码
def pytest_runtest_makereport(item, call):
    """ return a :py:class:`_pytest.runner.TestReport` object
    for the given :py:class:`pytest.Item` and
    :py:class:`_pytest.runner.CallInfo`.
    """