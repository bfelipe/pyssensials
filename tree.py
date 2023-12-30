def new_binary_tree(branch):
    return [branch, [], []]


def insert_left(root, branch):
    left_child = root.pop(1)
    if len(left_child) > 1:
        root.insert(1, [branch, left_child, []])
    else:
        root.insert(1, [branch, [], []])
    return root


def insert_right(root, branch):
    right_child = root.pop(2)
    if len(right_child) > 1:
        root.insert(2, [branch, [], right_child])
    else:
        root.insert(2, [branch, [], []])
    return root


def set_root(root, data):
    root[0] = data


def get_root(root):
    return root[0]


def get_left(root):
    return root[1]


def get_right(root):
    return root[2]


class BinaryTree:

    def __init__(self, data=None):
        self.key = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, data):
        node = BinaryTree(data)
        if self.left_child is None:
            self.left_child = node
        else:
            node.left_child = self.left_child
            self.left_child = node

    def insert_right(self, data):
        node = BinaryTree(data)
        if self.right_child is None:
            self.right_child = node
        else:
            node.right_child = self.right_child
            self.right_child = node

    def set_root(self, data):
        self.key = data

    def get_root(self):
        return self.key

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def __repr__(self):
        return '<Node key: %s, l: %s, r: %s>' % (self.key,
                                                 self.left_child,
                                                 self.right_child)


def pre_order(t: BinaryTree):
    if t:
        print(t.get_root())
        pre_order(t.get_left())
        pre_order(t.get_right())


def in_order(t: BinaryTree):
    if t:
        in_order(t.get_left())
        print(t.get_root())
        in_order(t.get_right())


def post_order(t):
    if t:
        post_order(t.get_left())
        post_order(t.get_right())
        print(t.get_root())


class Heap:

    def _percolate_up_from(self, index):
        pass

    def insert(self, data):
        pass

    def _percolate_down_from(self, index):
        pass

    def is_empty(self):
        pass

    def size(self):
        pass

    def clear(self):
        pass

    def build(self, items):
        pass


