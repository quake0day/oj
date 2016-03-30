class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        todo = "1"
        while n > 0:
            count = 1
            prev = todo[0]
            res = ""
            for k in xrange(1,len(todo)):
                if todo[k] == prev:
                    count += 1
                    prev = todo[k]
                else:
                    res += str(count) + prev
                    prev = todo[k]
            res += str(count) + prev
            todo = res
            n -= 1
        return res
            
a = Solution()
print a.countAndSay(20)