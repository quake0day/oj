class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        key_length = len(key)
        value = 0
        w = 1
        j = key_length - 1
        for i in xrange(j, -1, -1):
            value = (value + ord(key[i]) * w) % HASH_SIZE
            w = (w*33) % HASH_SIZE
        return value


a = Solution()
print a.hashCode("abcd", 1000)