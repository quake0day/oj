x = iter([1,3,5,7,9])
y = iter([2,4,6,8,10])

print x.next()
print y.next()

class Combine():
    def __init__(self):
        self.x = iter([1,3,5,7,9])
        self.y = iter([2,4,6,8,10])
        self.flag = True


    def Next(self):
        if self.flag:
            self.flag = False
            return self.x.next()
        else:
            self.flag = True
            return self.y.next()


a = Combine()
print a.Next()
print a.Next()
print a.Next()
print a.Next()