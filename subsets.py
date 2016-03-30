class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(tmp, final_res, nums):
            final_res.append(tmp)
            if len(nums) == 0:
                return
            for i in xrange(len(nums)):
                helper(tmp+[nums[i]], final_res, nums[i+1:])
        final_res = []
        helper([], final_res, nums)
        return final_res


a = Solution()
print a.subsets([1,2,3])