# Chapter 6: Breadth-First Search (BFS) — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 03/03/26
- **Course:** COSC 2436

## Key Concepts

**Adjacency List:** A way to represent a graph where each node (City) points to a list of its direct neighbors (Highways). It is much more memory-efficient than a matrix for sparse graphs like road networks, since only existing connections are stored rather than every possible pair of nodes.

**Breadth-First Search (BFS):** An algorithm that traverses a graph layer by layer, exploring all neighbors of the current node before moving on to neighbors of neighbors. Because it always processes nodes in the order they were discovered, it is guaranteed to find the shortest path (by number of edges) in an unweighted graph.

**Queue (FIFO):** The data structure used to keep track of which nodes to visit next. Because it is First-In, First-Out, BFS always finishes the current "level" of neighbors before moving deeper into the graph. Python's `collections.deque` is used here for efficient O(1) pops from the front.

## Test Results

```
============================================================
PART 1: TEXAS ROAD NETWORK GRAPH
============================================================

Created graph with 10 cities

============================================================
PART 2: SHORTEST PATH (BFS)
============================================================

Houston → El Paso
Route: Houston → San Antonio → El Paso

----------------------------------------
Houston → McKinney
Route: Houston → Dallas → McKinney

============================================================
PART 3: DISTANCES FROM HOUSTON
============================================================

Cities by distance (edges) from Houston:
  0 edge(s): Houston
  1 edge(s): Austin, Dallas, San Antonio
  2 edge(s): El Paso, Fort Worth, McKinney, Waco
  3 edge(s): Amarillo, Lubbock

============================================================
PART 4: BFS KEY CONCEPTS
============================================================

    Why BFS finds shortest path:
    1. Explores ALL nodes at distance 1 first
    2. Then ALL nodes at distance 2
    3. And so on...

    First time we reach destination = shortest path!

    BFS uses a QUEUE (FIFO):
    - First In, First Out
    - Process nodes in order they were discovered

    Time Complexity: O(V + E)
    - Visit each vertex once: O(V)
    - Check each edge once: O(E)

    Note: BFS finds shortest path by NUMBER OF EDGES.
    For weighted graphs (actual distances), use Dijkstra's (Lab 9)!
```

| Start   | Destination | Shortest Path                        | Edges |
|---------|-------------|--------------------------------------|-------|
| Houston | El Paso     | Houston → San Antonio → El Paso      | 2     |
| Houston | McKinney    | Houston → Dallas → McKinney          | 2     |
| Houston | Austin      | Houston → Austin                     | 1     |
| Houston | Amarillo    | Houston → Dallas → ... → Amarillo    | 3     |

## What I Learned

I learned that BFS is the gold standard for finding the shortest path in an unweighted graph. I also learned how to use `collections.deque` in Python to efficiently pop items from the front of a list, which is O(1) compared to O(n) for a standard list. A key implementation insight was storing a tuple `(current_city, path_to_here)` in the queue instead of just the city name — this way, when the destination is found, the full route is already recorded and ready to return without needing to reconstruct it afterward.

## Challenges

The biggest challenge was keeping track of the path itself, not just the nodes. Initially the queue only stored city names, which made it possible to detect when the destination was reached but impossible to know how we got there.

The fix was to store a tuple `(current_city, path_to_here)` in the queue. This way, every time a neighbor is added to the queue, the current path is extended and passed along with it. When the destination is found, the full route is already recorded and ready to return.

## Reflection Questions

### 1. Why does BFS use a queue instead of a stack?

A queue ensures we explore nodes in the order they were discovered, processing all neighbors at the current level before moving deeper — this is what guarantees the shortest path. A stack would produce Depth-First Search (DFS) instead, which goes as far down one branch as possible before backtracking. DFS can find a path, but it has no guarantee that the first path found is the shortest one.

### 2. What is the difference between BFS shortest path and actual shortest distance?

BFS finds the shortest path based on the number of edges (stops), treating every connection as equal. It does not account for the weight of those edges — for example, the actual mileage between Houston and Dallas vs. Houston and San Antonio. For real-world shortest distance problems where edges have different weights, Dijkstra's Algorithm (Lab 9) is the correct tool.

### 3. When would you use BFS vs DFS?

Use BFS when you need the shortest path or are searching for something close to the starting point, such as finding the nearest available node in a network. Use DFS when you need to visit every node in the graph (like solving a maze or detecting cycles), or when memory is a concern — DFS typically uses less space on deep, narrow graphs since it only keeps one active path in memory at a time rather than an entire frontier of nodes.
