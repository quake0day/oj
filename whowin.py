pair_list = [(1,4), (2,5), (5,1), (1,6), (6,4), (4,7), (1,7)]

#topo_sort
import collections
def getRank(pair_list):
    #g = {key:[] for key in set}
    g = {}
    indegree = {}
    for a, b in pair_list:
        if a not in g:
            g[a] = [b]
        else:
            g[a].append(b)
        if b not in g:
            g[b] = [a]
        else:
            g[b].append(a)
        if a not in indegree:
            indegree[a] = 1
        elif a in indegree:
            indegree[a] += 1
        if b not in indegree:
            indegree[b] = 0
    start = [i for i,j in indegree.items() if j == 0]
    if len(start) > 1:
        return "ERROR"
    start = start[0]
    print g
    q = collections.deque([start])
    final_res = []
    while q:
        node = q.popleft()
        for neighbor in g[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
        final_res.append(node)
        del g[node]
        #neighbor[]

    #final_res.append(g.keys()[0])
    return final_res[::-1]

        


    

print getRank(pair_list)