# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

# solution 1
def remove_char(s):
    # function that removes the first and last characters of a string
    return s[1: -1]

    # solution 2
    def remove_char(s)
    return '' if len(s) <= 2 else s[1: -1]

    # solution 3
    def remove_char(s)
    return s[1:len(s)-1]
    
    # solution 4
    def remove_char(s)
    remove_char= lambda s: s[1: -1]

     # solution 5
    def remove_char(s)
    if len(s) > 2:
        return s[1: -1]
    else:
        return ''