"""
Lab 08: Balanced Trees
Implement AVL tree from Chapter 8.

Chapter 8 covers:
- BST problems (unbalanced = O(n))
- AVL Trees (self-balancing)
- Splay Trees
- B-Trees
"""
from typing import Optional, Any, List


class AVLNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1


class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    def height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0
    
    def balance_factor(self, node: AVLNode) -> int:
        return self.height(node.left) - self.height(node.right)
    
    def rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        B = x.right
        x.right = y
        y.left = B
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x
    
    def rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        B = y.left
        y.left = x
        x.right = B
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y
    
    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)
    
    def _insert(self, node: Optional[AVLNode], value: Any) -> AVLNode:
        if node is None:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        bf = self.balance_factor(node)

        if bf > 1 and value < node.left.value:
            return self.rotate_right(node)
        if bf < -1 and value > node.right.value:
            return self.rotate_left(node)
        if bf > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if bf < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    
    def inorder(self) -> List[Any]:
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node: Optional[AVLNode], result: List) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)


if __name__ == "__main__":
    tree = AVLTree()
    for val in [10, 20, 5, 4, 15]:
        tree.insert(val)
    print("Inorder traversal:", tree.inorder())
