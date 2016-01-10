class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums) - 1
        while length > 0:
            if nums[length - 1] < nums[length]:
                break
            length -= 1
        if length == 0:
            for i, j in zip(range(length/2+1), range(length, length/2-1, -1)):
                nums[i],nums[j] = nums[j], nums[i]
        k = len(nums) - 1
        while k >= length:
            if(nums[k] > nums[length-1]):
                break
            k -= 1
        nums[k] , nums[length-1] = nums[length-1], nums[k]
        nums = nums[0:length]+sorted(nums[length:])
        return nums


a = Solution()
print a.nextPermutation([1,3,2])
print a.nextPermutation([1,3,2])
