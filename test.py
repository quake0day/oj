preset = {'car', 'leet'}
cand = {'carrot', 'car', 'cheese'}

res = []
for prefix in preset:
	for candidate in cand:
		if candidate.startswith(prefix):
			res.append(candidate)
print res


a = [1,2,3]
b = [3,4,6]
print [sum(x) for x in zip(a,b)]

# def permuataion(dicts):
# 	def dfs(node, length, res, rest_lest):
# 		if length == len(node):
# 			res.append(node)
# 		else:
# 			for i in xrange(len(rest_list)):
# 				dfs(node + [rest_list[i]], length, res, rest_list[:i]+rest_list[i+1:])

# 	n = len(dicts)
# 	rest = []
# 	if n == 0 or dicts == None:
# 		return res 
# 	if n == 1:
# 		return [dicts]
# 	dfs([], 2, dicts, rest)
# 	return res

# print permuataion([a,b])

import collections

a = [1,3,-1,-3,5,3,6,7]
k = 3

dq = collections.deque()
for i in xrange(len(nums)):
	while dq and nums[dq[-1]] <= nums[i]:
		dq.pop()
	dq.append(i)
	if dq[0] == i - k:
		dq.popleft()
	if i >= k - 1:
		ans.append(nums[dq[0]])
	return ans

