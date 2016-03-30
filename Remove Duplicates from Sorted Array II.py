class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums
        left = 0
        right = 0
        isTwice = False 
        isThrid = False
        while left <= right and right < len(nums):
            if nums[left] != nums[right] and right - left <= 1:
                left += 1
                right += 1
            elif nums[left] == nums[right] and isTwice == False:
                right += 1
                left += 1
                isTwice = True
            elif nums[left] == nums[right] and isTwice == True:
                right += 1
            elif nums[left] != nums[right] and right - left > 1:
                nums[left] = nums[right]
                left += 1
                right += 1
            print right, left
        print left, right
        return nums[:left]


a = Solution()
print a.removeDuplicates([1,1,1,2,2,3])