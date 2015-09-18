class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        length = len(nums)
        new_array = [x for x in xrange(len(nums)+1)]
        #print new_array
        for item in nums:
        	new_array[item] = -1
        for item in new_array:
        	if item != -1:
        		return item


a = Solution()
print a.findMissing([0,1,3])



