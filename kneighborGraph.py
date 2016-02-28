graph = [['a','b'],['b','c'],['c','a'],['a','d']]

import collections
def getSubset(graph, k):
    graph_ = {}
    
    for node in graph:
        if not node[0] in graph_:
            graph_[node[0]] = []
        if not node[1] in graph_:
            graph_[node[1]] = []
        graph_[node[0]].append(node[1])
        graph_[node[1]].append(node[0])

    vals = map(len, [x for x in graph_.values()])
    t = zip(graph_.keys(), vals)
    indegree = {j:cnt for j, cnt in t}
    print indegree

    q = collections.deque()
    for key, vals in indegree.items():
        if vals <= k-1:
            q.append(key)
    print k
    while q:
        node = q.popleft()
        del graph_[node]
        for v in graph_:
            if node in graph_[v]:
                indegree[v] -= 1
                if indegree[v] <= (k-1):
                    q.append(v)
        

    return graph_.keys()
    #indegree = {j:val for j in graph_.keys() for val in [lambda x: len(x) for x in graph_.values()]}
    


print getSubset(graph, 2)