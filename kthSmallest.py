from heapq import heappush, heappop
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        heap = []
        m = 0
        res = ""
        for i in xrange(len(matrix)):
        	for j in xrange(len(matrix[0])):
        		heappush(heap, matrix[i][j])
        		
        		if m > k:
        			for i in xrange(1,k):
        				res = heappop(heap)
        			return res
        		m += 1


a = Solution()
print a.kthSmallest([
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
], 4)

