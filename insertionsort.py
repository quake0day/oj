def insertionsort(list):
	for i in xrange(1, len(list)):
		tmp = list[i]
		k = i 
		while k > 0 and tmp < list[k-1]:
			list[k] = list[k-1]
			k -= 1
		list[k] = tmp
		print list


print insertionsort([1,2,3,4,8,7])