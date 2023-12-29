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

    def test_MinHeap(self):
        min_heap = tree.MinHeap()
        assert type(min_heap) is tree.MinHeap
        assert min_heap.is_empty() is True
        assert min_heap.size() == 0
        assert min_heap.remove_min() == -1
        assert min_heap.find_min() == -1

        data = [9, 6, 5, 3, 2]

        min_heap.build(data)
        assert min_heap.is_empty() is False
        assert min_heap.size() == 5
        assert min_heap.find_min() == 2
        min_heap.clear()
        assert min_heap.remove_min() == -1
        assert min_heap.find_min() == -1
        assert min_heap.is_empty() is True
        assert min_heap.size() == 0
        position = 0
        for item in data:
            min_heap.insert(item)
            assert min_heap.find_min() == data[position]
            position += 1
        assert min_heap.is_empty() is False
        assert min_heap.size() == 5
        for _ in data:
            min_val = min_heap.find_min()
            assert min_heap.remove_min() == min_val
        assert min_heap.is_empty() is True
        assert min_heap.size() == 0

    def test_MaxHeap(self):
        max_heap = tree.MaxHeap()
        assert type(max_heap) is tree.MaxHeap
        assert max_heap.is_empty() is True
        assert max_heap.size() == 0
        assert max_heap.remove_max() == -1
        assert max_heap.find_max() == -1

        data = [2, 3, 5, 6, 9]

        max_heap.build(data)
        assert max_heap.is_empty() is False
        assert max_heap.size() == 5
        assert max_heap.find_max() == 9
        max_heap.clear()
        assert max_heap.remove_max() == -1
        assert max_heap.find_max() == -1
        assert max_heap.is_empty() is True
        assert max_heap.size() == 0
        position = 0
        for item in data:
            max_heap.insert(item)
            assert max_heap.find_max() == data[position]
            position += 1
        assert max_heap.is_empty() is False
        assert max_heap.size() == 5
        for _ in data:
            max_val = max_heap.find_max()
            assert max_heap.remove_max() == max_val
        assert max_heap.is_empty() is True
        assert max_heap.size() == 0

    def test_TreeNode(self):
        parent = tree.TreeNode(3, 'red')
        right = tree.TreeNode(5, 'blue', parent=parent)
        left = tree.TreeNode(1, 'green', parent=parent)
        parent.right_child = right
        parent.left_child = left
    
        assert type(parent) is tree.TreeNode
        assert parent.parent is None
        assert parent.left_child == left
        assert parent.right_child == right
        assert parent.key == 3
        assert parent.val == 'red'
        assert parent.has_left_child() == left
        assert parent.has_right_child() == right
    
        left_child = parent.left_child
        right_child = parent.right_child
    
        assert left_child.is_left_child() is True
        assert right_child.is_right_child() is True
        assert parent.is_root() is True
        assert parent.left_child.is_leaf() is True
        assert parent.right_child.is_leaf() is True
        assert bool(parent.has_any_child()) is True
        assert bool(parent.has_both_children()) is True
    
        assert parent.find_successor().key == 5
    
        parent.left_child.right_child = tree.TreeNode(2, 'purple', parent=parent.left_child)
        parent.right_child.left_child = tree.TreeNode(4, 'yellow', parent=parent.right_child)
    
        assert parent.find_successor().key == 4

    def test_BinarySearchTree(self):
        bst = tree.BinarySearchTree()
        assert type(bst) is tree.BinarySearchTree

        assert bst.root is None
        assert len(bst) == 0

        bst.put(3, 'blue')
        assert len(bst) == 1
        assert bst.get(3) == 'blue'

        bst.put(3, 'red')
        assert len(bst) == 1
        assert bst.get(3) == 'red'

        bst[5] = 'blue'
        bst[1] = 'green'

        assert len(bst) == 3
        assert bst[5] == 'blue'
        assert bst[1] == 'green'

        contains_key_6 = False
        if 6 in bst:
            contains_key_6 = True
        assert contains_key_6 is False

        contains_key_1 = False
        if 1 in bst:
            contains_key_1 = True
        assert contains_key_1 is True

        bst.put(2, 'purple')
        bst.put(4, 'yellow')

        assert bst.get(2) == 'purple'
        assert bst[4] == 'yellow'

        assert len(bst) == 5

        empty_bst = tree.BinarySearchTree()

        with self.assertRaises(KeyError) as e:
            empty_bst.delete(1)
        self.assertEqual(str(e.exception), "'Key not found'")

        with self.assertRaises(KeyError) as e:
            del empty_bst[1]
        self.assertEqual(str(e.exception), "'Key not found'")

        assert empty_bst.get(1) is None
        assert empty_bst[1] is None

        bst.delete(3)
        assert len(bst) == 4
        assert bst[3] is None
        assert bst[5] == 'blue'
        assert bst[1] == 'green'
        assert bst[2] == 'purple'
        assert bst[4] == 'yellow'

        del bst[2]
        assert bst.get(2) is None
        assert len(bst) == 3
        assert bst[5] == 'blue'
        assert bst[1] == 'green'
        assert bst[4] == 'yellow'

        del bst[1]
        assert bst[1] is None
        assert len(bst) == 2
        assert bst[5] == 'blue'
        assert bst[4] == 'yellow'

        bst.delete(5)
        assert bst.get(5) is None
        assert len(bst) == 1
        assert bst[4] == 'yellow'

        bst.delete(4)
        assert bst.get(4) is None
        assert len(bst) == 0

        assert bst.root is None
        assert bst.size == 0

        bst.put(3, 'red')
        bst[5] = 'blue'
        bst[1] = 'green'
        bst.put(2, 'purple')
        bst.put(4, 'yellow')

        assert len(bst) == 5
        assert bst[3] == 'red'
        assert bst[5] == 'blue'
        assert bst[1] == 'green'
        assert bst[2] == 'purple'
        assert bst[4] == 'yellow'

        bst.clean()
        assert len(bst) == 0
        assert bst.root is None
        assert bst[3] is None
        assert bst[5] is None
        assert bst[1] is None
        assert bst[2] is None
        assert bst[4] is None