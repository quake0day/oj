class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, temp, final_res, length):
            if len(temp) == length:
                final_res.append(temp)
                return
            if nums:
                for i in xrange(len(nums)):
                    dfs(nums[:i]+nums[i+1:], temp+[nums[i]], final_res, length)
        final_res = []
        dfs(nums, [], final_res, len(nums))
        return final_res

a = Solution()
print a.permute([1,2,3])