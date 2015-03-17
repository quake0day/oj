class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res = []
        if numbers == None or len(numbers) <= 2:
            return res
        numbers = sorted(numbers)
        for i in xrange(len(numbers)-1, 1, -1):
            if i < len(numbers) - 1 and numbers[i] == numbers[i+1]:
                continue
            curRes = self.twoSum(numbers, i-1, -numbers[i])
            for j in xrange(len(curRes)):
                curRes[j].append(numbers[i])
            res += curRes
        res = [x for x in res if x]
        return res


    def twoSum(self, numbers, end, target):
        res = []
        if numbers == None or len(numbers) <= 1:
            return res
        i = 0
        j = end

        while i < j:
            if numbers[i] + numbers[j] == target:
                res_ = [None] * 2
                res_[0] = numbers[i]
                res_[1] = numbers[j]
                res.append(res_)
                i += 1
                j -= 1
                while (i < j and numbers[i] == numbers[i - 1]):
                    i += 1
                while i < j and numbers[j] == numbers[j+1]:
                    j -= 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return res


a = Solution()
print a.threeSum([-1,0,1,2,-1,-4])
print a.threeSum([-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5])
print a.threeSum([-1,0,1,2,-1,-4])
print a.threeSum([1,0,-1,-1,-1,-1,0,1,1,1])