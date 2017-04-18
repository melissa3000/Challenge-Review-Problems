

def uni_char(s):
    char_set = set()

    for letter in s:
        char_set.add(letter)

    if len(s) != len(char_set):
        return False
    else:
        return True


    # optimized:
    # return len(set(s)) == len(s)




uni_char('abedfgh') # T
uni_char('abbcdef') # F