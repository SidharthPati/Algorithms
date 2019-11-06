from collections import defaultdict


class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.final_list = list()

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def dfs_util(self, s, visited_nodes):
		visited_nodes[s] = True
		self.final_list.append(s)

		for node in self.graph[s]:
			if not visited_nodes[node]:
				self.dfs_util(node, visited_nodes)


	def dfs(self, s):
		visited_nodes = [False]*len(self.graph)
		self.dfs_util(s, visited_nodes)
		return self.final_list


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print(g.dfs(2))
