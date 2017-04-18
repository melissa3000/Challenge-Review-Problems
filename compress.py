

def compress(s):
    d = {}

    for letter in s:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    result = ''

    for key, value in d.items():
        result += key + str(value)

    print result


    #Solution 2
    # r = ''

    # if len(s) == 0:
    #     return ''

    # if len(s) == 1:
    #     return s + '1'

    # last = s[0]
    # count = 1
    # i = 1

    # while i < len(s):
    #     if s[i] == s[i - 1]:
    #         count += 1
    #     else:
    #         r = r + s[i-1] + str(count)
    #         count = 1

    #     i += 1

    # r = r + s[i-1] + str(count)
    # return r

compress('AAAAABBBBCCCC') #'A5B4C4'
compress('AABBCC') # 'A2B2C2'