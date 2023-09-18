from lib.greet import *

def test_greet_hello_name():
    result = greet("Ben")
    assert result == "Hello, Ben!"