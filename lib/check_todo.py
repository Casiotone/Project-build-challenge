# As a user
#So that I can keep track of my tasks
# I want to check if a text includes the string #TOD O.

# Function signature
# Method name - check_todo
# Parameters - text_string
# Return Boolean

def check_todo(text_string):
    if 'TODO' or 'todo' in text_string:
        return True 