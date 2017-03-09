#!bin/python


# program assumes valid input
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.distance = float('inf')

    def __eq__(self, other):
        self.name == other.name

    def addNeighbour(self, vertex):
        self.neighbours.append(vertex)



VERTICE_FILE_NAME = "vertice.txt"
EDGES_FILE_NAME = "edge.txt"

# init list
vertices = [Vertex(line.rstrip('\n')) for line in open(VERTICE_FILE_NAME)]
vertices = dict((v.name, v) for v in vertices)
edges = [tuple(line.rstrip('\n').split(" ")) for line in open(EDGES_FILE_NAME)]
vertex = input("Enter the starting vertex: ")
target = input("Enter the target vertex: ")

# connect the vertices
for e in edges:
    vertices[e[0][0]].addNeighbour(vertices[e[0][1]])
    vertices[e[0][1]].addNeighbour(vertices[e[0][0]])

current = vertices[vertex]
current.distance = 0
unvisited = list(vertices.values())
unvisited.remove(current)

while True:
    for v in current.neighbours:
        if v in unvisited:
            dist = current.distance
            for e in edges:
                if (e[0][0] == v.name and e[0][1] == current.name) or (e[0][1] == v.name and e[0][0] == current.name):
                    dist += e[1]
                    break
            if dist < v.distance:
                v.distance = dist

    if current.name == target:
        print(current.distance)
        break

    unvisited.remove(current)
    minimum = float('inf')
    index = -1
    for i in range(len(unvisited)):
        if unvisited[i].distance < minimum:
            minimum = unvisited[i].distance
            index = i
    if index == -1:
        print("No Connection point in the graph")
        break
    current = unvisited[index]
