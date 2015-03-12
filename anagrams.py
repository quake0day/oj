class Solution:
    # @param strs: A list of strings
    # @return: A list of strings

    #TLE
    # def anagrams(self, strs):
    #     # write your code here
    #     if len(strs) <= 1:
    #         return strs
    #     final_res = []
    #     for i in xrange(len(strs)):
    #         for j in xrange(i):
    #             if i != j:
    #                 if self.anagram(strs[i], strs[j]) == True:
    #                         final_res.append(strs[i])
    #                         final_res.append(strs[j])

    #     final_res = list(set(final_res))
    #     real_final_res = []
    #     for item in strs:
    #         if item in final_res:
    #             real_final_res.append(item)
    #     return real_final_res



    # def anagram(self, s, t):
    #     list_s = list(s)
    #     list_t = list(t)
    #     for item in list_s:
    #         try:
    #             list_t.remove(item)
    #         except:
    #             return False
    #     if len(list_t) == 0:
    #         return True
    def anagrams(self, strs):
        ret = []
        if strs == None:
            return ret

        hmap = {}
        len_ = len(strs)
        for i in xrange(len_):
            s = strs[i]

            chars = list(s)
            strSort = "".join(sorted(chars))

            if strSort not in hmap:
                new_list = []
                hmap[strSort] = new_list
            hmap.get(strSort).append(s)
        final_res = []
        for item in hmap.values():
            if len(item) == 1:
                continue
            
            final_res += item
        return final_res










a = Solution()
print a.anagrams(["",'b',""])
print a.anagrams(["tea","and","ate","eat","den"])
print a.anagrams(["tea","","eat","","tea",""])