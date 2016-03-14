words= ['abcd','dcba','lls','s','sssll']
# O(n * k^2)
def findPalindromePair(words):
    pair = []
    for word in words:
        l = len(word)
        revstr = word[::-1]
        for i in xrange(l):
            if word[:(l-i+1)/2] == revstr[i:(l+i+1)/2]:
                candidate = revstr[:i]
                maybePair = sorted([word, candidate])
                if candidate in words and maybePair not in pair and word != candidate:
                    pair += [maybePair]
        maybePair = sorted([word, revstr])
        if revstr in words and maybePair not in pair and word != revstr:
            pair += [[word, revstr]]
    return pair
print findPalindromePair(words)
