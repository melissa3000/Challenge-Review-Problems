class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def nth_to_last_node(n, head):

    left_pointer = head
    right_pointer = head

    # move the right pointer n places from the head
    for i in xrange(n-1):
        right_pointer = right_pointer.nextnode

    # while there is a next node to the right, move the search block down the list one node at a time
    while right_pointer.nextnode:
        right_pointer = right_pointer.nextnode
        left_pointer = left_pointer.nextnode

    # return left pointer when you reach the end of the list (when right pointer next node is None)
    return left_pointer







