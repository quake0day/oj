def twoSum(numbers, target):
	res = [None] * 2
	if numbers == None or len(numbers) < 2:
		return None
	hashMap = {}

	for i in xrange(len(numbers)):
		if(target - numbers[i]) in hashMap:
			res[0] = hashMap.get(target - numbers[i]) + 1
			res[1] = i + 1
			return res

		hashMap[numbers[i]] = i
	return None



print twoSum([1,2,3,5,6],9)
