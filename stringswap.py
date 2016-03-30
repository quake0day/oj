s = "abcde"
t = "ebcda"


def lastMove(s, t):
    map1 = {val:key for key, val in enumerate(s)}

    print map1

lastMove(s,t)