import sys
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        last = 0
        curr = 0
        for i in xrange(len(nums)):
        	if i > last:
        		last = curr
        		ret += 1
        	curr = max(curr, i+nums[i])
        return ret

a = Solution()
print a.jump([2,3,1,1,4])
print a.jump([2,3])