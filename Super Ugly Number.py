class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        hashmap = {val:0 for val in primes}
        m  = [float('inf')] * len(primes)
        while len(res) < n:
            newm = [res[hashmap[p]] * p for p in primes]
            mn = min(newm)
            hashmap[primes[newm.index(mn)]] += 1
            if mn not in res:
                res.append(mn)
            else:
                continue
        return res[-1]


a = Solution()
print a.nthSuperUglyNumber(12, [2, 7, 13, 19])   