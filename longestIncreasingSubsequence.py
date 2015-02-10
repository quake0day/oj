class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
    	if nums == None or len(nums) == 0:
    		return 0
        # write your code here
        f = [1] * len(nums)
        for i in xrange(len(nums)):
        	for j in xrange(i):
        		if (nums[j] <= nums[i]):
        			if f[i] > f[j] + 1:
        				f[i] = f[i]
        			else:
        				f[i] = f[j] + 1
        return max(f)

a = Solution()
print a.longestIncreasingSubsequence([1,2,3,9,4])


