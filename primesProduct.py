from heapq import heappush, heappop
def primeProduct(nums):
    res = []
    for i in xrange(len(nums)):
        l = len(res)
        res += [nums[i]]
        for j in xrange(l):
            res += [res[j] * nums[i]]
    return res

print primeProduct([3,5,11])



def shiftNoneZero(arr):
    l, r = 0, 0
    for r in xrange(len(arr)):
        if arr[r] != 0:
            arr[r], arr[l] = arr[l], arr[r]
            l += 1
    return arr 

print shiftNoneZero([0,1,0,0,4,2,0,3])


def topK(stream):
    k = 3
    h = [None] * k
    for i in stream:
        heappush(h, i)
        if len(h) >= k:
            heappop(h)
        print h

topK([1,1,2,1,1,3,4,5])
topK(['Alice','Bob', 'Alice', 'Bob', 'Bob', 'Chuck'])
