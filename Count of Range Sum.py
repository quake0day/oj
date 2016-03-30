class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        size = len(nums)
        sums = [0] * (size + 1)
        for x in range(1, size + 1):
            sums[x] += nums[x - 1] + sums[x - 1]
        INF = max(sums)

        def mergeSort(lo, hi):
            if lo == hi: return 0
            mi = (lo + hi) / 2
            cnt = mergeSort(lo, mi) + mergeSort(mi + 1, hi)
            x = y = lo
            for i in range(mi + 1, hi + 1): 
                print sums[i], sums[x], sums[y]

                while x <= mi and sums[i] - sums[x] >= lower:
                    x += 1
                while y <= mi and sums[i] - sums[y] > upper:
                    y += 1
                cnt += x - y
            part = sums[lo : hi + 1]

            l, h = lo, mi + 1
            for i in range(lo, hi + 1):
                x = part[l - lo] if l <= mi else INF
                y = part[h - lo] if h <= hi else INF
                if x < y: l += 1
                else: h += 1
                sums[i] = min(x, y)
            return cnt

        return mergeSort(0, size)


def brute(nums):
    sums = [0]*(len(nums)+1)
    for i in xrange(0, len(nums)):
        sums[i+1] = sums[i] + nums[i]
    for i in xrange(len(nums)):
        for j in range(i+1, len(nums)+1):
            print sums[i], sums[j]


a = Solution()
#print a.countRangeSum([-2, 5, -1], -2,2)

brute([-2, 5, -1])