class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return rooms
        q = []
        m = len(rooms)
        n = len(rooms[0])
        
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    q.append((i,j,0))
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        while q:
            (x, y, dis) = q.pop()
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] != -1 and rooms[nx][ny] != 0:
                    rooms[nx][ny] = min(rooms[nx][ny], dis+1)
                    q.append((nx, ny, dis+1))
        return rooms



rooms = [
         [float("Inf"),  -1 , 0 , float("Inf")],
         [float("Inf"), float("Inf") ,float("Inf"),  -1],
         [float("Inf"),  -1 ,float("Inf"),  -1],
         [0,  -1, float("Inf"), float("Inf")]
         ]

test = Solution()
test.wallsAndGates(rooms)
print rooms
            