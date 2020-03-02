class AdjNode:
	def __init__(self, data= None):
		self.data = data
		self.next = None
	
		
class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [None]*self.V
		self.visited = [None]*self.V

	def add_edge(self, src, dest):
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node

	def print_graph(self):
		for i in range(self.V):
			print("Vertex" , i, "is connected to")
			head = self.graph[i]
			while head:
				print(head.data, " ")
				head = head.next

	def depth_first_search(self, at):
		
		if self.visited[at]:
			self.visited[at] += 1
			return

		self.visited[at] = 1

		adj_node = self.graph[at]
		while adj_node:
			self.depth_first_search(adj_node.data)
			adj_node = adj_node.next

	def print_visited_count(self):
		for i in range(self.V):
			print("Visited Count of", i, "is", self.visited[i])		

	

if __name__ == "__main__":
	V = 4
	graph = Graph(V)
	graph.add_edge(0,1)
	graph.add_edge(1,2)
	graph.add_edge(1,3)
	graph.add_edge(2,3)

	graph.print_graph()

	graph.depth_first_search(3)
	graph.print_visited_count()
