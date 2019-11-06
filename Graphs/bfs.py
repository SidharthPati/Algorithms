from collections import defaultdict


class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def bfs(self, s):
		visited_nodes = [False]*len(self.graph)

		final_answer = list()

		queue = [s]
		visited_nodes[s] = True
		final_answer.append(s)

		while queue:
			node = queue.pop(0)

			for child in self.graph[node]:
				if not visited_nodes[child]:
					final_answer.append(child)
					visited_nodes[child] = True
					queue.append(child)

		return final_answer


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print(g.bfs(2))
