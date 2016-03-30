def getCoinCount(amount, coins):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    print dp
    for i in xrange(amount):
        for c in coins:
            if i + c > amount:
                continue
            dp[i+c] = min(dp[i+c], dp[i]+1)
    return dp



def change(n, coins_available, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass 
    else:
        for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c 
        for c in change(n, coins_available[1:], coins_so_far):
            yield c 

amount = 40
coins = [1,5,15,25]
print [s for s in change(amount, coins, [])]



def testy(x):
    x += 1
    if x == 100:
        yield x
    else:
        for x in testy(x):
            yield x
print [x for x in testy(10)]
# print getCoinCount(amount, coins)

# target = 1
# k = 2
# len_ = 99
# DP = [[[0]*(target+1) for _ in xrange(k+1)] for _ in xrange(len_+1)]
# print DP