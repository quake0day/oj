# class Solution(object):
#     def reverseWords(self, s):
#         """
#         :type s: a list of 1 length strings (List[str])
#         :rtype: nothing
#         """
#         stack = []
#         final_string = ""
#         for item in s:
#             if item != " ":
#                 stack.append(item)
#             else:
#                 while len(stack) != 0:
#                     final_string += stack.pop()
#                 final_string += " "
#         while(len(stack)) != 0:
#             final_string += stack.pop()
#         final_string += " "
#         return final_string[::-1]

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        for i in xrange(len(s) / 2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        return s
        
a = Solution().reverseWords(['t','h','e'])
print a