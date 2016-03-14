from heapq import heappush, heappop

heap = []

data = [1,3,5,7,8,2,4,6,7,10]
for item in data:
    heappush(heap, item)

for i in xrange(len(data)):
    print heappop(heap)