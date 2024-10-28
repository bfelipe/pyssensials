from typing import Any, List, Tuple
from collections import defaultdict

class Matrix:
    
    def __init__(self, dimension:Tuple[int,int], fill:Any=0):
        self.rows = dimension[0]
        self.cols = dimension[1]
        self.fill = fill
        self.grid = [[self.fill] * self.cols for _ in range(self.rows)]

    def add_vertexes(self, value:Any, coordinates:List[Tuple[int, int]]) -> None:
        for coord in coordinates:
            r,c = coord
            self.grid[r][c] = value

    def dimension(self) -> Tuple[int,int]:
        return (self.rows, self.cols)
    
    def vertex(self, coordinate:Tuple[int,int]) -> Any:
        r, c = coordinate
        return self.grid[r][c]
    
    def num_paths(self, start:Tuple[int,int], end:Tuple[int,int], blocked:List[Any]) -> int:
        if (min(start) < 0 or max(start) >= max(self.dimension()) or 
        min(end) < 0 or max(end) >= max(self.dimension())):
            return -1
        
        paths = 0
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(coordinate:Tuple[int, int]):
            out = 0
            r, c = coordinate
            if (r not in range(self.rows) or c not in range(self.cols) or
                coordinate in visited or self.vertex(coordinate) in blocked):
                return out
            
            if (r, c) == end:
                return 1

            visited.add(coordinate)    
            for dr, dc in directions:
                out += dfs((r + dr, c + dc))
            visited.remove(coordinate)
            return out
        
        paths += dfs(start)
        return paths
    
    def groups(self, target:Any) -> int:
        count = 0
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(coordinate:Tuple[int, int]):
            r, c = coordinate
            if (min(coordinate) < 0 or max(coordinate) >= max(self.dimension()) or
                coordinate in visited or self.vertex(coordinate) != target):
                return

            visited.add(coordinate)
            for dr, dc in directions:
                dfs((r + dr, c + dc))

        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in visited and self.vertex((row, col)) == target:
                    count += 1
                    dfs((row, col))
        return count
    
    def short_distance(self, start:Tuple[int, int], end:Tuple[int,int], blocked:List[Any]) -> int:
        if (min(start) < 0 or max(start) >= max(self.dimension()) or 
        min(end) < 0 or max(end) >= max(self.dimension())):
            return -1

        distance = 0
        queue = []
        visited = set()
        queue.append(start)
        visited.add(start)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(coordinate:Tuple[int, int]):
            if (min(coordinate) < 0 or max(coordinate) >= max(self.dimension()) or
            coordinate in visited or self.vertex(coordinate) in blocked):
                return
            queue.append(coordinate)
            visited.add(coordinate)


        while queue:
            for _ in range(len(queue)):
                row, col = queue.pop(0)
                if (row, col) == end:
                    return distance
                
                for dr, dc in directions:
                    bfs((row + dr, col + dc))
            distance += 1
        return -1

    def describe(self) -> None:
        for r in self.grid:
            print(r)

    def __repr__(self) -> str:
        return '<Matrix dimmension: %s, grid: %s>' % (self.dimension(), self.grid)
    

class AdjacentList:
    
    def __init__(self, edges:List[Tuple[Any, Any]]=None):
        self.vertexes = defaultdict(list)
        if edges:
            self.add_vertexes(edges)

    def add_vertexes(self, vertexes:List[Tuple[Any, Any]]):
        # Vertex: Origin, Destination
        for origin, destination in vertexes:
            if origin not in self.vertexes:
                self.vertexes[origin] = []
            if destination not in vertexes:
                self.vertexes[destination] = []
            self.vertexes[origin].append(destination)
    
    def vertex(self, key:Any) -> Tuple[Any, List]:
        return key, self.vertexes.get(key)
    
    def num_paths(self, origin:Any, destination:Any) -> int:
        if origin not in self.vertexes or destination not in self.vertexes:
            return -1
        
        visited = set()
        
        def dfs(vertex:Any) -> int:
            if vertex in visited:
                return 0
            if vertex == destination:
                return 1
            
            out = 0
            visited.add(vertex)
            for neighbor in self.vertexes.get(vertex):
                out += dfs(neighbor)
            visited.remove(vertex)
            return out
        
        return dfs(origin)


    def short_distance(self, origin:Any, destination:Any) -> int:
        if origin not in self.vertexes or destination not in self.vertexes:
            return -1
        
        queue = []
        visited = set()
        queue.append(origin)
        visited.add(origin)

        distance = 0

        def bfs(vertex:Any):
            if vertex in visited:
                return
            queue.append(vertex)
            visited.add(vertex)

        while queue:
            for _ in range(len(queue)):
                vertex = queue.pop(0)
                if vertex == destination:
                    return distance
            
                for neighbor in self.vertexes.get(vertex):
                    bfs(neighbor)
            distance += 1
        return -1

    def describe(self) -> None:
        for k, v in self.vertexes.items():
            print(f'vertex: %s, neighbors: %s' % (k, v))

    def is_empty(self):
        return self.vertexes == {}

    def __repr__(self) -> str:
        return '<AdjacentList vertexes: %s>' % (list(self.vertexes.keys()))
