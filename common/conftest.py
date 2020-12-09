import pytest
from common import login


@pytest.fixture()
def loginssid():
    login_sid = login.Login1
    return login_sid()
