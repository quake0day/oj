class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        res = []
        for i in xrange(len(nums)):
        	if nums[i] % 2 == 0:
        		nums.append(nums[i])
        		nums[i] = -1
        for item in nums:
        	if item != -1:
        		res.append(item)
        return res

a = Solution()
print a.partitionArray([402,455,25,15,42,538,369,741,651,473,310,112,525,682,622,119,287,242,701,439])
