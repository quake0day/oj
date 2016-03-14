

stream = [10, 20, 30, 40, 50, 60]

def getAvg(prev, x, n):
    return (prev*n + x) / (n +1)

avg = 0
for i in xrange(6):
    avg = getAvg(avg, stream[i], i)
    print avg



class MiddleFinder:
    def __init__(self):
        self.arr = []
        self.avg = 0

    def addNum(self, num):
        self.arr.append(num)
        self.avg = ((self.avg * (len(self.arr)-1) + num) / (len(self.arr)))



    def findMiddle(self):
        return self.avg


a = MiddleFinder()
a.addNum(10)
print a.findMiddle()
a.addNum(20)
print a.findMiddle()
