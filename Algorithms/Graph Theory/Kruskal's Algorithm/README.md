# Kruskal's Algorithm
Kruskal's Algorithm finds the minimum spanning tree in a graph by using a greedy approach.
The algorithm works by sorting the edges in increasing order by their weights and adding it to the MST 
if there is not already a path between the 2 vertices being connected. 
This finds the subset of the edges that connects every vertice with a minimum weight.
This makes use of the disjoint-set data structure to arrive at its runtime.
The runtime of this algorithm is O(|E| * log(|V|)).

