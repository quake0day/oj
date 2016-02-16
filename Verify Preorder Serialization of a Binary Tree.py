class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        diff = 1
        for node in nodes:
            if diff - 1 < 0:
                return False 
            diff -= 1
            if not node == '#':
                diff += 2
        return diff == 0

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for x in preorder.split(","):
            stack += [x]
            while len(stack) >= 3 and stack[-2:] == ['#', '#'] and stack[-3] != '#':
                stack = stack[:-3] + ['#']
        return len(stack) == 1 and stack[0] == '#'
a = Solution()
print a.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")