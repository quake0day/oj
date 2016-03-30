x = [('parker', 'parker'), ('laks', 'parker'), ('avinash', 'laks'), ('jonathan', 'avinash'), ('jason', 'laks'), ('david', 'parker'), ('arisa', 'david') ]


def buildGraph(x):
    graph = {}
    for ele in x:
        if ele[0] == ele[1]:
            graph['boss'] = [ele[0]]
        elif graph.get(ele[1], []):
            graph[ele[1]].append(ele[0])
        else:
            graph[ele[1]] = [ele[0]]
    print graph
    return graph

graph = buildGraph(x)

def dfs(graph):
    stack = []
    visited = set()
    for boss in graph['boss']:
        stack.append([0, boss])

    while stack:
        count, boss = stack.pop()
        if boss not in visited:
            visited.add(boss)
            print " "*count, boss
            if graph.get(boss, None):
                for employee in graph[boss]:
                    if employee not in visited:
                        stack.append([count+1, employee])
dfs(graph)
