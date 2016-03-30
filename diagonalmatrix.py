# 1 2 3
# 4 5 6
# print 3 2 6 1 5 4

def zigzagPrint(arr):
    # edge
    if not arr: return ""
    if len(arr) == 1: return ",".join(map(str, arr[0][::-1]))
    m = len(arr); n = len(arr[0])
    ans = []
    for x in reversed(range(1-m, n)):
        print x
        for i in range(m):
            for j in range(n)[::-1]:
                if j == x + i:
                    ans.append(arr[i][j])
    return ",".join(map(str, ans))


print zigzagPrint([[1,2,3],[4,5,6]])