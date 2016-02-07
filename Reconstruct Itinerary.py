import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        print targets
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
                print airport 
            route.append(airport)
        visit('JFK')
        return route[::-1]


a = Solution()
tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print a.findItinerary(tickets1) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
print a.findItinerary(tickets2)