class Node(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

def reverse(head):

    while head.nextnode != None:
        head = head.nextnode

    print head.value
    print head.nextnode.value