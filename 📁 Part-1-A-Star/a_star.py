import heapq
graph = {
    'S': {'A': 3, 'C': 2},
    'A': {'B': 4},
    'B': {'D': 5},
    'C': {'D': 2},
    'D': {}
} 
heuristic = {
    'S': 4,
    'A': 7,
    'B': 5,
    'C': 2,
    'D': 0
}
START = 'S'
GOAL = 'D'
 
 
def a_star_search(graph, heuristic, start, goal):
    """
    Runs A* search and returns (path, total_cost, explored_order).
    Also prints g(n), h(n), f(n) for every node as it is expanded.
    """
    # Priority queue holds tuples: (f, g, node, path_so_far)
    open_list = [(heuristic[start], 0, start, [start])]
    # Best known g(n) for each node, to avoid re-expanding worse paths
    best_g = {start: 0}
    explored_order = []
 
    print(f"{'Node':<6}{'g(n)':<8}{'h(n)':<8}{'f(n)':<8}")
    print("-" * 30)
 
    while open_list:
        f, g, node, path = heapq.heappop(open_list)
 
        # Skip stale entries (a better path to this node was already found)
        if g > best_g.get(node, float('inf')):
            continue
 
        explored_order.append(node)
        print(f"{node:<6}{g:<8}{heuristic[node]:<8}{f:<8}")
 
        if node == goal:
            return path, g, explored_order
 
        for neighbour, cost in graph[node].items():
            new_g = g + cost
            if new_g < best_g.get(neighbour, float('inf')):
                best_g[neighbour] = new_g
                new_f = new_g + heuristic[neighbour]
                new_path = path + [neighbour]
                heapq.heappush(open_list, (new_f, new_g, neighbour, new_path))
 
    return None, None, explored_order  # No path found
 
 
def main():
    print("A* Search Algorithm")
    print("=" * 30)
    print(f"Start node : {START}")
    print(f"Goal node  : {GOAL}\n")
 
    path, total_cost, explored = a_star_search(graph, heuristic, START, GOAL)
 
    print("\nNodes explored (in order):", " -> ".join(explored))
 
    if path:
        print("\nFinal Path :", " -> ".join(path))
        print("Total Cost :", total_cost)
    else:
        print(f"\nNo path found from {START} to {GOAL}.")
 
 
if __name__ == "__main__":
    main()
 
