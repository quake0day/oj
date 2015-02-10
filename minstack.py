class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.A = []
        self.min_stack = []

    def push(self, number):
        # write yout code here
        self.A.append(number)
        if len(self.min_stack) != 0: 
            if self.min_stack[-1] >= number:
                self.min_stack.append(number)
        else:
            self.min_stack.append(number)


    def pop(self):
        # pop and return the top item in stack
        res = self.A.pop()
        if res == self.min_stack[-1]:
            self.min_stack.pop()
        return res

    def min(self):
        # return the minimum number in stack
        return self.min_stack[-1]
