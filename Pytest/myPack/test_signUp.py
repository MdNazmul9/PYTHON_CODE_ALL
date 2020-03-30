#pytest -v -s test_loging.pycls
#pytest -v -s D:\PyCode\Pytest\myPack
#pytest -v -s test_loging.py::test_loggingByFacebook

import pytest

@pytest.yield_fixture()
def setup():
    print("Run before signup test method")
    yield
    print("Run after signup test method")

def test_signupgByFacebook(setup):
    print("This is test signupg by facebook")

def test_signupByGmail(setup):
    print("This is test signupg by gmail")