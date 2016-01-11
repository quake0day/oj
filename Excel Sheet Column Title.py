class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        if n == 0: return res
        alpha = [chr(i) for i in xrange(65, 91)]
        while n > 0:
            t = n % 26
            res+= alpha[t-1]
            n = n / 26
            if t == 0:
                n -= 1
        return res[::-1]

a = Solution()
print a.convertToTitle(26)
