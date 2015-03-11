import heapq
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def __init__(self):
        self.heap_min = []
        self.heap_max = []

    def insert(self, num):
        if not self.heap_min or num > self.heap_min[0]:
            heapq.heappush(self.heap_min, num)
        else:
            heapq.heappush(self.heap_max, -num)
        self.balance()

    def balance(self):
        l1 = len(self.heap_min)
        l2 = len(self.heap_max)
        if l1-l2 > 1:
            heapq.heappush(self.heap_max, -heapq.heappop(self.heap_min))
            self.balance()
        elif l2-l1 > 1:
            heapq.heappush(self.heap_min, -heapq.heappop(self.heap_max))
        return 

    def get_median(self):
        l1 = len(self.heap_min)
        l2 = len(self.heap_max)
        m = (l1 + l2 - 1) / 2
        if m == l2 - 1:
            return -self.heap_max[0]
        elif m == l2:
            return self.heap_min[0]
        raise Exception("not blanced")


    def medianII(self, nums):
        # write your code here
        ret = []
        for num in nums:
            self.insert(num)
            ret.append(self.get_median())
        return ret


a = Solution()
print a.medianII([4, 5, 1, 3, 2, 6, 0])