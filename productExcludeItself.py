class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        B = []
        for i in xrange(len(A)):
        	res = 1
        	for j in xrange(len(A)):
        		
        		if j == i:
        			pass
        		else:
        			res = res * A[j]
        	B.append(res)
        return B


a = Solution()
print a.productExcludeItself([1,2,3])
