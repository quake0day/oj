a = [[2,5],[3,4],[4,1]]

def test(a):
    for i in a:
        for j in a:
            print i[0],j[0], i[1],j[1]
            if i[0] + j[0] == 6 and i[1] + j[1] == 6:
                return True 

print test(a)


def twoSum(a, target):
    t1 = {}
    t2 = {}
    for i in a:
        a,b = i
        if a in t1 and b in t2:
            return True 
        t1[target-a] = True
        t2[target-b] = True

print twoSum(a, 6)