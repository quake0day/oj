class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, flags = [], [False]*len(nums)
        nums.sort()
        self.dfs(nums, flags, [], res)
        return res
    
    def dfs(self, nums, flags, path, res):
        if len(nums) == len(path):
            res.append(path)
            return
        for i in xrange(len(nums)):
            if not flags[i]:
                if i > 0 and not flags[i-1] and nums[i] == nums[i-1]:
                    continue
                flags[i] = True
                self.dfs(nums, flags, path+[nums[i]], res)
                flags[i] = False
        

a = Solution()
print a.permuteUnique([1,1,2])