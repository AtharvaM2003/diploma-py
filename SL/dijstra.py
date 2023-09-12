import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        # Initialize distances and visited vertices
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        visited = set()

        # Create a priority queue (min heap) to store vertices and their distances
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Skip if already visited
            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            # Update distances to neighboring vertices
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example usage:
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'E', 3)
g.add_edge('E', 'A', 2)
start_vertex = 'A'
shortest_distances = g.dijkstra(start_vertex)

for vertex, distance in shortest_distances.items():
    print(f"Shortest distance from {start_vertex} to {vertex} is {distance}")
