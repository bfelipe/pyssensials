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
