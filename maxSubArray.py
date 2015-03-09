import sys
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        maximum = -sys.maxint - 1
        sum_ = 0
        for item in nums:
        	sum_ += item
        	maximum = max(maximum, sum_)
        	sum_ = max(sum_, 0)
        return maximum


a = Solution()
print a.maxSubArray([-2,2,-3,4,-1,2,1,-5,3])

