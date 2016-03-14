prices = [2, 1, 2, 1, 2, 1]
total = 0
for i in xrange(1, len(prices), 2):
    total += prices[i] - prices[i-1]

print total