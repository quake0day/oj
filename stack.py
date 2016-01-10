class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        tmp = []
        while (len(self.queue) != 0):
            tmp.append(self.queue[-1])
            self.queue.pop()
        self.queue.append(x)
        print self.queue
        while(len(tmp) != 0):
            self.queue.append(tmp[-1])
            tmp.pop()
        print self.queue

            
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0



a = Stack()
a.push(1)
a.push(2)
a.pop()
print a.top()