class MinHeap(Heap):

    def __init__(self, items: list = None):
        self.items = [0]
        self.current_size = 0
        if items:
            self.build(items)

    def _percolate_up_from(self, index):
        while index // 2 > 0:
            if self.items[index] < self.items[index // 2]:
                tmp = self.items[index // 2]
                self.items[index // 2] = self.items[index]
                self.items[index] = tmp
            index //= 2

    def insert(self, data):
        self.items.append(data)
        self.current_size += 1
        self._percolate_up_from(self.current_size)

    def find_min(self):
        if not self.is_empty():
            return self.items[1]
        return -1

    def _get_min_child_index(self, index):
        if (index * 2 + 1) > self.current_size:
            return index * 2
        else:
            if self.items[index * 2] < self.items[index * 2 + 1]:
                return index * 2
            return index * 2 + 1

    def _percolate_down_from(self, index):
        while (index * 2) <= self.current_size:
            min_child_index = self._get_min_child_index(index)
            if self.items[index] > self.items[min_child_index]:
                tmp = self.items[min_child_index]
                self.items[min_child_index] = self.items[index]
                self.items[index] = tmp
            index = min_child_index

    def remove_min(self):
        if not self.is_empty():
            result = self.items.pop(1)
            self.items.insert(1, self.items.pop())
            self.current_size -= 1
            self._percolate_down_from(1)
            return result
        return -1

    def is_empty(self):
        return self.items == [0]

    def size(self):
        return self.current_size

    def clear(self):
        self.items = [0]
        self.current_size = 0

    def build(self, items):
        index = len(items) // 2
        self.current_size = len(items)
        self.items += items
        while index > 0:
            self._percolate_down_from(index)
            index -= 1

    def __repr__(self):
        return str(self.items)


class MaxHeap(Heap):

    def __init__(self, items: list = None):
        self.items = [0]
        self.current_size = 0
        if items:
            self.build(items)

    def _percolate_up_from(self, index):
        while index // 2 > 0:
            if self.items[index] > self.items[index // 2]:
                tmp = self.items[index // 2]
                self.items[index // 2] = self.items[index]
                self.items[index] = tmp
            index //= 2

    def insert(self, data):
        self.items.append(data)
        self.current_size += 1
        self._percolate_up_from(self.current_size)

    def find_max(self):
        if not self.is_empty():
            return self.items[1]
        return -1

    def _get_max_child_index(self, index):
        if (index * 2 + 1) > self.current_size:
            return index * 2
        else:
            if self.items[index * 2] > self.items[index * 2 + 1]:
                return index * 2
            return index * 2 + 1

    def _percolate_down_from(self, index):
        while (index * 2) <= self.current_size:
            max_child_index = self._get_max_child_index(index)
            if self.items[index] < self.items[max_child_index]:
                tmp = self.items[max_child_index]
                self.items[max_child_index] = self.items[index]
                self.items[index] = tmp
            index = max_child_index

    def remove_max(self):
        if not self.is_empty():
            result = self.items.pop(1)
            self.items.insert(1, self.items.pop())
            self.current_size -= 1
            self._percolate_down_from(1)
            return result
        return -1

    def is_empty(self):
        return self.items == [0]

    def size(self):
        return self.current_size

    def clear(self):
        self.items = [0]
        self.current_size = 0

    def build(self, items):
        index = len(items) // 2
        self.current_size = len(items)
        self.items += items
        while index > 0:
            self._percolate_down_from(index)
            index -= 1

    def __repr__(self):
        return str(self.items)


class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.balance_factor = 0

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not self.left_child or self.right_child

    def has_any_child(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def _find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right_child._find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent._find_successor()
                    self.parent.right_child = self
        return successor

    def replace(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __repr__(self):
        return '<Node key: %s, val: %s, l: %s, r: %s>' % (self.key,
                                                          self.val,
                                                          self.left_child,
                                                          self.right_child)


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def _put(self, key, val, current):
        update_key = False
        if key == current.key:
            current.val = val
            update_key = True
        elif key < current.key:
            if current.has_left_child():
                self._put(key, val, current.left_child)
            else:
                current.left_child = TreeNode(key, val, parent=current)
        else:
            if current.has_right_child():
                self._put(key, val, current.right_child)
            else:
                current.right_child = TreeNode(key, val, parent=current)
        return update_key

    def put(self, key, val):
        updated_key = False
        if self.root:
            updated_key = self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        if not updated_key:
            self.size += 1

    def __setitem__(self, k, v):
        self.put(k, v)

    def _get(self, key, current):
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left_child)
        else:
            return self._get(key, current.right_child)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            return result.val if result else None
        return None

    def __getitem__(self, k):
        return self.get(k)

    def __contains__(self, k):
        return bool(self._get(k, self.root))

    def _remove_node_with_no_children(self, node: TreeNode):
        if node.is_root():
            self.root = None
        elif node.is_left_child():
            node.parent.left_child = None
        else:
            node.parent.right_child = None

    def _remove_node_with_single_child(self, node: TreeNode):
        if node.has_left_child():
            if node.is_left_child():
                node.left_child.parent = node.parent
                node.parent.left_child = node.left_child
            elif node.is_right_child():
                node.left_child.parent = node.parent
                node.parent.right_child = node.left_child
            else:
                node.replace(node.left_child.key,
                             node.left_child.val,
                             node.left_child.left_child,
                             node.left_child.right_child)
        else:
            if node.is_left_child():
                node.right_child.parent = node.parent
                node.parent.left_child = node.left_child
            elif node.is_right_child():
                node.right_child.parent = node.parent
                node.parent.right_child = node.right_child
            else:
                node.replace(node.right_child.key,
                             node.right_child.val,
                             node.right_child.left_child,
                             node.right_child.right_child)

    def _remove_node_with_both_children(self, node: TreeNode):
        successor = node.find_successor()
        successor.splice_out()
        node.key = successor.key
        node.val = successor.val

    def _remove(self, node: TreeNode):
        if not node.has_both_children():
            self._remove_node_with_no_children(node)
        elif node.has_both_children():
            self._remove_node_with_both_children(node)
        else:
            self._remove_node_with_single_child(node)

    def delete(self, key):
        if self.size > 1:
            node = self._get(key, self.root)
            if node:
                self._remove(node)
                self.size -= 1
            else:
                raise KeyError('Key not found')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Key not found')

    def __delitem__(self, k):
        self.delete(k)

    def clean(self):
        self.root = None
        self.size = 0

    def __repr__(self):
        return str(self.root)


class AVLTree(BinarySearchTree):

    def _rotate_right(self, node: TreeNode):
        new_root = node.left_child
        node.left_child = new_root.right_child

        if new_root.right_child is not None:
            new_root.right_child.parent = node
        
        new_root.parent = node.parent

        if node.is_root():
            self.root = new_root
        else:
            if node.is_right_child():
                node.parent.right_child = new_root
        new_root.right_child = node
        node.balance_factor = node.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(node.balance_factor, 0)

    def _rotate_left(self, node: TreeNode):
        new_root = node.right_child
        node.right_child = new_root.left_child

        if new_root.left_child is not None:
            new_root.left_child.parent = node
        
        new_root.parent = node.parent

        if node.is_root():
            self.root = new_root
        else:
            if node.is_left_child():
                node.parent.left_child = new_root
            else:
                node.parent.right_child = new_root
        new_root.left_child = node
        node.parent = new_root
        node.balance_factor = node.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(node.balance_factor, 0)
            

    def _rebalance(self, node: TreeNode):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self._rotate_right(node.right_child)
                self._rotate_left(node)
            else:
                self._rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self._rotate_left(node.left_child)
                self._rotate_right(node)
            else:
                self._rotate_right(node)

    def _update_balance(self, node: TreeNode):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self._rebalance(node)
            return
        if node.parent != None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
        
            if node.parent.balance_factor != 0:
                self._update_balance(node.parent)


    def _put(self, key, val, current):
        if key < current.key:
            if current.has_left_child():
                self._put(key, val, current.left_child)
            else:
                self._put(key, val, current.right_child)
                self._update_balance(current.left_child)
        else:
            if current.has_right_child():
                self._put(key, val, current.right_child)
            else:
                current.right_child = TreeNode(key, val, parent=current)
                self._update_balance(current.right_child)