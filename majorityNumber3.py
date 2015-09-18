class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        kover1 = len(nums) / k
        array_kover1 = {}
        for item in nums:
        	if item not in array_kover1.keys():
        		array_kover1[item] += 1
        	elif:
        		array_kover1[item] += 1
        	if array_kover1[item] > kover1:
        		return item

