class Solution:
    """
    @param nums: The rotated sorted array
    @return: The recovered sorted array
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        for index in xrange(len(nums) - 1):
        	if (nums[index] > nums[index+1]):

        		self.reverse(nums, 0, index)
        		self.reverse(nums, index+1, len(nums)-1)
        		nums = nums[::-1]
        		
        return nums

    def reverse(self, nums, start, end):
    	i = start
    	j = end
    	while i < j:
    		temp = nums[i]
    		nums[i] = nums[j]
    		nums[j] = temp
    		i += 1
    		j -= 1
    	

a = Solution()
print a.recoverRotatedSortedArray([4,5,1,2,3])