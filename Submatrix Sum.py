class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        # Write your code here
        m = len(matrix)
        n = len(matrix[0])
        to_top = [[ 0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                to_top[i][j] = to_top[i-1][j] + matrix[i-1][j-1]
        print to_top
        for up in xrange(m):
            for down in xrange(up, m):
                h = {}
                s = 0
                h[s] = -1
                for j in xrange(n):
                    s += to_top[down+1][j+1] - to_top[up][j+1]
                    print h
                    if s in h:
                        print s
                        print h
                    h[s] = j
        return [[-1,-1],[-1,-1]]
        


a = Solution()
print a.submatrixSum([
        [1, 5, 7],
        [3, 7, -8],
        [4, -8, 9],
    ])
