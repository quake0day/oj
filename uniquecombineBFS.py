import collections
def getCombineBFS(arr, n):
    q = collections.deque()
    length = len(arr)
    maxLevel = length / n
    final_res = []
    for i in range(n):
        q.append([[arr[i]], 0])
    while q:
        tmp, level = q.popleft()
        if level + 2 <= maxLevel:
            for i in range((level+1)*n, (level+2)*n):
                q.append([tmp+[arr[i]],level+1])
        else:
            final_res.append(tmp)
    return final_res



def getCombineDFS(arr, n):
    final_res = []
    maxLevel = len(arr) / n
    def dfs(level, tmp, final_res):
        if level == maxLevel:
            final_res.append(tmp)
            return 
        for i in xrange(n):
            dfs(level+1, tmp+[arr[level*n+i]], final_res)
    
    dfs(0, [], final_res)
    return final_res

print getCombineBFS([1,2,3,4,5,6], 2)
print getCombineDFS([1,2,3,4,5,6], 2)