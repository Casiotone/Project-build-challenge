def grammar_check(text_string):
    if text_string[0].isupper():
        return True
    elif any(char in text_string[-1] for char in '.?!'):
        return True
    else:
        return False
     
