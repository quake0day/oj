class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        num_list = [i for i in xrange(1, n+1)]
        def dfs(num_list, final_res, k, temp):
            if len(temp) == k:
                if sorted(temp) not in final_res:
                    final_res.append(temp)
                return

            for i in xrange(len(num_list)):
                dfs(num_list[:i]+num_list[i+1:], final_res, k, temp+[num_list[i]])
        final_res = []
        dfs(num_list, final_res, k, [])
        return final_res

class Solution2:
    # @return a list of lists of integers
    def combine(self, n, k):
        def dfs(start, valuelist):
            if self.count == k: ret.append(valuelist); return
            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, valuelist + [i])
                self.count -= 1
        ret = []; self.count = 0
        dfs(1, [])
        return ret

a = Solution2()
print a.combine(4,2)
        