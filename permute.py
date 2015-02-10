rst = []
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # def permute(self, nums):
    # 	if len(nums) < 2:
    # 		return [nums]
    # 	ret = []
    # 	for permu in self.permute(nums[:-1]):
    # 		ret += [permu[:i] + [nums[-1]] + permu[i:] for i in range(len(permu) + 1)]
    # 	return ret
    def permute(self, nums):
    	length = len(nums)
    	if length == 0: return []
    	if length == 1: return [nums]
    	res = []
    	for i in xrange(length):
    		for j in self.permute(nums[0:i] + nums[i+1:]):
    			res.append([nums[i]] + j)
    	return res
    # def permute(self, nums):
    #     # write your code here
    #     p_list = []
    #     global rst
    #     if (nums == None or len(nums) == 0):
    #     	return rst
    #     self.helper(rst, p_list, nums)
    #    	return rst


    # def helper(self, rst, p_list, nums):
    # 	if len(p_list) == len(nums):
    # 		rst.append(p_list)
    # 		return 

    # 	for i in xrange(len(nums)):
    # 		if nums[i] in p_list:
    # 			pass
    # 		else:
	   #  		p_list.append(nums[i])
	   #  		self.helper(rst, p_list, nums)
	   #  		p_list.pop()

a = Solution()
print a.permute([1,2,3,4])