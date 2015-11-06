class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        i = 0
        while i < len(A):
        	if A[i] != (i+1) and A[i] >= 1 and A[i] <= len(A) and A[A[i]- 1] != A[i]:
        		A[A[i]-1], A[i] = A[i], A[A[i]-1]
        	else:
        		i += 1
        print A
        for i in xrange(len(A)):
        	if A[i] != (i+1):
        		print "HI"
        		return i+1
        return len(A)+1


a = Solution()
print a.firstMissingPositive([2,1])