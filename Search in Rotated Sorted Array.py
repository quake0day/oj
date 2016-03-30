class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid =  l + r >> 1
            print mid
            if nums[mid] == target:
                return mid
            elif nums[mid] < target and nums[l] <= nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target and  target < nums[mid] <= nums[r]:
                r = mid - 1
            elif nums[mid] > target and  not target < nums[mid] <= nums[r]:
                l = mid + 1
            else:
                return -1
        return -1
        

a = Solution()
print a.search([3,5, 1], 3)
#print a.search([1], 1)