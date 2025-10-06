from lib.report_length import *

def test_report_length():
    first = report_length("")
    second = report_length("asdfghjklzxcvbnmqwertyuiop")
    third = report_length(" ")

    assert first == "This string was 0 characters long."
    assert second == "This string was 26 characters long."
    assert third == "This string was 1 characters long."