import sys
class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        res = 0
        if A == None or len(A) == 0:
        	return res

        forLeft = True
        start = 0
        res = 1
        for i in xrange(1, len(A)):
        	if A[i] > A[i-1]:
        		if forLeft:
        			res = max(res, i - start + 1)
        		else:
        			start = i - 1
        			forLeft = True
        	elif A[i] < A[i-1]:
        		if forLeft == False:
        			res = max(res, i - start + 1)
        		else:
        			start = i - 1
        			forLeft = False
        return res

a = Solution()

print a.longestIncreasingContinuousSubsequence([5, 4, 2, 1, 3])
print a.longestIncreasingContinuousSubsequence([5, 1, 2, 3, 4])
print a.longestIncreasingContinuousSubsequence([1,3,5,7,9])

