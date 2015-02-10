class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        num = nums[0]
        count = 1
        size = len(nums)
        for i in xrange(1, size):
        	if count == 0:
        		num = nums[i]
        		count = 1
        	elif (nums[i] == num):
        		count += 1
        	else:
        		count -= 1
        return num


a = Solution()
print a.majorityNumber([1,2,1,1,1,11])

        
