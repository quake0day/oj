def check_continue(data):
	res = {}
	for i in data:
		if i not in res:
			res[i] = 1
		else:
			res[i] += 1
	return [x > 3 for x in res.values()]

print any(check_continue([1,2,2,2,2,2,2,3,3,4,4]))