def prim_mst_tree(graph):
    # Initialize data structures
    vertices = set(graph.keys())
    start_vertex = list(vertices)[0]  # Choose any starting vertex

    visited = set()
    mst = []
    min_cost = 0

    # Use a priority queue to keep track of edges with their weights
    priority_queue = [(0, start_vertex)]  # (weight, vertex)

    while priority_queue:
        weight, vertex = min(priority_queue)
        priority_queue.remove((weight, vertex))

        if vertex not in visited:
            visited.add(vertex)
            min_cost += weight

            if vertex != start_vertex:
                mst.append((vertex, weight))

            for neighbor, edge_weight in graph[vertex]:
                if neighbor not in visited:
                    priority_queue.append((edge_weight, neighbor))

    return mst, min_cost

# Example graph represented as an adjacency list
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (3, 4)],
    2: [(0, 3), (4, 5)],
    3: [(1, 4)],
    4: [(2, 5)],
}

mst, min_cost = prim_mst_tree(graph)

print("Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} -- {edge[1]}")

print(f"Minimum Cost: {min_cost}")
