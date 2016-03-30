stream = [10,20,11,70,50,40,100,5]

from heapq import heappop,heappush


class TopK(object):
    def __init__(self, k):
        self.k = k
        self.topK = []
        self.currLen = 0



    def addOne(self, val):
        self.currLen += 1
        if self.currLen < self.k:
            heappush(self.topK, -val)
        else:
            heappop(self.topK)
            self.currLen -= 1
            heappush(self.topK, -val)

    def getTopK(self):
        return self.topK

t = TopK(5)
for i in stream:
    t.addOne(i)
    print t.getTopK()
