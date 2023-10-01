import random

class TreeNode:
    def __init__(self, value=random.randint(0, 10), left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self, level=0, prefix="root: "):
        ret = " . " * level + prefix + repr(self.value) + "\n"
        if self.left is not None:
            ret += self.left.__repr__(level+1, " L: ")
        if self.right is not None:
            ret += self.right.__repr__(level+1, " R: ")
        return ret


def insert_random(node, depth=3):
    if depth == 0 or node is None:
        return
    node.left = TreeNode(random.randint(0, 10))
    node.right = TreeNode(random.randint(0, 10))
    insert_random(node.left, depth-1)
    insert_random(node.right, depth-1)