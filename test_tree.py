import unittest
import operator

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

    def test_BinaryTree(self):
        bt = tree.BinaryTree()
        assert type(bt) is tree.BinaryTree
        assert bt.get_root() is None
        bt.set_root('a')
        assert bt.get_root() == 'a'
        assert bt.get_left() is None
        assert bt.get_right() is None
        bt.insert_left('b')
        assert bt.get_left().get_root() == 'b'
        bt.insert_right('c')
        assert bt.get_right().get_root() == 'c'


    def test_parse_BinaryTree(self):
        tokens = '( ( 10 + 5 ) * 3 )'.split()
        root = tree.BinaryTree()
        token_stack = [root]
        current_node = root

        for i in tokens:
            if i == '(':
                current_node.insert_left('')
                token_stack.append(current_node)
                current_node = current_node.get_left()
            elif i in ['+', '-', '*', '/']:
                current_node.set_root(i)
                current_node.insert_right('')
                token_stack.append(current_node)
                current_node = current_node.get_right()
            elif i == ')':
                current_node = token_stack.pop()
            else:
                current_node.set_root(int(i))
                parent = token_stack.pop()
                current_node = parent

        assert root.get_root() == '*'
        assert root.get_left().get_root() == '+'
        assert root.get_left().get_left().get_root() == 10
        assert root.get_left().get_right().get_root() == 5
        assert root.get_right().get_root() == 3

        def evaluate(root):
            opers = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv
            }

            left_child = root.get_left()
            right_child = root.get_right()
            if left_child and right_child:
                operation = opers[root.get_root()]
                return operation(evaluate(left_child), evaluate(right_child))
            else:
                return root.get_root()

        assert evaluate(root) == 45
