import operator
class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        hashtable = {}
        for word in words:
            if word not in hashtable:
                hashtable[word] = 1
            else:
                hashtable[word] += 1
        sorted_x = sorted(hashtable.items(), key=operator.itemgetter(1), reverse=True)
        i = 0
        final_res = []
        while i < k:
            final_res.append(sorted_x[i][0])
            i += 1
        return final_res


a = Solution()
print a.topKFrequentWords([
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
], 4)