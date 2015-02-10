class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        n = len(self.stack1)
        for i in xrange(n):
            temp = self.stack1.pop()
            self.stack2.append(temp)
        top = self.stack2[-1]
        for i in xrange(n):
            temp = self.stack2.pop()
            self.stack1.append(temp)
        return top


    def pop(self):
        # write your code here
        # pop and return the top element
        n = len(self.stack1)
        for i in xrange(n):
            temp = self.stack1.pop()
            self.stack2.append(temp)
        res = self.stack2.pop()
        for i in xrange(n-1):
            temp = self.stack2.pop()
            self.stack1.append(temp)
        return res

