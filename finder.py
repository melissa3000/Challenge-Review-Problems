

def finder(arr1, arr2):
    number_dict = {}

    for num in arr2:
        if num not in number_dict:
            number_dict[num] = 1
        else:
            number_dict[num] += 1

    for num in arr1:
        if num not in number_dict:
            return num





    # O(n ^2) solution
    # for i in range(len(arr1)):
    #     if arr1[i] not in arr2:
    #         print arr1[i]

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]) #5
finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]) #6
finder([5,5,7,7],[5,7,7]) #5