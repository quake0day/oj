class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        for n in num:
            bits = 0
            while n:
                bits += n & 1
                n >>= 1
            print bits 


a = Solution()
print a.countBits([i for i in xrange(33)])