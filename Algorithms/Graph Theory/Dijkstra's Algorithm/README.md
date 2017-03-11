# Dijkstra's Algorithm
Dijkstra's Algorithm is an algorithm for finding the shortest path between two vertices in a graph. This algorithm has many different variants, examples include versions that return the distance between two vertices and another that returns a map with the distance between an initial node and every other node in the graph. The runtime of this algorithm is O(|V|<sup>2</sup>) not using a min-priority queue and runs O(|E| + |V| log |V|) using a min-priority queue. The algorithm works by when on a current node, it considers all unvisited neighbours and calculates the distance to that node. This new tentative distance is compared to the previous shortest distance for that node, if there even is a previous shortest distace for that node. When this finishes, the current node is marked visited and then another node with the smallest tentative distance is chosen as the next current node. This process continues until the target node is visited or there is no smallest distance from the current node to anything in the set of unvisited nodes. This algorithm is often used in routing protocols to find the shorest distance between cities connected by roads. Another usage of this is in the field of artifical intelligence as uniform-cost search. 