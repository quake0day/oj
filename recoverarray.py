
toRec = [0, 1, 2, 1, 0]
candidateList = [i for i in xrange(1, len(toRec)+1)][::-1]
final_res = []
for j in xrange(len(toRec)-1, -1, -1):
    final_res += [candidateList[toRec[j]]]
    candidateList.remove(final_res[-1])
print final_res[::-1]


