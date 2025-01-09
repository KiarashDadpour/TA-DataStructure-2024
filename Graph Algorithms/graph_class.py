class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            del self.graph[vertex]

    def bfs(self, start_vertex):
        visited = set()  
        queue = [start_vertex] 
        result = []  

        while queue:
            current = queue.pop(0)  
            if current not in visited:
                visited.add(current)  
                result.append(current)  
                queue.extend([neighbor for neighbor in self.graph[current] if neighbor not in visited])

    def dfs(self, vertex, visited=None, result=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []

        visited.add(vertex)
        result.append(vertex)
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, result)
        return result

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
