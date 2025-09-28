import pytest
from data import  find_first_unique_char

def test_first_unique_char():
    assert find_first_unique_char("abbbccdf") == "a"

def test2_first_unique_char():
    assert find_first_unique_char("aabbcdeeff") == "c"

def test3_first_unique_char():
    assert find_first_unique_char("aabbcc") is None


