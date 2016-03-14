class Solution(object):
    def combine(self, n, k, start=1):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[x,] for x in xrange(start, n+1)]
        result = []
        for firstNum in xrange(start, n-k+2):
            for comb in self.combine(n, k-1, firstNum+1):
                result.append([firstNum,]+comb)
        return result

a = Solution()
print a.combine(8,4)