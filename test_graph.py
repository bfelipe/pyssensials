import unittest

import graph


class GraphTestCase(unittest.TestCase):

    def test_Vertex(self):
        vtx = graph.Vertex('a')
        assert type(vtx) is graph.Vertex
        assert vtx.key == 'a'
        assert vtx.neighbors == {}
        assert vtx.connections == 0

        vtx.add_neighbor('b')
        vtx.add_neighbor('c', 2)

        assert vtx.connections == 2
        n, c = vtx.get_connections()
        for key in n:
            assert key in ['b', 'c']
        assert c == 2

        assert vtx.get_weight('b') is None
        assert vtx.get_weight('c') == 2
        assert vtx.get_weight('d') is None

        vtx.disconnect('d')
        assert vtx.connections == 2
        vtx.disconnect('b')
        assert vtx.connections == 1
        n, c = vtx.get_connections()
        assert 'b' not in n

        vtx.add_neighbor('c', 3)
        assert vtx.connections == 1
        assert vtx.get_weight('c') == 3

    def test_AdjacentListGraph(self):
        alg = graph.AdjacentListGraph()
        assert type(alg) is graph.AdjacentListGraph
        assert alg.is_empty() is True
        assert alg.size() == 0
        assert alg.get_vertices() == []

        for i in range(6):
            alg.add_vertex(graph.Vertex(i))

        alg.add_edge(0, 1, 5)
        alg.add_edge(0, 5, 2)
        alg.add_edge(1, 2, 4)
        alg.add_edge(2, 3, 9)
        alg.add_edge(3, 4, 7)
        alg.add_edge(3, 5, 3)
        alg.add_edge(4, 0, 1)
        alg.add_edge(5, 4, 8)
        alg.add_edge(5, 2, 1)

        assert alg.is_empty() is False
        assert alg.size() == 6

        assert alg.get_vertex_by(6) is None
        v = alg.get_vertex_by(0)
        assert v.key == 0
        assert v.neighbors == {1: 5, 5: 2}
        assert v.connections == 2

        v = alg.get_vertex_by(1)
        assert v.key == 1
        assert v.neighbors == {2: 4}
        assert v.connections == 1

        v = alg.get_vertex_by(2)
        assert v.key == 2
        assert v.neighbors == {3: 9}
        assert v.connections == 1

        v = alg.get_vertex_by(3)
        assert v.key == 3
        assert v.neighbors == {4: 7, 5: 3}
        assert v.connections == 2

        v = alg.get_vertex_by(4)
        assert v.key == 4
        assert v.neighbors == {0: 1}
        assert v.connections == 1

        v = alg.get_vertex_by(5)
        assert v.key == 5
        assert v.neighbors == {4: 8, 2: 1}
        assert v.connections == 2

        assert alg.get_vertices() == [k for k in range(6)]

        alg.clear()
        assert alg.is_empty() is True
        assert alg.size() == 0
        assert alg.get_vertices() == []

    def test_BFS(self):
        word_table = {}
        alg = graph.AdjacentListGraph()

        with open('words.txt', 'r') as file:

            for line in file:
                word = line[:-1]
                for idx in range(len(word)):
                    bucket = f'{word[:idx]}_{word[idx + 1:]}'
                    if bucket in word_table:
                        word_table[bucket].append(word)
                    else:
                        word_table[bucket] = [word]

            for bucket in word_table.keys():
                for w1 in word_table[bucket]:
                    for w2 in word_table[bucket]:
                        if w1 != w2:
                            alg.add_edge(w1, w2)

        word_table.clear()