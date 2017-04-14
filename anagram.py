def anagram(s1,s2):

    # Solution 1

    count = {}

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()


    if len(s1) != len(s2):
        return False

        for letter in s1:
            if letter in count:
                count[letter] += 1
            else:
                letter[count] = 1

        for letter in s2:
            if letter in count:
                count[letter] -= 1
            else:
                letter[count] = 1

    for num in count.values():
        if num > 0:
            return False

    return True

    # for i in range(len(lst1)):
    #     if lst1[i] not in lst2:
    #         return False
    #     else:
    #         return True


    # Solution 2

    # s1 = s1.replace(' ', '').lower()
    # s2 = s2.replace(' ', '').lower()

    # return sorted(s1) == sorted(s2)



anagram('clint eastwood','old west action')