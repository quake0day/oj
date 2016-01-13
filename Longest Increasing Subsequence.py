class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
       	if n == 0: return 0
       	if n == 1: return 1
        DP = [1] * n
        for i in xrange(1, n):
        	for j in xrange(i-1, -1, -1):
	        	if nums[i] > nums[j] and DP[i] < DP[j] + 1:
	        		DP[i] = DP[j] + 1
        return DP,max(DP)

        


a = Solution()
print a.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print a.lengthOfLIS([2,2])