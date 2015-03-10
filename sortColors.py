class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums == None or len(nums) <= 1:
        	return
       	pl = 0
       	pr = len(nums) - 1
       	i = 0
       	while i <= pr:
       		if nums[i] == 0:
       			nums = self.swap(nums, pl, i)
       			pl += 1
       			i += 1
       		elif nums[i] == 1:
       			i += 1
       		else:
       			nums = self.swap(nums, pr, i)
       			pr -= 1
       	return nums

    def swap(self, a, i, j):
    	tmp = a[i]
    	a[i] = a[j]
    	a[j] = tmp
    	return a
