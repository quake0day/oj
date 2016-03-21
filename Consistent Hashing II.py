import random
class Solution:

    # @param {int} n a positive integer
    # @param {int} k a positive integer
    # @return {Solution} a Solution object
    @classmethod
    def create(cls, n, k):
        # Write your code here
        cls.n = n
        cls.k = k
        cls.valuelist = [i for i in xrange(cls.n)]
        cls.h = {}
        return cls


    # @param {int} machine_id an integer
    # @return {int[]} a list of shard ids
    def addMachine(self, machine_id):
        # write your code here
        res = random.sample(self.valuelist,  self.k)
        for e in res:
            self.h[e] = machine_id
            self.valuelist.remove(e)
        return res


    # @param {int} hashcode an integer
    # @return {int} a machine id
    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        while hashcode not in self.h:
            hashcode += 1
        return self.h[hashcode]
a = Solution()
print a.create(100,3)
print a.addMachine(1)
print a.getMachineIdByHashCode(4)
print a.addMachine(2)
print a.getMachineIdByHashCode(61)
print a.getMachineIdByHashCode(91)
