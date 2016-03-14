# a sample graph
graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F','D'],
             'F': ['C']}
graph2 = {'A': ['B', 'C'],
             'B': [ 'D'],
             'C': ['E'],
             'D': ['F'],
             'E': [],
             'F': []}
import collections
def checkcycle(graph):
    q = collections.deque(['A'])
    visited = {i:False for i in graph.keys()}
    while q:
        node = q.popleft()
        if visited[node] == True:
            return False
        else:
            for subnode in graph[node]:
                q.append(subnode)
                visited[node] = True
    return True

    

print checkcycle(graph)
print checkcycle(graph2)



graph_tasks = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }

def kahn_topsort(graph):
    indegree = {i:0 for i in graph.keys()}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    q = collections.deque()
    for u in indegree:
        if indegree[u] == 0:
            q.append(u)
    L = []
    while q:
        u =  q.popleft()
        L.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    if len(L) == len(graph):
        return L 
    else:
        return []

print kahn_topsort(graph_tasks)
