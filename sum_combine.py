#
#
#
#
#
#


def allSumCombine(n):
    allSet = [i for i in xrange(1,n+1)]
    def dfs(tmp, final_res, tmpVal):
        if tmpVal == 0:
            if sorted(tmp) not in final_res:
                final_res.append(sorted(tmp))
            return 
        for item in allSet:
            if tmpVal - item >= 0:
                dfs(tmp+[item], final_res, tmpVal-item)
    final_res = []
    for i in allSet:
        dfs([i], final_res, 10-i)
    res = []
    for item in final_res:
        for i in xrange(len(item)):
            if i == 0:
                temp = str(item[i])
            elif i > 0:
                temp += "+"+str(item[i])
        res.append(temp)
    return res


print allSumCombine(10)