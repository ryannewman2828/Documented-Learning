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

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __copy__(self):
        v = Vertex(self.name, self.saturated)
        v.neighbours = self.neighbours.copy()
        return v


def setMinus(set1, set2):
    return list(filter((lambda x: x not in set2), set1))


def inMatching(matching, v1, v2):
    return (matching[0] == v1.name and matching[1] == v2.name) or (matching[1] == v1.name and matching[0] == v2.name)

VERTICE_FILE_NAME = "vertice2.txt"
EDGES_FILE_NAME = "edge2.txt"
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
    setM = setMinus(verticesB.values(), Y)
    found = False
    vert = Vertex("", False)
    for v in setM:
        for u in X:
            if u in v.neighbours or v in u.neighbours:
                found = True
                vert = v
                Y.append(v)
                for i in pr:
                    if i[len(i) - 1] == u:
                        pr.append(i.copy())
                        i.append(v)
                        break
                break
        if found:
            break

    # We have found the maximum matching and minimum cover so we print it
    if not found:
        print("matching is:")
        for m in matches:
            print(m[0] + " " + m[1])
        print("Cover is:")
        for c in Y + setMinus(verticesA.values(), X):
            print(c.name)
        break

    #we have an M-augmenting path, so we make a larger matching
    if not vert.saturated:
        for i in pr:
            if i[len(i) - 1] == vert:
                for m in matches:
                    for j in range(0, len(i) - 1):
                        if inMatching(m, i[j], i[j + 1]):
                            matches.remove(m)
                m = 0
                i[0].saturated = True
                i[len(i) - 1].saturated = True
                for n in range(0, len(i)):
                    if n % 2 == 0:
                        m = i[n].name
                    else:
                        matches.append((m, i[n].name))

        X = list(filter((lambda x: not x.saturated), verticesA.values()))
        Y = []
        orig = X.copy()
        pr = [[x] for x in X]
        continue

    #
    setM = setMinus(verticesA.values(), X)
    found = False
    for w in setM:
        for z in Y:
            for m in matches:
                if inMatching(m, w, z) and not found:
                    X.append(w)
                    found = True
                    for i in pr:
                        if i[len(i) - 1] == z:
                            i.append(w)
