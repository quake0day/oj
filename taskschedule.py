def taskSchedule(s, coolTime):
    h = {}
    t = 0
    for i in xrange(len(s)):
        if s[i] not in h or h[s[i]] + coolTime <= t:
            t += 1
            h[s[i]] = t 
        else:
            t = h[s[i]] + coolTime + 1
            h[s[i]] = t
        print h
    return t

print taskSchedule("AABABCD", 2)
print taskSchedule("AAB", 4)
print taskSchedule("1121", 2)
print taskSchedule("123123", 2)