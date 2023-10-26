import unittest

import tree


class BinaryTreeTestCase(unittest.TestCase):

    def test_binary_tree(self):
        t = tree.new_binary_tree(3)
        assert tree.get_root(t) == 3
        assert tree.get_left(t) == []
        assert tree.get_right(t) == []
        tree.insert_left(t, 4)
        tree.insert_left(t, 5)
        tree.insert_right(t, 6)
        tree.insert_right(t, 7)
        assert tree.get_left(t) == [5, [4, [], []], []]
        assert tree.get_right(t) == [7, [], [6, [], []]]
        left_child = tree.get_left(t)
        tree.set_root(left_child, 9)
        assert tree.get_left(t) == [9, [4, [], []], []]
        assert t == [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
