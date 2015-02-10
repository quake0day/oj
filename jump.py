import sys
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        if (len(A) <= 0):
        	return 0
        least_jump = [0] * len(A)
        
        # init
        least_jump[0] = 0

        for i in xrange(1,len(A)):
        	#print A[i]
        	least_jump[i] = sys.maxint
        	for j in xrange(A[i]):
        		if (least_jump[j] != sys.maxint and j + A[j] >= i):
        			least_jump[i] = least_jump[j] + 1
        			break
        		#print i+j
        return least_jump[-1]
a = Solution()
print a.jump([1,2,3,4])
