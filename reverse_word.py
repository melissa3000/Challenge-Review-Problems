

def rev_word(s):
    #Solution 1
    result = ''

    #remove trailing spaces and convert s to list
    s_new = s.rstrip().lstrip()

    word_list = s_new.split()

    backwards = word_list[-1::-1]
    for word in backwards:
        result += word + " "
    print result



    #Solution 2

    # words = []
    # spaces = [' ']

    # i = 0

    # while i < len(s):
    #     if s[i] not in spaces:
    #         word_start = i
    #         while i < len(s) and s[i] not in spaces:
    #             i += 1
    #         words.append(s[word_start:i])
    #     i += 1
    # print " ".join(reversed(words))


rev_word('Hi John,   are you ready to go?') #'go? to ready you are John, Hi'
rev_word('    space before') #'before space'