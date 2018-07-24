# Bellman-Ford Algorithm
The Bellman-Ford Algorithm is used for solving the Single Source Shortest Path problem. 
This differs from Dijkstra's because this algorithm works when the graph has negative edge weights.
When the graph has a negative cycle, there is no cheapest path and so this algorithm can report there existence.
This algorithm uses the principle of relaxation where it starts with an approximation and then tightens to the optimal value.
The distance for every path from v to the source is overestimated in the array and is then replaced if a smaller value is found.
The runtime of this algorithm is O(|V| * |E|) in the worst case.
