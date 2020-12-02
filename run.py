import pytest
import os


if __name__ == '__main__':
    pytest.main(["-s","-q",
                 "--alluredir", "./allure-results"])
    # os.system(r"allure generate --clean allure-results -o allure-report")
    # pytest.main(["test_case/test_log.py"])
    # pytest.main(['-s', '-q', '--alluredir', './report/xml'])