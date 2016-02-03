class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses
        childs = [[] for _ in xrange(numCourses)]
        for pair in prerequisites:
        	degrees[pair[0]] += 1
        	childs[pair[1]].append(pair[0])
        courses = set(range(numCourses))
        flag = True 
        while flag and len(courses):
        	flag = False
        	removeList = []
        	for x in courses:
        		if degrees[x] == 0:
        			for child in childs[x]:
        				degrees[child] -= 1
        			removeList.append(x)
        			flag = True
        	for x in removeList:
        		courses.remove(x)
        return len(courses) == 0