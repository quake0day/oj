def magicNumber(n):
    if n < 1:
        return 1
    return magicNumber(n-1) + 2*magicNumber(n-3)


print magicNumber(5)


#def newMagic(n, k):
    #return magicNumber(n-1) + 2 * magicNumber(n-k)


def newMagic(n, k):
    # if k = 3
    return magicNumber(n-1) + 2 * magicNumber(n-2) + 2 * magicNumber(n-3)
#print newMagic(5, 2)