class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    # def enqueue(self,element):

    #     # FILL OUT CODE HERE
    #     return self.stack1.append(element)

    # def dequeue(self):

    #     # FILL OUT CODE HERE
    #     return self.stack1.pop(0)



    #Solution 2 - treating the stacks as stacks and not as python lists
    def enqueue(self,element):

        # FILL OUT CODE HERE
        self.stack1.append(element)

    def dequeue(self):

        # FILL OUT CODE HERE
        if not self.stack2:
            while self.stack1:
                #add items to stack2 in reverse order
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()



