from typing import Any, List, Tuple, Dict

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
    
    def __init__(self):
        self.vertices: Dict[int,List[int]]