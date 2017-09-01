class Graph:
    def __init__(self):
        self.adjacency = {}

    def connect(self, vertex1, vertex2, weight=None):
        if vertex1 not in self.adjacency:
            self.adjacency[vertex1] = {}

        self.adjacency[vertex1][vertex2] = weight

    def is_vertex(self, vertex):
        return vertex in self.adjacency

    def are_connected(self, vertex1, vertex2):
        return self.is_vertex(vertex1) and vertex2 in self.adjacency[vertex1]

    def weight(self, vertex1, vertex2):
        return self.adjacency[vertex1][vertex2]

    def neighbors(self, vertex1):
        return self.adjacency[vertex1].keys()

# Test Code
G = Graph()

G.connect('A', 'B')
G.connect('A', 'C')
G.connect('B', 'C')
G.connect('C', 'D')

print(G.are_connected('A', 'B')) # True
print(G.are_connected('B', 'A')) # False, because the graph is directed!
print(G.are_connected('A', 'C')) # False, because there is no direct connection
print(G.neighbors('A')) # ['C', 'B']
