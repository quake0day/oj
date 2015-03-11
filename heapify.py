class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        n = len(A)
        for i in xrange(n/2, -1, -1):
        	self.heappush(A, i)


    def heappush(self, A, i):
    	n = len(A)
    	if i >= n:
    		return 
    	l = 2*i + 1
    	r = 2*i + 2

    	mini = i
    	if l < n and A[l] < A[mini]:
    		mini = l
    	if r < n and A[r] < A[mini]:
    		mini = r
    	if i != mini:
    		A[i], A[mini] = A[mini], A[i]
    		self.heappush(A, mini)