class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write you code here

        len_A = len(A)
        del_ = [False] * len_A

        for i in xrange(0,k):
            prev = -1
            prev_index = -1
            hasDel = False
            for j in xrange(len_A):
                if del_[j]:
                    continue
                num = int(A[j])
                if (num >= prev):
                    prev = num
                    prev_index = j
                else:
                    break
            del_[prev_index] = True
        string_final = []
        for i in xrange(len_A):
            if del_[i] == False:
                string_final.append(A[i])
        return str(int("".join(str(e) for e in string_final)))



        # stack_ = []
        # length = len(A)
        # if length == k:
        #     return ""


        # for i in xrange(len(A)):
        #     num = int(A[i])
        #     if len(stack_) == 0:
        #         stack_.append(num)
        #     elif num >= stack_[-1] and k > 0:
        #         stack_.append(num)
        #     elif num < stack_[-1] and k > 0:
        #         stack_.pop()
        #         stack_.append(num)
        #         k -= 1
        #     else:
        #         stack_.append(num)
        # i = len(A) - 1
        # while k > 0 and i > -1:
        #      stack_.pop()



        return "0"



            
        # for i in xrange(len(A)):
        #     num = int(A[i])
        #     if len(st) == 0:
        #         st.append(num)
        #     elif num >= st[-1]:
        #         st.append(num)
        #     else:
        #         if pop_count < k:
        #             st.pop()
        #             i -= 1
        #             pop_count += 1
        #         else:
        #             st.append(num)

        # while pop_count < k:
        #     res.append(st.pop())
        #     pop_count += 1

        # string_final = "".join(str(e) for e in res)[::-1]
        # return string_final

        # for i in xrange(1,len(A)):
        #     if int(rev_A[i-1]) < int(rev_A[i]) and k != 0:
        #         rev_A[i] = rev_A[i-1]
        #         k -= 1
        #     elif int(rev_A[i-1]) > int(rev_A[i]) and k != 0:
        #         pass
        #     elif k == 0:
        #         print rev_A[i]



a = Solution()
print a.DeleteDigits("90249", 2)
print a.DeleteDigits("123456789", 1)
print a.DeleteDigits("87654321", 2)
print a.DeleteDigits("178542", 4)