import pytest
from lib.password_checker import *

def test_password_checker():
    checker = PasswordChecker()
    check1 = checker.check("12345678")
    assert check1 == True
    with pytest.raises(Exception) as e:
        checker.check("123")
    assert str(e.value) == "Invalid password, must be 8+ characters."