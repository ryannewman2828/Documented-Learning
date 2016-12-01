#!bin/python
from functools import reduce


# program assumes valid input
class Vertex:
    def __init__ (self, name, saturated):
        self.name = name
        self.saturated = saturated
        self.neighbours = []

    def addNeighbour (self, vertex):
        self.neighbours.append(vertex)


def setMinus(set1, set2):
    return list(filter((lambda x: x not in set2), set1))

VERTICE_FILE_NAME = "vertice.txt"
EDGES_FILE_NAME = "edge.txt"
MATCHING_FILE_NAME = "matching.txt"

# init list
vertices = [line.rstrip('\n') for line in open(VERTICE_FILE_NAME)]
edges = [line.rstrip('\n') for line in open(EDGES_FILE_NAME)]
matches = [line.rstrip('\n') for line in open(MATCHING_FILE_NAME)]

# convert to tuples
edges = list(map((lambda x: tuple(x)), edges))
matches = list(map((lambda x: tuple(x)), matches))

# create bipartition
#todo optimize this
A = [vertices[0]]
B = []
for e in edges:
    if e[0] in A and e[1] not in B:
        B.append(e[1])
    elif e[0] in B and e[1] not in A:
        A.append(e[1])
    elif e[1] in A and e[0] not in B:
        B.append(e[0])
    elif e[1] in B and e[0] not in A:
        A.append(e[0])
    elif e[0] not in A and B and e[1] not in A and B:
        # cant determine so move to the back
        edges.append(e)

#init vertices
verticesA = dict((
    v, Vertex(
        v, reduce((lambda y, z: y or z[0] == v or z[1] == v), [False] + matches))) for v in A)

verticesB = dict((
    v, Vertex(
        v, reduce((lambda y, z: y or z[0] == v or z[1] == v), [False] + matches))) for v in B)

for e in edges:
    if e[0] in verticesA:
        verticesA[e[0]].addNeighbour(verticesB[e[1]])
        verticesB[e[1]].addNeighbour(verticesA[e[0]])
    if e[0] in verticesB:
        verticesB[e[0]].addNeighbour(verticesA[e[1]])
        verticesA[e[1]].addNeighbour(verticesB[e[0]])

X = list(filter((lambda x: not x[1].saturated), verticesA.items()))
Y = []

#while True:

