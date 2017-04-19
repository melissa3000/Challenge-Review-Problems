class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

def reverse(head):

    current = head
    previous = None
    nextnode = None

    while current:
        # copy current node's next node to nextnode variable before overwriting
        nextnode = current.nextnode

        # reverse pointer to the nextnode
        current.nextnode = previous

        # move forward in the list
        previous = current
        current = nextnode

    return previous