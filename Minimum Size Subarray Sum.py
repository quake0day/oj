class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        currsum = 0
        bestAns = len(nums) + 1
        while end < len(nums):
            while end < len(nums) and currsum < s:
                currsum += nums[end]
                end += 1
                while currsum >= s and start < end:
                    bestAns = min(bestAns, abs(start - end))
                    currsum -= nums[start]
                    start += 1
        return [0, bestAns][bestAns <= len(nums)]


a = Solution()
print a.minSubArrayLen(7, [2,3,1,2,4,3])