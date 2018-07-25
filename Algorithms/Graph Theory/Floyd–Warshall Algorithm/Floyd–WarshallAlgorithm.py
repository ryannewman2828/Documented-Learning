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

dist = [[float('inf') for x in range(len(vertices))] for y in range(len(vertices))]
for e in edges:
    dist[int(e[0][0])][int(e[0][1])] = int(e[1])

for v in list(vertices.keys()):
    dist[int(v)][int(v)] = 0

for i in range(len(vertices)):
    for j in range(len(vertices)):
        for k in range(len(vertices)):
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

print(dist)
