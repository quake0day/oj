


def encode(strs):
    return "".join('%d' % len(s) + s for s in strs)
def encode1( strs):
    """Encodes a list of strings to a single string.
    
    :type strs: List[str]
    :rtype: str
    """
    encoded_str = ""
    for s in strs:
        encoded_str += "%0*x" % (8, len(s)) + s
    return encoded_str

def encode3(strs):
    res = ""
    count = 1
    for i in xrange(1, len(strs)):
        if strs[i-1] == strs[i]:
            count += 1
        else:
            if count == 1:
                res += strs[i-1]
                count = 1
            else:
                res += (str(count) + strs[i-1]) 
                count = 1

    res += str(count) + strs[-1] if count > 1 else strs[-1]
    
    print res


print encode3("abaa")

print encode3("aabbbccd")

def getLCM(a, b):
    return (a*b)/getGCD(a,b)

def getGCD(a,b):
    if a == b: return a
    if a > b: return getGCD(a-b, b)
    else:
        return getGCD(a, b-a)

