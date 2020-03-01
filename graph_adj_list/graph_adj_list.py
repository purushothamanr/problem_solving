class AdjNode:
	def __init__(self, data= None):
		self.data = data
		self.next = None
	
		
class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [None]*self.V


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
	
	

if __name__ == "__main__":
	V = 5
	graph = Graph(5)
	graph.add_edge(0,1)
	graph.add_edge(0,2)
	graph.add_edge(0,3)
	graph.add_edge(1,2)
	graph.add_edge(1,3)
	graph.add_edge(2,4)
	graph.add_edge(3,4)
	
	graph.print_graph()

