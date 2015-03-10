class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
    	if k < 1 or k > len(A):
    		return -1
    	return self.helper(len(A)-k +1, A, 0, len(A)-1)

    def helper(self, k, A, start, end):
    	pivot = A[end]
    	left = start
    	right = end
    	while True:
    		while A[left] < pivot and left < right:
    			left += 1
    		while A[right] >= pivot and right > left:
    			right -= 1
    		if (left == right):
    			break
    		self.swap(A, left, right)

    	# left: the first one which is bigger than pivot
    	self.swap(A, left, end)

    	if (k == left + 1):
    		return pivot
    	elif k < left + 1:
    		return self.helper(k, A, start, left-1)
    	else:
    		return self.helper(k, A, left+1, end)



    def swap(self, A, i, j):
    	tmp = A[i]
    	A[i] = A[j]
    	A[j] = tmp

        
