#pytest -v -s test_loging.pycls
#pytest -v -s D:\PyCode\Pytest\myPack
#pytest -v -s test_loging.py::test_loggingByFacebook

import pytest
@pytest.yield_fixture()
def setup():
    print("Run before loging test method")
    yield
    print("Run after loging test method")

def test_loggingByFacebook(setup):
    print("This is test loging by facebook")

def test_LoggingByGmail(setup):
    print("This is test logging by gmail")