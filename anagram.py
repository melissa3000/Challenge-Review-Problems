def anagram(s1,s2):

    dict = {}

    s1 = s1.lower()
    s2 = s2.lower()

    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

    lst1 = list(s1)
    lst2 = list(s2)


    if len(s1) != len(s2):
        return False

    for i in range(len(lst1)):
        if lst1[i] not in lst2:
            return False
        else:
            return True


anagram('clint eastwood','old west action')