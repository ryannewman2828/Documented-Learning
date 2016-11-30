#!bin/python
from functools import reduce

# program assumes valid input

class Vertex:
    name = ""
    edges = []
    saturated = False

    def __init__ (self, name, saturated):
        self.name = name
        self.saturated = saturated

    def addEdge (self, edge):
        self.edges.append(edge)

class Edge:
    def __init__(self, vertexA, vertexB):
        self.vertexA = vertexA
        self.vertexB = vertexB

VERTICE_FILE_NAME = "vertice.txt"
EDGES_FILE_NAME = "edge.txt"
MATCHING_FILE_NAME = "matching.txt"

vertices = [line.rstrip('\n') for line in open(VERTICE_FILE_NAME)]
edges = [line.rstrip('\n') for line in open(EDGES_FILE_NAME)]
matches = [line.rstrip('\n') for line in open(MATCHING_FILE_NAME)]

edges = list(map((lambda x: tuple(x)), edges))
matches = list(map((lambda x: tuple(x)), matches))

vertices = list(map(
    (lambda x: Vertex(
        x,
        reduce((lambda y, z: y or z[0] == x or z[1] == x), matches))),
    vertices))

for e in edges:
    for v in vertices:
        if v.name == e[0] or v.name == e[1]:
            v.addEdge(e)