class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(node, rest_list, res):
            if rest_list == []:
                res.append(node)
            else:
                for i in xrange(len(rest_list)):
                    dfs(node+[rest_list[i]], rest_list[:i]+rest_list[i+1:], res)
            
        
        n = len(nums)
        res = []
        if n == 0 or nums == None:
            return [res]
        if n == 1:
            return [nums]
        dfs([], nums, res)
        return res


a = Solution()
print a.permute([1,2,3])