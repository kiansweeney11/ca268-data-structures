class Queue_Two_Stacks():

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, item):
        self.stack_1.append(item)

    def dequeue(self):
        if len(self.stack_2) == 0:
        # If stack_1 is empty, raise an error
            if len(self.stack_1) == 0:
                raise IndexError("Can't dequeue from empty queue!")
        
        # while stack_1 is not empty, 
        # move items from stack_1 to stack_2, reversing order
            while len(self.stack_1) > 0:
                last_stack_1_item = self.stack_1.pop()
                self.stack_2.append(last_stack_1_item)
        # return the last item in stack_2, which is the first
        # item that entered stack_1 (FIFO!)
        return self.stack_2.pop()
