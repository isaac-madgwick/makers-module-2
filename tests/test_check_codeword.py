from lib.check_codeword import *

def test_check_codeword():
    first = check_codeword("horse")
    second = check_codeword("hOrsE")
    third = check_codeword("hrose")
    forth = check_codeword("sjdsaf")

    assert first == "Correct! Come in."
    assert second == "WRONG!"
    assert third == "Close, but nope."
    assert forth == "WRONG!"