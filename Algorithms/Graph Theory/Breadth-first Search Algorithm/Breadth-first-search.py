#!bin/python
from queue import Queue

# program assumes valid input
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def __ne__(self, other):
        return self.name != other.name

    def __repr__(self):
        return self.name

    def addNeighbour(self, vertex):
        self.neighbours.append(vertex)


def BFS(vertex):
    set = [vertex]
    queue = Queue()
    queue.put(vertex)
    while not queue.empty():
        current = queue.get()
        answer.append(current)
        for v in current.neighbours:
            if v not in set:
                set.append(v)
                queue.put(v)


VERTICE_FILE_NAME = "vertice.txt"
EDGES_FILE_NAME = "edge.txt"

# init list
vertices = [Vertex(line.rstrip('\n')) for line in open(VERTICE_FILE_NAME)]
vertices = dict((v.name, v) for v in vertices)
edges = [line.rstrip('\n') for line in open(EDGES_FILE_NAME)]

# convert to tuples
edges = list(map((lambda x: tuple(x)), edges))

# connect the vertices
for e in edges:
    vertices[e[0]].addNeighbour(vertices[e[1]])
    vertices[e[1]].addNeighbour(vertices[e[0]])

answer = []
node = input("Enter the starting node: ")
BFS(vertices[node])
print("Search starting from " + node + " Visited in the following order: ")
print(answer)
