class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if len(nums) == 0 or target == None:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] == target:
                end = mid
        if (nums[start] == target):
            return start
        if (nums[end] == target):
            return end
        return -1


a = Solution()
print a.binarySearch([1,2,3,3,3,3,4,5,10],3)
