class GraphColoring:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)
        self.colors = [0] * self.num_vertices
        self.num_colors = 0

    def is_safe(self, v, c):
        for i in range(self.num_vertices):
            if self.graph[v][i] == 1 and self.colors[i] == c:
                return False
        return True

    def solve_backtracking(self, v):
        if v == self.num_vertices:
            self.num_colors = max(self.colors) + 1
            return True

        for c in range(1, self.num_vertices + 1):
            if self.is_safe(v, c):
                self.colors[v] = c
                if self.solve_backtracking(v + 1):
                    return True
                self.colors[v] = 0

        return False

    def solve_branch_and_bound(self, v):
        if v == self.num_vertices:
            self.num_colors = max(self.colors) + 1
            return True

        for c in range(1, self.num_vertices + 1):
            if self.is_safe(v, c):
                self.colors[v] = c
                if self.solve_branch_and_bound(v + 1):
                    return True
                self.colors[v] = 0

        return False

    def solve(self, algorithm):
        if algorithm == 'backtracking':
            if not self.solve_backtracking(0):
                print("No solution exists.")
                return None
        elif algorithm == 'branch_and_bound':
            if not self.solve_branch_and_bound(0):
                print("No solution exists.")
                return None
        else:
            print("Invalid algorithm choice")
            return None
        
        return self.colors, self.num_colors

def print_solution(colors):
    print("Vertex - Color")
    for v, c in enumerate(colors):
        print(f"{v + 1} - {c}")

if __name__ == "__main__":
    # Define the adjacency matrix of the graph (0-based index)
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    graph_coloring = GraphColoring(graph)
    
    print("Solving using Backtracking:")
    colors, num_colors = graph_coloring.solve('backtracking')
    if colors is not None:
        print(f"Number of colors needed: {num_colors}")
        print_solution(colors)
    
    print("\nSolving using Branch and Bound:")
    colors, num_colors = graph_coloring.solve('branch_and_bound')
    if colors is not None:
        print(f"Number of colors needed: {num_colors}")
        print_solution(colors)
