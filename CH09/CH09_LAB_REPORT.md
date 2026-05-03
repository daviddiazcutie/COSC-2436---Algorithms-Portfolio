# Chapter 9: Dijkstra's Algorithm — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 04/12/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Dijkstra's algorithm finds the shortest path between a starting node and all other nodes in a weighted graph. It works by maintaining a table of the current known shortest distance to each node, always visiting the unvisited node with the smallest known distance next, and updating neighbor distances if a shorter path is found through the current node.
- **Time complexity:** O(V²) with a simple implementation, or O((V + E) log V) with a priority queue, where V is the number of vertices and E is the number of edges.
- **When to use it:** Dijkstra's algorithm is well-suited for finding shortest paths in graphs with non-negative edge weights, such as GPS navigation, network routing, and map applications.

## Test Results

```
=== Dijkstra's Algorithm — Shortest Path Demo ===

Graph:
  Start → A (weight 6)
  Start → B (weight 2)
  A     → Finish (weight 1)
  B     → A (weight 3)
  B     → Finish (weight 5)

Running Dijkstra from 'Start' to 'Finish'...

Distances from Start:
  Start  : 0
  B      : 2
  A      : 5
  Finish : 6

Shortest path: Start → B → A → Finish
Total cost:    6
```

| Source | Destination | Shortest Distance | Path                        |
|--------|-------------|-------------------|-----------------------------|
| Start  | A           | 5                 | Start → B → A               |
| Start  | B           | 2                 | Start → B                   |
| Start  | Finish      | 6                 | Start → B → A → Finish      |

## Reflection Questions

1. **Why can't Dijkstra's algorithm handle negative edge weights?**
   Dijkstra's algorithm assumes that once a node is marked as visited with a known shortest distance, that distance cannot be improved further. A negative edge weight can create a situation where revisiting an already-settled node would yield a shorter path, which violates that assumption and causes the algorithm to produce incorrect results. The Bellman-Ford algorithm is the standard alternative for graphs that contain negative weights.

2. **What is the role of the "costs table" in Dijkstra's algorithm?**
   The costs table tracks the current best-known distance from the start node to every other node in the graph. It is initialized with infinity for all nodes except the start node, which is set to zero. As the algorithm progresses, it continuously updates the costs table whenever it finds a shorter path to a neighbor, ensuring the final values represent the true shortest distances.

3. **How does Dijkstra's algorithm differ from Breadth-First Search (BFS)?**
   BFS finds the path with the fewest edges between two nodes but treats all edges as having equal weight. Dijkstra's algorithm extends this idea to weighted graphs by always prioritizing the lowest-cost path rather than the fewest hops. This makes Dijkstra's more suitable for real-world problems like GPS routing where roads have different distances or travel times.

## Challenges Encountered
The most challenging part of this lab was correctly initializing the costs and parents tables and ensuring the algorithm always selected the unvisited node with the lowest current cost at each step. Tracking which nodes had already been processed was easy to overlook, and forgetting to mark a node as visited caused the algorithm to re-process it and produce incorrect distances. Working through a small example graph by hand first — tracing each step manually before running the code — helped clarify the logic and made debugging significantly easier.
