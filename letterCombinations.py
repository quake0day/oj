class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
    	if len(digits) <= 0:
    		return []
        map = {
               "0":  (),
               "1":  (),
               "2": ("a", "b", "c"),
               "3": ("d", "e", "f"),
               "4": ("g", "h", "i"),
               "5": ("j", "k", "l"),
               "6": ("m", "n", "o"),
               "7": ("p", "q", "r", "s"),
               "8": ("t", "u", "v"),
               "9": ("w", "x", "y", "z")
               }
        result1 = [ "" ]
        result2 = [ ]
        for ch in digits:
            list = map[ch]
            if 0 == len(list):
                continue
            for str in result1:
                for suffix in list:
                    result2.append(str + suffix)
            result1 = result2
            result2 = [ ]
        return result1

a = Solution()
print a.letterCombinations('2')