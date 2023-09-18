from lib.check_codeword import *

"""
if the code word is correct 
returns "Correct! Come in."
"""
def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

"""
if the code word is wrong
returns "WRONG!"
"""
def test_with_wrong_codeword():
    result = check_codeword("water")
    assert result == "WRONG!"

"""
if code word has first and last letter right
returns "Close, but nope."
"""
def test_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

"""
if first letter right but last letter wrong
returns "WRONG!"
"""
def test_with_right_first_letter_codeword():
    result = check_codeword("hat")
    assert result == "WRONG!"

"""
if first letter wrong but last letter right
returns "WRONG!"
"""
def test_with_right_last_letter_codeword():
    result = check_codeword("rice")
    assert result == "WRONG!"
