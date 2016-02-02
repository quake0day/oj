class Solution(object):
	def canJump(self, nums):
		step = nums[0]
		for i in xrange(1, len(nums)):
			if step > 0:
				step -= 1
				step = max(step, nums[i])
			else:
				return False
		return True
    # def canJump_TLE(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     DP = [False] * len(nums)
    #     DP[0] = True
    #     for i in xrange(len(nums)):
    #     	for k in xrange(nums[i]):
    #     		if i + k < len(nums):
    #     			DP[i+k] = True
    #     return reduce(lambda x, y: x and y, DP )

a = Solution()
print a.canJump([2,3,1,1,4])
print a.canJump([3,2,1,0,4])
