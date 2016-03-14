def longest(s):
    hashmap = {}
    start = 0
    maxLen = 0
    for i in range(len(s)):
        c = s[i]
        if len(hashmap) == 2 and c not in hashmap:
            charEndsMostLeft = " "
            minLast = len(s)
            for ch in hashmap.keys():
                last = hashmap[ch]
                if last < minLast:
                    minLast = last
                    charEndsMostLeft = ch 
            del hashmap[charEndsMostLeft]
            start = minLast + 1

        hashmap[c] = i 
        maxLen = max(maxLen, i - start + 1)
    return maxLen 



def longestK(s, k):
    start = 0
    maxLen = 0 

    hashmap = {}
    for i in xrange(len(s)):
        c = s[i]
        if c in hashmap:
            hashmap[c] += 1
        else:
            hashmap[c] = 1 
            while (len(hashmap) > k):
                startChar = s[start]
                start += 1
                count = hashmap[startChar]
                if count > 1:
                    hashmap[startChar] -= 1
                else:
                    del hashmap[startChar]
    maxLen = max(maxLen, i - start + 1)



s = "eceba"
print longest(s)