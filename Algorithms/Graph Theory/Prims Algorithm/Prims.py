#!bin/python

VERTICE_FILE_NAME = "vertice.txt"
EDGES_FILE_NAME = "edge.txt"

# init inputs
vertices = [line.rstrip('\n') for line in open(VERTICE_FILE_NAME)]
edges = [tuple(line.rstrip('\n').split(" ")) for line in open(EDGES_FILE_NAME)]
vertex = input("Enter the starting vertices: ")

cheapMap = {}
edgesMap = {}
total = 0
forest = []

for v in vertices:
    cheapMap[v] = float('inf')
    edgesMap[v] = ""
cheapMap[vertex] = 0

while len(vertices) > 0:
    minimum = float('inf')
    v = vertices[0]
    for key in cheapMap:
        if cheapMap[key] < minimum:
            minimum = cheapMap[key]
            v = key
    vertices.remove(v)
    total += minimum
    if edgesMap[v] != "":
        forest.append(edgesMap[v])
    for edge in edges:
        if v in edge[0]:
            if edge[0][0] == v:
                w = edge[0][1]
            else:
                w = edge[0][0]
            if w in vertices and float(edge[1]) < cheapMap[w]:
                cheapMap[w] = float(edge[1])
                edgesMap[w] = edge[0]
    cheapMap.pop(v, None)
    edgesMap.pop(v, None)

print("Edges: ")
print(forest)
print("Total Weight: " + str(total))
