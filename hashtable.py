A = ['a','b']
B = ['c','b','a']

def generatehash(A):
    hashA = {}
    for item in A:
        if item not in hashA:
            hashA[item] = 1
        else:
            hashA[item] += 1
    return hashA

def compareHash(A, B):
    lenA = len(A)
    lenB = len(B)
    hashA = generatehash(A)

    if lenB < lenA:
        return False
    elif lenB == lenA:
        return hashA == generatehash(B)
    else:
        for i in xrange(lenB-lenA+1):
            newB = B[i:i+lenA]
            if hashA == generatehash(newB):
                return True
    return False

print compareHash(A, B)
