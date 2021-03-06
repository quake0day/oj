class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """

    def dfs(self, pos, k, n , start, ans, vec):
    	if pos == k:
    		temp = vec[:]
    		ans.append(temp)
    		return
    	for i in xrange(start, n+1):
    		vec[pos] = i
    		self.dfs(pos+1, k, n , i+1, ans, vec)

    def combine(self, n, k):
    	ans = []
    	vec = [0 for i in xrange(k)]
    	self.dfs(0, k, n, 1, ans, vec)
    	return ans    
        # write your code here   

    #     res = []
    #     if n <= 0 or k == 0:
    #     	return res

    #     nums = [0] * n
    #     for i in xrange(len(nums)):
    #     	nums[i] = i + 1

    #     tempList = []

    #     for i in xrange(n-k+1):
    #     	tempList.append(nums[i])
    #     	self.helper(res, tempList, nums, k, i + 1)
    #     return res



    # def helper(self, res, tempList, nums, len_, index):
    # 	if len(tempList) == len_:
    # 		res.append(tempList[:])
    # 		return
    # 	if index == len(nums):
    # 		return 
    # 	for i in xrange(index, len(nums)):
    # 		tempList.append(nums[i])
    # 		self.helper(res, tempList, nums, len_, i+1)
    # 		tempList.pop()


a = Solution()
print a.combine(2,1)
print a.combine(4,3)