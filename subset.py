class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        import itertools
        # write your code here
        S = sorted(S)
        combs = []

        for i in xrange(1, len(S)+1):
            els = [list(x) for x in itertools.combinations(S, i)]
            combs.extend(els)
        return combs








a = Solution()
print a.subsets([3,2,4,1])
