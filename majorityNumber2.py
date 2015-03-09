class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        count1 = 0
        count2 = 0
        candidate = [0,0]
        for i in xrange(len(nums)):
        	if count1 == 0:
        		candidate[0] = nums[i]
        	if count2 == 0 and nums[i] != candidate[0]:
        		candidate[1] = nums[i]
        	if nums[i] != candidate[0] and nums[i] != candidate[1] \
        		and count2 != 0 and count1 != 0:
        		count1 -= 1
        		count2 -= 1
        	if nums[i] == candidate[0]:
        		count1 += 1
        	if nums[i] == candidate[1]:
        		count2 += 1
        count1 = 0
        count2 = 0
        for i in xrange(len(nums)):
        	if nums[i] == candidate[0]:
        		count1 += 1
        	elif nums[i] == candidate[1]:
        		count2 += 1
    	if count1 > count2:
    		return candidate[0]
    	else:
    		return candidate[1]



a = Solution()
print a.majorityNumber([1,1,1,1,2,2,3,3,4,4,4])