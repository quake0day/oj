class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums == None or len(nums) == 0:
            return result
        list = []
        visited = [0] * len(nums)
        nums = sorted(nums)
        self.helper(result, list, visited, nums)
        return result
        
        
    def helper(self, result, list, visited, nums):
        if len(list) == len(nums):
            temp = list[:]
            result.append(temp)
            return result
        
        for i in xrange(len(nums)):
            if(visited[i] == 1 or (i != 0 and nums[i] == nums[i-1] and visited[i-1] == 0)):
                continue
            visited[i] = 1
            list.append(nums[i])
            self.helper(result, list, visited, nums)
            list.pop()
            visited[i] = 0


a = Solution()
print a.permuteUnique([1])
