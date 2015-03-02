class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        mini = min(nums)

        current = 0
        for item in nums:
        	current += item
        	mini = min(mini, current)
        	if current > 0:
        		current = 0
        return mini


a = Solution()

print a.minSubArray([1,-1,-2,1])