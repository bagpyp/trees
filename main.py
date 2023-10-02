from tree_node import TreeNode, insert_random

def depth_first(node: TreeNode, order: str, path=None):
    if path is None:
        path = []
    if node is None:
        return
    if order == 'pre':
        path.append(node.value)
        depth_first(node.left, order, path)
        depth_first(node.right, order, path)
    elif order == 'in':
        depth_first(node.left, order, path)
        path.append(node.value)
        depth_first(node.right, order, path)
    else: 
        depth_first(node.left, order, path)
        depth_first(node.right, order, path)
        path.append(node.value)
    return path

def breadth_first(node: TreeNode):
    path = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        path.append(node.value)
        if node and node.left:
            queue.append(node.left)
        if node and node.right:
            queue.append(node.right)
    return path


if __name__ == "__main__":
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right.left = TreeNode('F')
    root.right.right = TreeNode('G')
    root.left.left.left = TreeNode('H')
    root.left.left.right = TreeNode('I')
    root.left.right.left = TreeNode('J')
    root.left.right.right = TreeNode('K')
    root.right.left.left = TreeNode('L')
    root.right.left.right = TreeNode('M')
    root.right.right.left = TreeNode('N')
    root.right.right.right = TreeNode('O')
    print('Tree Structure:\n', root)

    print('Traversals:')
    print('Preorder:      ', depth_first(root, 'pre'))
    print('Inorder:       ', depth_first(root, 'in'))
    print('Postorder:     ', depth_first(root, 'post'))

    print('Breadth First: ', breadth_first(root))



