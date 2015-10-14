import math
class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        # write your code here
        nA = self.norm(A)
        nB = self.norm(B)
        m = 0
        if nA == 0 or nB == 0:
        	return 2.0
        for i in xrange(len(A)):
        	m += A[i] * B[i]
        return m / (nA * nB)

    def norm(self, A):
    	res = 0
    	for i in xrange(len(A)):
    		res += A[i] * A[i]

    	return math.sqrt(res)




a = Solution()
print a.cosineSimilarity([1, 2, 3], [2, 3 ,4])
