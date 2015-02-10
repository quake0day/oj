class Solution:
    """
    @param A : An integer array
    @return : An integer
    """
    def singleNumberII(self, A):
        # write your code here
        res = 0
        if A == None or A == 0:
            return -1
        n = len(A)
        #for item in A:
            #for k in self.baseConvert(item)
        bits = [0]*32
        for i in xrange(32):
            for j in xrange(n):
                bits[i] += A[j] >> i & 1
                bits[i] %= 3
            res |= (bits[i] << i)
        return res

    def baseConvertInv(self, n):
        string = str(n)[::-1]
        base = 1
        res = 0
        for word in string:
            res += int(word) * base
            base *= 3
        return res


    def baseConvert(self, n):
        result = ''
        while True:
            tup = divmod(n, 2)
            result += str(tup[1])
            if tup[0] == 0:
                return int(result[::-1])
            else:
                n = tup[0]

a = Solution()
print a.singleNumberII([3,3,3,4])