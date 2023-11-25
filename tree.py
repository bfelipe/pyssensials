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
        return None

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
        result = self.items.pop(1)
        self.items.insert(1, self.items.pop())
        self.current_size -= 1
        self._percolate_down_from(1)
        return result

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
