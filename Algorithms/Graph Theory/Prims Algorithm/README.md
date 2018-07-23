# Prim's Algorithm
Prim's Algorithm is a greedy algorithm for finding a minimum spanning tree in a connected directed graph.
The algorithms output is the subset of edges with minimum weighting that makes a tree including all of the vertices in the graph.
It also outputs the minimum weighting as a direct result.
The algorithm functions by finding the cheapest edge leading to a vertex not currently in the subset from a vertex in the subset.
The vertex with this edge not in the subset is then added to the subset.
This process is completed until every vertex is in the subset and thusly a tree is formed.
