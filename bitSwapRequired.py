class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    # def bitSwapRequired(self, a, b):
    	# addition = 0
    	# if ((a < 0 and b > 0) or (a > 0 and b < 0)):
    	# 	return 31


     #    # write your code here
     #    bin_a = bin(a).split("b")[1][::-1]
     #    bin_b = bin(b).split("b")[1][::-1]
     #    len_a = len(bin_a)
     #    len_b = len(bin_b)
     #    diff_len = abs(len_a - len_b)

     #    min_len = min(len_a, len_b)
     #    result = 0

     #    for i in xrange(min_len):
     #    	if bin_a[i] != bin_b[i]:
     #    		result += 1
     #    for j in xrange(min_len,diff_len+min_len):
	    #     try:
	    #     	if bin_a[j] == '1':
	    #     		result += 1
	    #     except:
	    #     	pass
	    #     try:
	    #     	if bin_b[j] == '1':
	    #     		result += 1
	    #     except:
	    #     	pass
     #    return result
        # while xor != 0:
        # 	if xor & 1 == 1:
        # 		result += 1
        # 	xor >>= 1
        # return result

    def bitSwapRequired(self, a, b):
        # write your code here
        xor = a ^ b 
        result = 0
        index = 0
        while index < 32:
            if ((1 << index) & a) != ((1 << index) & b):
                result += 1
            index += 1
        return result
        
a = Solution()
print a.bitSwapRequired(14, 31)
print a.bitSwapRequired(67, 31)
print a.bitSwapRequired(1, -1)
print a.bitSwapRequired(-2147483648, 2147483647)