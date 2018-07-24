#!bin/python


# program assumes valid input
class Vertex:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        self.name == other.name


VERTICE_FILE_NAME = "vertice.txt"
EDGES_FILE_NAME = "edge.txt"

# init list
vertices = [Vertex(line.rstrip('\n')) for line in open(VERTICE_FILE_NAME)]
vertices = dict((v.name, v) for v in vertices)
edges = [tuple(line.rstrip('\n').split(" ")) for line in open(EDGES_FILE_NAME)]
source = input("Enter the starting vertex: ")

distance = {}
predecessor = {}

for v in list(vertices.keys()):
    distance[v] = float('inf')
    predecessor[v] = None

distance[source] = 0

for i in range(1, len(vertices)):
    for e in edges:
        if distance[e[0][0]] + int(e[1]) < distance[e[0][1]]:
            distance[e[0][1]] = distance[e[0][0]] + int(e[1])
            predecessor[e[0][1]] = e[0][0]

for e in edges:
    if distance[e[0][0]] + int(e[1]) < distance[e[0][1]]:
        print("Graph contains a negative-weight cycle")
        exit(1)

print(distance)
print(predecessor)
