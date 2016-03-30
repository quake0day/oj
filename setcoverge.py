S = [(1,4), (30,40), (20, 91), (8, 10), (6, 7), (3,9 ), (9,12), (11,14)]
R = (3,13)

def getSetcoverage(S, R):
    S.sort()  #O(nlog(n))
    if len(S) == 0 or S[0][0] > R[0]:
        return []
    if S[0][1] >= R[1]:
        return [S[0]]

    ret = [] 
    start = R[0]
    end = S[0][1]
    greedy = S[0]

    for inter in S[1:]:
        if inter[0] <= start:
            if inter[1] > end:
                greedy = inter 
                end = inter[1]
                if end >= R[1]:
                    ret.append(greedy)
                    return ret 
        else:
            if inter[0] > end:
                return [] 
            ret.append(greedy)
            start = end 
            greedy = inter 
            end = inter[1]
            if end >= R[1]:
                ret.append(greedy)
                return ret 
    return []
print getSetcoverage(S, R)