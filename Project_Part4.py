class Node(object):
    def __init__(self, val, Left = None, Right = None):
        self.value = val
        self.left = Left
        self.right = Right


class binary_tree(object):
    def __init__(self,root):
        self.root = Node(root)

