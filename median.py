class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        if len(nums) <= 0:
        	return None
        return self.sub(nums, 0, len(nums) - 1, (len(nums) + 1) / 2)
    

    def sub(self, A, start, end, size):
    	i = start + 1
    	j = end
    	while i <= j:
    		while(i <= j and A[i] < A[start]):
    			i += 1
    		while(i <= j and A[j] >= A[start]):
    			j -= 1
    		if (i < j):
    			self.swap(A, i, j)
    	self.swap(A, start, j)
    	if j + 1 == size:
    		return A[j]
    	elif j + 1 > size:
    		return self.sub(A, start, j, size)
    	else:
    		return self.sub(A, j+1, end, size)

    def swap(self, nums, i, j):
    	tmp = nums[i]
    	nums[i] = nums[j]
    	nums[j] = tmp
a = Solution()
print a.median([4,5,1,2,3])