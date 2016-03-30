class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, temp, final_res):
            if target == 0:
                if sorted(temp) not in final_res:
                    final_res.append(sorted(temp))
                return
            for c in candidates:
                if target - c >= 0:
                    candidates.remove(c)
                    dfs(candidates, target-c, temp+[c], final_res)
                    candidates.append(c)

        final_res = []
        if target == None or candidates == None:
            return final_res
        dfs(candidates, target, [], final_res)
        return final_res

a = Solution()
print a.combinationSum2([2,3,6,7], 7)
print a.combinationSum2([8,7,4,3], 11)
print a.combinationSum2([10,1,2,7,6,1,5], 8)