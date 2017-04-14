
def pair_sum(arr,k):

    # solution 1

    # pair = []

    # for num in arr:
    #     pr = k - num
    #     if pr in arr:
    #         pair.append((num, pr))

    # if pair == []:
    #     return False

    # print len(pair) / 2


    # solution 2

    if len(arr) < 2:
        return

    seen = set()
    result = set()

    for num in arr:
        pr = k - num

        if pr not in seen:
            seen.add(num)
        else:
            result.add((num, pr))

    return len(result)


pair_sum([1,3,2,2],4)
pair_sum([1, 3, 2, 2], 5)