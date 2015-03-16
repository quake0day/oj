class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        n = len(L)
        if n == 0:
        	return 0
        L = sorted(L)
        res = 0
        left = 1 
        right = L[-1]
        while left <= right:
        	mid = (right - left) / 2 + left
        	count = 0
        	for i in xrange(n-1, -1, -1):
        		count += L[i] / mid
        	if count >= k:
        		res = mid
        		left = mid + 1
        	else:
        		right = mid - 1

       	return res
