import collections
# def maxSum(arr):
#     n = len(arr)
#     q = collections.deque(arr)
#     num_list = []
#     for _ in xrange(n):
#         tmp = q.popleft()
#         num_list.append(list(q))
#         q.append(tmp)
#     DP = [[0] * (n-1) for _ in xrange(n)]
#     for i in range(n):
#         DP[i][0] = num_list[i][0]
#         DP[i][1] = num_list[i][1]
#         for k in range(2, n-1):
#             DP[i][k] = max(DP[i][k-1], DP[i][k-2]+num_list[i][k])
#     print DP
#     print num_list
#     return max(DP[c][-2] for c in range(n))


def maxSum(arr):
    
    n = len(arr)
    q = collections.deque(arr)
    q_list = []
    for _ in range(n):
        tmp = q.popleft()
        q.append(tmp)
        q_list.append(list(q))
    max_ = 0
    for q in q_list:
        que = collections.deque(q)
        curMax = 0
        while que:
            curMax += que.popleft()
            que.popleft()
            que.pop()
        max_ = max(curMax, max_)
    return max_

print maxSum([1,10,1,8,1,2])
print maxSum([1,99,98, 99, 100, 101])