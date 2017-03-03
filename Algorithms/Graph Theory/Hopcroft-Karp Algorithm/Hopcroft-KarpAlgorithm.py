#!bin/python
from functools import reduce


# program assumes valid input
class Vertex:
    def __init__(self, name, saturated):
        self.name = name
        self.saturated = saturated
        self.neighbours = []

    def addNeighbour(self, vertex):
        self.neighbours.append(vertex)

    def __eq__(self, other):
        return self.name == other.name

    def __copy__(self):
        v = Vertex(self.name, self.saturated)
        v.neighbours = self.neighbours.copy()
        return v


def setMinus(set1, set2):
    return list(filter((lambda x: x not in set2), set1))


def inMatching(matching, v1, v2):
    return (matching[0] == v1.name and matching[1] == v2.name) or (matching[1] == v1.name and matching[0] == v2.name)

VERTICE_FILE_NAME = "vertice.txt"
EDGES_FILE_NAME = "edge.txt"
MATCHING_FILE_NAME = "empty.txt"

# init list
vertices = [line.rstrip('\n') for line in open(VERTICE_FILE_NAME)]
edges = [line.rstrip('\n') for line in open(EDGES_FILE_NAME)]
matches = [line.rstrip('\n') for line in open(MATCHING_FILE_NAME)]

# convert to tuples
edges = list(map((lambda x: tuple(x)), edges))
matches = list(map((lambda x: tuple(x)), matches))

# create bipartition
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

# init vertices
verticesA = dict((
    v, Vertex(
        v, reduce((lambda y, z: y or z[0] == v or z[1] == v), [False] + matches))) for v in A)

verticesB = dict((
    v, Vertex(
        v, reduce((lambda y, z: y or z[0] == v or z[1] == v), [False] + matches))) for v in B)

# set every vertices neighbours
for e in edges:
    if e[0] in verticesA:
        verticesA[e[0]].addNeighbour(verticesB[e[1]])
        verticesB[e[1]].addNeighbour(verticesA[e[0]])
    if e[0] in verticesB:
        verticesB[e[0]].addNeighbour(verticesA[e[1]])
        verticesA[e[1]].addNeighbour(verticesB[e[0]])

X = list(filter((lambda x: not x.saturated), verticesA.values()))
Y = []
orig = X.copy()
pr = [[x] for x in X]

while True:
    # Create a level in our alternating level graph
    l = []
    for strand in pr:
        v = strand[len(strand) - 1]
        for u in v.neighbours:
            if u not in Y:
                s = strand.copy()
                s.append(u)
                l.append(s)
                Y.append(u)
    found = len(l) == 0
    pr = l

    # We have found the maximum matching and minimum cover so we print it
    if found:
        print("matching is:")
        for m in matches:
            print(m[0] + " " + m[1])
        print("Cover is:")
        for c in Y + setMinus(verticesA.values(), X):
            print(c.name)
        break

    # we have an augmenting path
    vertex = Vertex("", False)
    cont = False
    s = []
    for strand in pr:
        v = strand[len(strand) - 1]
        if not v.saturated:
            cont = True
            s = strand
    if cont:
        for m in matches:
            for j in range(len(s) - 1):
                if inMatching(m, s[j], s[j + 1]):
                    matches.remove(m)
        m = ""
        s[0].saturated = True
        s[len(s) - 1].saturated = True
        for n in range(len(s)):
            if n % 2 == 0:
                m = s[n].name
            else:
                matches.append((m, s[n].name))
        X = list(filter((lambda x: not x.saturated), verticesA.values()))
        Y = []
        pr = [[x] for x in X]
        continue

    # Create the matching layer of our alternating level graph
    for strand in pr:
        v = strand[len(strand) - 1]
        for u in v.neighbours:
            for m in matches:
                if inMatching(m, u, v):
                    strand.append(u)
                    X.append(u)
