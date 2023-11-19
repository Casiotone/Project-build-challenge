from lib.count_words import * 

def test_count_and_return_words_in_string():
    result = count_words('This is a string')
    assert result == 4