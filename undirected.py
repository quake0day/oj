import collections
a = [[5,4], [4,5], [5,6], [6,5]]
b = 4 
g = {4:[5], 5:[4,6], 6:[5]}
q = collections.deque()
q.append(b)
final_res = {}
while q:
    node = q.popleft()
    if len(g[node]) != 0:
        for c in g[node]:
            g[c].remove(node)
            q.append(c)
    final_res[node] = g[node]

print final_res


# g = {key:[] for key in [4,5,6]}
# 
# print g[5]
# final_res = []
# while q:
#     node = q.popleft()
#     for c in g[node]:
#         g[c].remove(node)
#         if len(g[c]) == 0:
#             q.append(g[c])
#     final_res.append(node)
#     del g[node]
