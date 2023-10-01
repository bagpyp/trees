from tree_node import TreeNode, insert_random

def preorder(node: TreeNode, path=None):
    if path is None:
        path = []
    if node is None:
        return
    path.append(node.value)
    preorder(node.left, path)
    preorder(node.right, path)
    return path

def inorder(node: TreeNode, path=None):
    if path is None:
        path = []
    if node is None:
        return
    inorder(node.left, path)
    path.append(node.value)
    inorder(node.right, path)
    return path

def postorder(node: TreeNode, path=None):
    if path is None:
        path = []
    if node is None:
        return
    postorder(node.left, path)
    postorder(node.right, path)
    path.append(node.value)
    return path


if __name__ == "__main__":
    root = TreeNode()
    insert_random(root)
    print(root)

    print('preorder ', preorder(root))
    print('inorder  ', inorder(root))
    print('postorder', postorder(root))




