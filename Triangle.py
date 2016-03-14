class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return triangle
        
        sums = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            for j in xrange(len(triangle[i])):
                sums[j] += triangle[i][j] + min(sums[j], sums[j+1])
        print sums
        return sums[0]

a = Solution()
print a.minimumTotal([[1],[2,3]])
print a.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
print a.minimumTotal([[-1],[-2,-3]])