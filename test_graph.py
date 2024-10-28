import unittest

import graph

class GraphTestCase(unittest.TestCase):

    def test_Matrix(self):
        m = graph.Matrix(dimension=(4, 4))
        assert type(m) is graph.Matrix
        assert m.dimension() == (4, 4)
        for row in m.grid:
            for col in row:
                assert col == 0
        assert m.fill == 0

        coordinates = [(1, 0), (1, 1), (2, 3), (3, 1)]
        m.add_vertexes(value=1, coordinates=coordinates)
        for c in coordinates:
            assert m.vertex(c) == 1
        assert m.grid == [
            [0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]
        
        assert m.num_paths(start=(0,0), end=(3,3), blocked=[1]) == 2
        assert m.num_paths(start=(0,0), end=(4,3), blocked=[1]) == -1
        assert m.num_paths(start=(1,2), end=(2,2), blocked=[1]) == 1
        assert m.groups(1) == 3
        assert m.groups(0) == 1
        assert m.short_distance(start=(0,0), end=(3,3), blocked=[1]) == 6
        assert m.short_distance(start=(0,0), end=(4,3), blocked=[1]) == -1
