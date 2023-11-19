# Takes string and returns first 5 words and 'a' if there are more than that

from lib.personal_diary import *

def test_make_snippet():
    result = make_snippet('Go to the dog shelter and adopt another dog')
    assert result == 'Go to the dog shelter a'