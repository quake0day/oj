class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if len(A) <= 0:
            return False
        if len(B) <= 0:
            return True
        if len(B) > 1 and len(A) > 1:
        
            AA = [0] * 26
            BB = [0] * 26
            for i in xrange(len(A)):
                AA[ord(A[i]) - ord('A')] += 1
            for j in xrange(len(B)):
                BB[ord(B[i]) - ord('A')] += 1
                if BB[ord(B[i]) - ord('A')] > AA[ord(A[i]) - ord('A')]:
                    return False
            return True


a = Solution()
print a.compareStrings("A", "")