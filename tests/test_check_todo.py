from lib.check_todo import *

def test_check_todo():
    result = check_todo('TODO: Take dogs out for walk')
    assert result == True