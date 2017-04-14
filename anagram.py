def anagram(s1,s2):

    # Solution 1

    # s1 = s1.lower()
    # s2 = s2.lower()

    # s1 = s1.replace(' ', '')
    # s2 = s2.replace(' ', '')

    # lst1 = list(s1)
    # lst2 = list(s2)


    # if len(s1) != len(s2):
    #     return False

    # for i in range(len(lst1)):
    #     if lst1[i] not in lst2:
    #         return False
    #     else:
    #         return True


    # Solution 2

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)



anagram('clint eastwood','old west action')