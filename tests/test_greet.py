from lib.greet import *

def test_greet():

    greet1 = greet("Tom")
    assert greet1 == "Hello, Tom!"
    greet2 = greet("Jake")
    assert greet2 == "Hello, Jake!"