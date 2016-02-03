# def find_missing(input_):
# 	res = []
# 	k = helper(input_, 0, len(input_)/2, res)
# 	print k

# def helper(string, start, length, res):
# 	if len(res) * length == len(string):
# 		return new
# 	string1 = string[start:start+length] 
# 	if len(res) == 0:
# 		res.append(int(string1))
# 		helper(string, start+length, length, res)
# 	else:
# 		if int(string1) - res[-1] == 1 or int(string1) - res[-1] == 2:
# 			res.append(int(string1))
# 			helper(string, start+length, length, res)
# 		else:
# 			length -= 1
# 			res = []
# 			helper(string, 0, length, res)

def find_missing(input_):
	length = len(input_)
	res = []

	for j in xrange(1, length/2):
		res = [int(input_[i:i+j]) for i in xrange(0, length, j)]
		if len(res) * j == len(input_):
			q = 2
			for i in xrange(1, len(res)):
				if (res[i-1] == res[i] - 1) or (res[i-1] == res[i] - 2): 
					q -= 1
			if q == 0:
				return get_missing(res)
		
def get_missing(nums):
	r = 0
	for i in xrange(len(nums)):
		r ^= i ^ nums[i]
	return r ^ len(nums)		
			

print find_missing("125612571259")