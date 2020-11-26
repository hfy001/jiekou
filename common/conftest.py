import  pytest
from _pytest import runner
from common import login

@pytest.fixture()
def loginssid():
    aa=login.login1
    return aa()
