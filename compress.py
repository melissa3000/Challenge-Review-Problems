

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


compress('AAAAABBBBCCCC') #'A5B4C4'
compress('AABBCC') # 'A2B2C2'