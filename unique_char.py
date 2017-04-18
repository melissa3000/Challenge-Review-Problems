

def uni_char(s):
    char_set = set()

    for letter in s:
        char_set.add(letter)

    if len(s) != len(char_set):
        print False
    else:
        print True


uni_char('abedfgh') # T
uni_char('abbcdef') # F