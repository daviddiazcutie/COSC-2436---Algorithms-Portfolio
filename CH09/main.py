# =============================================================================
# Dijkstra's Shortest Path — Interactive CLI
# =============================================================================

def get_nodes():
    print("=== Dijkstra's Shortest Path ===\n")
    print("Enter node names one per line.")
    print("Type 'done' when finished.\n")

    nodes = []

    while True:
        line = input("Node: ").strip()

        if line.lower() == "done":
            break

        if not line:
            continue

        if line in nodes:
            print(f"  '{line}' already added.")
            continue

        nodes.append(line)
        print(f"  Added: {line}")

    return nodes


def get_edges(nodes):
    print("\nFor each pair of nodes, enter the edge weight if connected, or press Enter to skip.\n")

    graph = {n: {} for n in nodes}

    for i, frm in enumerate(nodes):
        for to in nodes[i + 1:]:
            raw = input(f"  {frm} <--> {to}  (weight or Enter to skip): ").strip()

            if raw == "":
                continue

            try:
                weight = float(raw)

                # Prevent negative weights (Dijkstra requirement)
                if weight < 0:
                    print("    Skipped (negative weights not allowed).")
                    continue

                graph[frm][to] = weight
                graph[to][frm] = weight

                print(f"    Added: {frm} <--{raw}--> {to}")
            except ValueError:
                print("    Skipped (not a number).")

    return graph


def draw_ascii_graph(graph, nodes, path_edges=None, path=None):
    if path_edges is None:
        path_edges = set()

    col_w = 12

    def node_label(n):
        return f"[{n}]" if path and n in path else f"({n})"

    print("\n" + "─" * 52)
    print("  GRAPH")
    print("─" * 52)

    seen = set()
    any_edges = False

    for frm in nodes:
        for to, weight in graph.get(frm, {}).items():
            pair = tuple(sorted([frm, to]))
            if pair in seen:
                continue
            seen.add(pair)

            any_edges = True

            on_path = (frm, to) in path_edges or (to, frm) in path_edges
            arrow = "<=>" if on_path else "<->"
            w_str = int(weight) if weight == int(weight) else weight

            line = f"  {node_label(frm):>{col_w}}  {arrow}  {w_str:<6}  {node_label(to)}"

            if on_path:
                line = f"\033[92m{line}\033[0m"

            print(line)

    if not any_edges:
        print("  (no edges)")

    print("─" * 52)

    if path:
        print("  [node] = on shortest path    <=> = path edge")

    print()


# =========================
# DIJKSTRA ALGORITHM
# =========================
def dijkstra(graph, nodes, start, end):
    infinity = float("inf")

    costs = {n: infinity for n in nodes}
    costs[start] = 0

    parents = {n: None for n in nodes}
    processed = []

    def find_lowest_cost_node():
        lowest = infinity
        result = None
        for n in costs:
            if costs[n] < lowest and n not in processed:
                lowest = costs[n]
                result = n
        return result

    node = find_lowest_cost_node()

    while node is not None:
        cost = costs[node]

        for neighbor, weight in graph.get(node, {}).items():
            new_cost = cost + weight

            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node

        processed.append(node)
        node = find_lowest_cost_node()

    if costs[end] == infinity:
        return None, None

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()

    return path, costs[end]


def main():
    nodes = get_nodes()
    if len(nodes) < 2:
        print("Need at least 2 nodes. Exiting.")
        return

    graph = get_edges(nodes)

    draw_ascii_graph(graph, nodes)

    print(f"Nodes: {', '.join(nodes)}")

    start = input("From: ").strip()
    while start not in nodes:
        start = input("Invalid node. From: ").strip()

    end = input("To:   ").strip()
    while end not in nodes:
        end = input("Invalid node. To: ").strip()

    if start == end:
        print(f"\nShortest path: {start}")
        print("Total cost: 0\n")
        return

    path, total_cost = dijkstra(graph, nodes, start, end)

    if path is None:
        print(f"\nNo path found from '{start}' to '{end}'.")
        return

    path_edges = {(path[i], path[i + 1]) for i in range(len(path) - 1)}

    draw_ascii_graph(graph, nodes, path_edges=path_edges, path=path)

    print(f"  Shortest path: {' -> '.join(path)}")
    cost_str = int(total_cost) if total_cost == int(total_cost) else total_cost
    print(f"  Total cost:    {cost_str}\n")


if __name__ == "__main__":
    main()