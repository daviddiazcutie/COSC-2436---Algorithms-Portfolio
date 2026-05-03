# Chapter 7: Binary Trees and Tree Traversal — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 03/29/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** A binary search tree (BST) stores data in a hierarchical structure where each node has at most two children. Every value smaller than a node is placed in its left subtree and every value greater is placed in its right subtree. This property makes insertion, search, and traversal all follow a predictable path through the tree without needing to examine every element.
- **Time complexity:** O(log n) on average for insertion and search in a balanced tree; O(n) in the worst case when the tree becomes a straight line (e.g., inserting already-sorted data). Inorder traversal is always O(n) since every node must be visited exactly once.
- **When to use it:** Binary search trees are well-suited for problems that require fast insertion and lookup alongside sorted access — such as implementing dictionaries, priority queues, or any application where data is frequently inserted and needs to be retrieved in sorted order.

## Test Results

```
$ python3 binary_tree.py

Tree built from: [7, 3, 9, 1, 5, 8, 10]

        7
       / \
      3   9
     / \ / \
    1  5 8  10

Inorder traversal: [1, 3, 5, 7, 8, 9, 10]

tree.search(5)   → True
tree.search(11)  → False
```

| Operation          | Input              | Result               | Notes                              |
|--------------------|--------------------|----------------------|------------------------------------|
| insert (×7)        | [7,3,9,1,5,8,10]   | Tree built           | 7 becomes root                     |
| inorder_traversal  | —                  | [1,3,5,7,8,9,10]     | ✅ Sorted ascending                |
| search             | 5                  | True                 | ✅ Found in left subtree           |
| search             | 11                 | False                | ✅ Correctly returns False         |

## Reflection Questions

1. **Why does inorder traversal of a BST always return elements in sorted order?**
   Inorder traversal visits the left subtree first, then the current node, then the right subtree. Because the BST property guarantees that everything to the left of a node is smaller and everything to the right is larger, visiting in left → root → right order naturally produces values in ascending sequence. This is why inorder traversal can be used as an O(n) sorting mechanism for data already stored in a BST.

2. **What is the worst-case time complexity for search in a BST, and when does it occur?**
   The worst case for search is O(n), and it occurs when the tree becomes completely unbalanced — for example, when data is inserted in already-sorted order. In that scenario every new node is always larger than the previous one, so each insertion goes to the right child, producing a structure that looks like a linked list rather than a tree. Searching such a tree requires traversing every node, eliminating the logarithmic advantage a balanced tree provides.

3. **How does a binary search tree differ from a binary search on a sorted array?**
   Both achieve O(log n) average search time by halving the search space at each step, but they handle insertions very differently. Inserting into a sorted array requires shifting elements to maintain order, which is O(n). Inserting into a BST only requires finding the correct leaf position and adding a new node, which is O(log n) on average. BSTs are therefore preferred when data is frequently inserted or deleted, while sorted arrays are better when the data is static and random access by index is needed.

## Challenges Encountered
The most challenging part of this lab was implementing the recursive insert and search functions correctly using nested helper functions. Understanding that each recursive call operates on a subtree — not the whole tree — required a clear mental model of what the current `node` parameter represents at each level of recursion. Tracing through the insertion of `[7, 3, 9, 1, 5, 8, 10]` step by step, drawing the tree after each insert, helped make the left/right placement logic concrete. Once the tree structure was visualized clearly, the inorder traversal and search implementations followed naturally from the same recursive pattern.
