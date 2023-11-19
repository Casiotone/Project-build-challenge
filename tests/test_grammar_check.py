from lib.grammar_check import *

def test_check_text_starts_with_capital_letter_and_ends_with_punctuation():
    result = grammar_check('This sentence is correct!')
    assert result == True