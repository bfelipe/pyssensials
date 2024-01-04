class Vertex:

    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        self.connections = 0

    def add_neighbor(self, vertex, weight=None):
        if vertex in self.neighbors:
            self.neighbors[vertex] = weight
        else:
            self.neighbors[vertex] = weight
            self.connections += 1

    def get_connections(self):
        return self.neighbors.keys(), self.connections

    def get_weight(self, vertex):
        return self.neighbors.get(vertex)

    def disconnect(self, vertex):
        if vertex in self.neighbors:
            del self.neighbors[vertex]
            self.connections -= 1

    def __repr__(self):
        return '<Vertex key: %s, neighbors: %s: connections: %s>' % (self.key,
                                                                     self.neighbors,
                                                                     self.connections)


class AdjacentListGraph:

    def __init__(self):
        self.vertices = {}
        self.current_size = 0

    def add_vertex(self, vertex: Vertex):
        self.vertices[vertex.key] = vertex
        self.current_size += 1

    def add_edge(self, from_vtx, to_vtx, weight=None):
        if from_vtx not in self.vertices:
            self.add_vertex(Vertex(from_vtx))
        if to_vtx not in self.vertices:
            self.add_vertex(Vertex(to_vtx))
        self.vertices[from_vtx].add_neighbor(to_vtx, weight)

    def get_vertex_by(self, key):
        return self.vertices.get(key)

    def get_vertices(self):
        return list(self.vertices.keys())

    def __contains__(self, k):
        return k in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

    def is_empty(self):
        return self.vertices == {}

    def size(self):
        return self.current_size

    def clear(self):
        self.vertices = {}
        self.current_size = 0

    def __repr__(self):
        return '<Graph vertices: %s>' % self.vertices