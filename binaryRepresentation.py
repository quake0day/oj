class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        length = len(n)
        if length == 0:
        	return n
        split = n.split(".")
        decimalPart = self.decBinary(split[1])
        if decimalPart == "ERROR":
        	return decimalPart
        intPart = self.intBinary(split[0])

        if decimalPart == "":
        	return intPart
        else:
        	return intPart+"."+decimalPart


    def decBinary(self, num):
    	n = "0." + num
    	val = float(n)
    	sb = []

    	while val != 0:
    		if len(sb) > 32:
    			return "ERROR"
    		r = val * 2
    		if r >= 1:
    			sb.append("1")
    			val = r - 1
    		else:
    			sb.append("0")
    			val = r
    	return "".join(sb)


    def intBinary(self, num):
    	i = int(num)
    	sb = []
    	base = 1
    	current = 0
    	while current != i:
    		if (i & base) != 0:
    			sb.append("1")
    			current += base
    		else:
    			sb.append("0")
    		base = base << 1
    	if len(sb) == 0:
    		sb.append("0")
    	return "".join(sb)[::-1]


