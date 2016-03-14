class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.final_res = []
        if not num or not target:
            return []
        def dfs(num, target, tmp, curr, prev):
           if num == 0 and curr == target:
               self.final_res.append(tmp)

        
            
          
        
        