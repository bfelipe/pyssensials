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
