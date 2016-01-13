class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        P = {"(":")", "{":"}","[":"]"}
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif P[stack.pop()] == i:
                    continue
                else:
                    return False
        return True



a = Solution()
print a.isValid("()")
print a.isValid("()]")    
        
print a.isValid("([)")    
