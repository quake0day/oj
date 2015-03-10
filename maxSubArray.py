import sys
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums == None:
        	return 0

        maximum = nums[0]
        length = len(nums)
        for i in xrange(len(nums)):
        	tempSum = nums[i]
        	max_ = max(maximum, tempSum)
        	for j in xrange(i+1, length):
        		if tempSum > 0:
        			tempSum += nums[j]
        			max_ = max(max_, tempSum)
        		else:
        			break
        return max_


a = Solution()
print a.maxSubArray([-2,2,-3,4,-1,2,1,-5,3])

