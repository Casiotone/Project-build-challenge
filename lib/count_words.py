

def count_words(string):
    # remove spaces from start and end of string
    string = string.strip()
    # initialise count from 1 because there is no space at last
    count = 1
    # interate string
    for i in string:
        # if space is encountered increment 1
        if i==' ':
            count+= 1

    return count
