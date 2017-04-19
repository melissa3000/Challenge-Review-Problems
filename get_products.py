# given a list of int
#for each index, find the product of every integer except the one at that index
#return a list of the products
#[1, 7, 3, 4] ==> [84, 12, 28, 21]

def get_products_of_all_ints_except_at_index(lst):

    # skip = 0
    # prod = 1
    # result = []
    # i = 0

    # while i in range(len(lst)):

    #     if i == skip:
    #         i += 1
    #     else:
    #         prod = lst[i] * prod
    #         i += 1
    #         skip += 1

    #     print prod

    if len(lst) < 2:
        raise IndexError("List must include more than two numbers")

    products_of_all_ints_except_at_index = [None] * len(lst)

    # for each int, we find the product of all the ints before it, storing
    # the total product so far each time
    product_so_far = 1
    i = 0
    while i < len(lst):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= lst[i]
        i += 1

    # for each int, we find the product of all the ints after it.
    # Since each index in the products already has the product of all
    # the ints before it, now we're storing the total product of all other ints.

    product_so_far = 1
    i = len(lst) - 1
    while i >= 0:
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= lst[i]
        i -= 1

    return get_products_of_all_ints_except_at_index

get_products_of_all_ints_except_at_index([1, 7, 3, 4])


