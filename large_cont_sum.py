

def large_cont_sum(arr):
    result = 0
    end_index = None
    j = -1

    if len(arr) <= 2:
        return max(arr)

    while arr[j] < 0:
        j -= 1

    for i in range(len(arr) + j + 1):

        result += arr[i]
    return result

large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) #29