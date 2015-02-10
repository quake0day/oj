class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if len(triangle) <= 0:
            return 0

        n = len(triangle) # start from the bottom
        end_triangle = n - 1
        m = len(triangle[end_triangle])
        f = [[0] * n for n in range(1,m+1)]
        print f
        # initalize the last row
        i = 0
        while i < m:
            f[end_triangle][i] = triangle[end_triangle][i]
            i += 1
        for i in xrange(end_triangle - 1,0 - 1,-1):
            for j in xrange(0,i+1):
                f[i][j] = min(f[i+1][j], f[i+1][j+1])+triangle[i][j]

        return f[0][0]



        # state


a = Solution()
print a.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])