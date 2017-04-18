

def balance_check(s):

    if len(s) % 2 != 0:
        return False


    open = set("[{(")

    pairs = set([ ('(',')'), ('[',']'), ('{','}') ])

    lst_open = []


    for item in s:
        if item in open:
            lst_open.append(item)

        else:
            if len(lst_open) == 0:
                return False

            last_open = lst_open.pop()

            if (last_open, item) not in pairs:
                return False

    return len(lst_open) == 0










balance_check('[](){([[[]]])}') # True
# balance_check('()(){]}') # False