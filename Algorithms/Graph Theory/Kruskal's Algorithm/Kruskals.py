#!bin/python

# https://codereview.stackexchange.com/questions/79208/disjoint-set-data-structure-in-python-3
class Disjoint:
    def __init__(self):
        self.sets = []

    def createSet(self, repr):
        self.sets.append([repr])

    def mergeSets(self, repr1, repr2):
        set1 = self.findSet(repr1)
        set2 = self.findSet(repr2)
        if set1 != set2:
            set1.extend(set2)
            self.sets.remove(set2)

    def findSet(self, repr1):
        for oneSet in self.sets:
            if repr1 in oneSet:
                return oneSet

    def getSets(self):
        return self.sets

# program assumes valid input
class Vertex:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        self.name == other.name


VERTICE_FILE_NAME = "vertice2.txt"
EDGES_FILE_NAME = "edge2.txt"

# init list
vertices = [Vertex(line.rstrip('\n')) for line in open(VERTICE_FILE_NAME)]
vertices = dict((v.name, v) for v in vertices)
edges = [tuple(line.rstrip('\n').split(" ")) for line in open(EDGES_FILE_NAME)]

A = []
sets = Disjoint()
for v in list(vertices.keys()):
    sets.createSet(v)

edges = sorted(edges, key=lambda x: int(x[1]), reverse=False)

for e in edges:
    if sets.findSet(e[0][0]) != sets.findSet(e[0][1]):
        A.append(e)
        sets.mergeSets(e[0][0], e[0][1])
print(A)
