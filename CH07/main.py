from typing import List, Dict, Optional
from collections import deque
from graph import Graph

def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    """
    # 1. Check if start or end is not in graph
    if start not in graph.vertices or end not in graph.vertices:
        return None
    
    # 2. Initialize a queue with (current_vertex, path_taken_to_reach_it)
    queue = deque([(start, [start])])
    
    # 3. Initialize visited set
    visited = {start}
    
    # 4. While queue is not empty
    while queue:
        # 5. Pop the leftmost element (FIFO)
        current_vertex, path = queue.popleft()
        
        # 6. If current vertex is end, we found the shortest path!
        if current_vertex == end:
            return path
        
        # 7. Check neighbors
        for neighbor in graph.get_neighbors(current_vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                # Append neighbor to a new path list and add to queue
                queue.append((neighbor, path + [neighbor]))
                
    return None

def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    """
    Find all vertices reachable from start and their distances.
    """
    if start not in graph.vertices:
        return {}
        
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
    return distances

def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    path = bfs_find_path(graph, v1, v2)
    return path is not None