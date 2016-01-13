class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if len(image) == 0:
            return 0
        top = self.searchV(image, 0, x, True)
        bot = self.searchV(image, x+1, len(image), False)
        left = self.searchH(image, 0, y, top, bot, True)
        right = self.searchH(image, y+1, len(image[0]), top, bot, False)
        return (left-right) * (bot - top)
        
    
    def searchV(self, image, low, high, opt):
        while low < high:
            mid = (low + high) / 2
            if '1' in image[mid] == opt:
                high = mid
            else:
                low = mid + 1
        return low
        
        
    
    def searchH(self, image, low, high, top, bot opt):
        while low < high:
            mid = (low + high) / 2
            found = False
            for i in xrange(top, bot):
                if image[i][mid] == '1':
                    if opt:
                        high = mid
                    else:
                        low = mid + 1
                    found = True
                    break
            if not found:
                if opt:
                    low = mid + 1
                else:
                    high = mid
        return low
