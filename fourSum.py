class Solution:
    """
    @param numbersbers : Give an array numbersbersbers of n integer
    @param target : you need to find four elements that's sum of target
    @return : Find all unique quadruplets in the array which gives the sum of 
              zero.
    """

    def fourSum(self ,numbers, target):
        # write your code here
        rst = []
        numbers.sort()

        for i in xrange(len(numbers) - 3):
        	if i != 0 and numbers[i] == numbers[i-1]:
        		continue
        	for j in xrange(i+1, len(numbers) - 2):
        		if j != i+1 and numbers[j] == numbers[j-1]:
        			continue

        		left = j + 1
        		right = len(numbers) - 1
        		while left < right:
        			sum_ = numbers[i] + numbers[j] + numbers[left] + numbers[right]
        			if sum_ < target:
        				left += 1
        			elif sum_ > target:
        				right -= 1
        			else:
        				tmp = []
        				tmp.append(numbers[i])
        				tmp.append(numbers[j])
        				tmp.append(numbers[left])
        				tmp.append(numbers[right])
        				rst.append(tmp)
        				left += 1
        				right -= 1
        				while left < right and numbers[left] == numbers[left - 1 ]:
        					left += 1
        				while left < right and numbers[right] == numbers[right + 1]:
        					right -= 1
       	return rst

    # TLE for lintcode...
    def fourSum_TLE(self ,numbers, target):
        # write your code here
        numLen, res, dict = len(numbers), set(), {}
        if numLen < 4: return []
        numbers.sort()

        for p in xrange(numLen):
        	for q in xrange(p+1, numLen):
        		if numbers[p] + numbers[q] not in dict:
        			dict[numbers[p]+numbers[q]] = [(p,q)]
        		else:
        			dict[numbers[p]+numbers[q]].append((p,q))

        for i in xrange(numLen):
        	for j in xrange(i+1, numLen - 2):
        		T = target - numbers[i] - numbers[j]
        		if T in dict:
        			for k in dict[T]:
        				if k[0] > j:
        					res.add((numbers[i],numbers[j],numbers[k[0]],numbers[k[1]]))
        return [list(i) for i in res]


    # def fourSum(self ,numbers, target):
    #     # write your code here
    #     res = []
    #     if numbers == None or len(numbers) <= 2:
    #         return res       
    #     for i in xrange(len(numbers) -1, 1, -1):
    #     	if i == len(numbers) -1 or numbers[i] != numbers[i+1]:
    #     		curRes = self.threeSum(numbers, i-1, target-numbers[i])
    #     		for j in xrange(len(curRes)):
    #     			curRes[j].append(numbers[i])
    #     		res += curRes
    #     res = [x for x in res if x]

    #     return res



    # def threeSum(self, numbers, end, target):
    #     # write your code here
    #     res = []

    #     for i in xrange(end, 1, -1):
    #         if i == end  or numbers[i] != numbers[i+1]:       
	   #          curRes = self.twoSum(numbers, i-1, target-numbers[i])
	   #          for j in xrange(len(curRes)):
	   #              curRes[j].append(numbers[i])
	   #          res += curRes
    #     return res


    # def twoSum(self, numbers, end, target):
    #     res = []
    #     if numbers == None or len(numbers) <= 1:
    #         return res
    #     i = 0
    #     j = end

    #     while i < j:
    #         if numbers[i] + numbers[j] == target:
    #             res_ = [None] * 2
    #             res_[0] = numbers[i]
    #             res_[1] = numbers[j]
    #             res.append(res_)
    #             i += 1
    #             j -= 1
    #             while (i < j and numbers[i] == numbers[i - 1]):
    #                 i += 1
    #             while i < j and numbers[j] == numbers[j+1]:
    #                 j -= 1
    #         elif numbers[i] + numbers[j] > target:
    #             j -= 1
    #         else:
    #             i += 1

    #     return res
a = Solution()
print a.fourSum([1,0,-1,0,-2,2],0)