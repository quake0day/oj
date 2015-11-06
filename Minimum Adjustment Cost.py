import sys
class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if A == None or len(A) == 0:
        	return 0

        D = [[0 for _ in xrange(101)] for _ in xrange(len(A))]
        size = len(A)

        for i in xrange(size):
        	for j in xrange(1, 101):
        		D[i][j] = sys.maxint
        		if (i == 0):
        			D[i][j] = abs(j - A[i])
        		else:
        			for k in xrange(1, 101):
        				if (abs(j - k) > target):
        					continue

        				dif = abs(j - A[i]) + D[i-1][k]
        				D[i][j] = min(D[i][j], dif)

        ret = sys.maxint
        for i in xrange(1, 100):
        	ret = min(ret, D[size - 1][i])
        return ret


a = Solution()
print a.MinAdjustmentCost([1,4,2,3],1)
                

