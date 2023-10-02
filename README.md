# Breadth First and Depth First Search
Simple binary tree `__repr__` 
BFSvwith a queue and DFS (pre- in- and post-order) using recursion
 
run `main.py`

```
Tree Structure:
 root: 'A'
 .  left : 'B'
 .  .  left : 'D'
 .  .  .  left : 'H'
 .  .  .  right: 'I'
 .  .  right: 'E'
 .  .  .  left : 'J'
 .  .  .  right: 'K'
 .  right: 'C'
 .  .  left : 'F'
 .  .  .  left : 'L'
 .  .  .  right: 'M'
 .  .  right: 'G'
 .  .  .  left : 'N'
 .  .  .  right: 'O'

Traversals:
Preorder:       ['A', 'B', 'D', 'H', 'I', 'E', 'J', 'K', 'C', 'F', 'L', 'M', 'G', 'N', 'O']
Inorder:        ['H', 'D', 'I', 'B', 'J', 'E', 'K', 'A', 'L', 'F', 'M', 'C', 'N', 'G', 'O']
Postorder:      ['H', 'I', 'D', 'J', 'K', 'E', 'B', 'L', 'M', 'F', 'N', 'O', 'G', 'C', 'A']
Breadth First:  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
```