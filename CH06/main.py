"""
Lab 6: Main Program
Demonstrates BFS on Texas road network.
"""
from graph import Graph, create_texas_road_network
from bfs import bfs_find_path, bfs_all_reachable


def main():
    # =========================================
    # PART 1: Create Road Network
    # =========================================
    print("=" * 60)
    print("PART 1: TEXAS ROAD NETWORK GRAPH")
    print("=" * 60)
    
    roads = create_texas_road_network()
    print(f"\nCreated graph with {len(roads)} cities")
    roads.display()
    
    # =========================================
    # PART 2: Find Shortest Paths
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: SHORTEST PATH (BFS)")
    print("=" * 60)
    
    # Houston to El Paso
    path = bfs_find_path(roads, "Houston", "El Paso")
    if path:
        print(f"\nRoute: {' → '.join(path)}")
    
    # Houston to McKinney
    print("\n" + "-" * 40)
    path = bfs_find_path(roads, "Houston", "McKinney")
    if path:
        print(f"\nRoute: {' → '.join(path)}")
    
    # =========================================
    # PART 3: Reachability
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: DISTANCES FROM HOUSTON")
    print("=" * 60)
    
    distances = bfs_all_reachable(roads, "Houston")
    
    print("\nCities by distance (edges) from Houston:")
    for dist in range(max(distances.values()) + 1):
        cities_at_dist = [c for c, d in distances.items() if d == dist]
        if cities_at_dist:
            print(f"  {dist} edge(s): {', '.join(sorted(cities_at_dist))}")
    
    # =========================================
    # PART 4: Key Concepts
    # =========================================
    print("\n" + "=" * 60)
    print("PART 4: BFS KEY CONCEPTS")
    print("=" * 60)
    print("""
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
    """)


if __name__ == "__main__":
    main()
