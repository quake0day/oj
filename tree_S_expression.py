class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None



class Solution(object):
	def SExp(self, pair):
		links = [[None, None, None] for _ in xrange(26)]
		edges = pair.split(";")
		for edge in edges:
			edge = edge.replace('(','').replace(')','').replace(' ','')
			a,b = edge.split(',')

			# Change node value into index 
			a = ord(a) - ord('A')
			b = ord(b) - ord('A')
			if a < 0 or a > 25 or b < 0 or b > 25:
				raise Exception("E5: invalid node value")

			# multiple roots
			if links[b][0]:
				raise Exception ('E4')

			# record the father node for a certain node 
			links[b][0] = a 

			# record father's child node

			if links[a][1] == None:
				links[a][1] = b
			elif links[a][2] == None:
				if b < links[a][1]:
					links[a][2] = b
				else:
					links[a][2] = links[a][1]
					links[a][1] = b 
			elif links[a][1] == b or links[a][2] == b:
				raise Exception('E2')
			else:
				raise Exception('E1')


		# find root 
		root = None
		for idx in range(26):
			parent, child1, child2 = links[idx]
			if parent == None and (child1 != None or child2 != None):
				if root:
					raise Exception('E5: multiple tree!')

				root = idx 


		if root == None:
			raise Exception("E3") # no root -> cycle present

		# avoid cycle, all the nodes should not appears in the same level or higher level 
		seen = [False for i in xrange(26)] 
		layer = [root]
		while layer:
			tmpLayer = []
			for node in layer:
				if seen[node]:
					raise Exception("E3")
				seen[node] = True
				if links[node][1] != None:
					tmpLayer.append(links[node][1])
					if links[node][2] != None:
						tmpLayer.append(links[node][2])
			layer = tmpLayer

		def output(node):
			if links[node][1] == None:
				return "(%s)" % (chr(65+node))
			tmp = output(links[node][1])
			if links[node][2] == None:
				return "(%s%s)" % (chr(65+node), tmp)
			tmp2 = output(links[node][2])
			return "(%s%s%s)" % (chr(65 + node), tmp2, tmp)
		return output(root)



a = Solution()
print a.SExp("(A,B);(A,C);(B,G);(C,H);(E,F);(B,D);(C,E)")