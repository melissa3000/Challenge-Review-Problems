def is_unique(str):
    seen = {}
    for letter in str:
        if letter in seen:
            return False
        else:
            seen[letter] = 1

    return True

is_unique("aboout")