def kpair(nums, target):
    mapping = {}
    result = []
    for i in xrange(len(nums)):
        possible1 = nums[i] - target
        possible2 = nums[i] + target
        if possible1 in nums:
            if sorted([nums[i], possible1]) not in result:
                result += [sorted([nums[i], possible1])]
        if possible2 in nums:
            if sorted([nums[i], possible2]) not in result:
                result+= [sorted([nums[i], possible2])]
    return len(result)

print kpair([1,5,3,4,2], 2)
