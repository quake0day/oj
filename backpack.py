class Solution_MLE:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        f = [[False for i in xrange(m + 1)] for i in xrange(len(A) + 1)]

        # state: f[i][j]
        # Meaning: from the first i numbers, take some, is it possible to get an addition equal to j?
        f[0][0] = True
        for i in xrange(len(A)):
        	for j in xrange(m+1):
        		# if take some of the first i numbers, and we're able to get j
        		# then, take some of the first i+1 numbers, we're able to do the same thing
        		f[i + 1][j] = f[i][j]

        		# otherwise, if satisfy: f[i][S] = f[i-1][S-a[i]]

        		if (j >= A[i] and f[i][j - A[i]]):
        			f[i+1][j] = True
        for i in xrange(m,-1,-1):
        	if (f[len(A)][i]):
        		return i
        return 0

class Solution:
    def backPack(self, m, A):
        """
        dp
        f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]}
        to
        f[v]=max{f[v],f[v-c[i]+w[i]}
        NEED TO KEEP A COPY OF (i-1) STATE.
        :param m: An integer m denotes the size of a backpack
        :param A: Given n items with size A[i]
        :return: The maximum size
        """
        n = len(A)
        f = [0 for _ in xrange(m+1)]  # plus 1 for dummy
        for i in xrange(1, n+1):
            copy = list(f)
            for j in xrange(1, m+1):
                # decide whether to put A[i-1]
                if j-A[i-1]>=0:
                    f[j] = max(copy[j], copy[j-A[i-1]]+A[i-1])
                else:
                    f[j] = copy[j]
        return f[m]


a = Solution()
print a.backPack(80000, [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932])