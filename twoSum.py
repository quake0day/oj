class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        res = [None] * 2
        if numbers == None or len(numbers) < 2:
            return None
        hashMap = {}
        for i in xrange(len(numbers)):
            if (target - numbers[i]) in hashMap:
                res[0] = hashMap.get(target-numbers[i]) + 1
                res[1] = i + 1
                return res
            hashMap[numbers[i]] = i
        return None
        #nums = sorted(numbers)
        # nums = sorted(numbers)
        # if len(nums) < 0:
        #     return None
        # i = 0
        # j = len(nums) - 1
        # while i < j:
        #     if nums[i] + nums[j] < target:
        #         i += 1
        #     elif nums[i] + nums[j] > target:
        #         j -= 1
        #     else:
        #         return [i+1,j+1]



a  = Solution()
print a.twoSum([1,0,-1], -1)
print a.twoSum([1,0,-1], 1)

print a.twoSum([2,7,11, 15], 9)

