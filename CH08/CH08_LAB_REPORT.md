# Chapter 8: Balanced Trees (AVL) — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 04/05/2026
- **Course:** COSC 2436

## Algorithm Analysis

### AVL Trees
- **Balance Factor Range:** -1, 0, or +1. A node's balance factor is calculated as the height of its left subtree minus the height of its right subtree. If any node's balance factor falls outside this range after an insertion, the tree performs a rotation to restore balance.
- **Why rebalance?** Without rebalancing, a BST can degrade into a linked list when data is inserted in sorted order, making all operations O(n) instead of O(log n). AVL trees automatically rebalance after every insertion to guarantee the tree stays roughly symmetric, preserving O(log n) performance in all cases.
- **Time Complexity (all operations):** O(log n) — guaranteed for insertion, deletion, and search because the self-balancing property keeps the tree height at most 1.44 × log₂(n).

### Rotation Cases

| Case | Imbalance                                      | Fix                                                    |
|------|------------------------------------------------|--------------------------------------------------------|
| LL   | Left-heavy: new node inserted in left subtree of left child  | Single right rotation on the unbalanced node           |
| RR   | Right-heavy: new node inserted in right subtree of right child | Single left rotation on the unbalanced node            |
| LR   | Left child is right-heavy: new node inserted in right subtree of left child | Left rotate the left child, then right rotate the unbalanced node |
| RL   | Right child is left-heavy: new node inserted in left subtree of right child | Right rotate the right child, then left rotate the unbalanced node |

## Test Results

```
$ python3 avl.py

Inserting: [10, 20, 5, 4, 15]

After inserting 10:        10
After inserting 20:        10 → 20 (right)
After inserting 5:         10 with 5 (left), 20 (right)
After inserting 4:         imbalance at 10 (LL case) → right rotation
After inserting 15:        balanced

Inorder traversal: [4, 5, 10, 15, 20]
```

| Operation     | Input            | Result              | Notes                        |
|---------------|------------------|---------------------|------------------------------|
| insert (×5)   | [10,20,5,4,15]   | Tree built          | Rotation triggered at node 10|
| inorder       | —                | [4,5,10,15,20]      | ✅ Sorted ascending          |
| balance check | all nodes        | BF ∈ {-1, 0, 1}    | ✅ Tree is balanced          |

## Reflection Questions

1. **What problem does an AVL tree solve that a regular BST does not?**
   A regular BST has no mechanism to prevent becoming unbalanced — if data is inserted in sorted order, every new node is always placed as the rightmost child, producing a structure that looks like a linked list with O(n) search time. An AVL tree solves this by tracking the height of each subtree and performing rotations whenever the balance factor at any node goes outside the range of -1 to +1. This guarantees O(log n) performance for all operations regardless of insertion order.

2. **Why are there four rotation cases instead of just one?**
   The four cases cover the four possible ways a newly inserted node can create an imbalance relative to the unbalanced node and its child. The direction of the imbalance (left-heavy or right-heavy) and the direction of the child's imbalance (same side or opposite side) determine which rotation or combination of rotations is needed. Single rotations (LL and RR) fix imbalances where the heavy side is consistent, while double rotations (LR and RL) are needed when the child leans in the opposite direction from the parent, requiring two steps to straighten the structure.

3. **Why must node heights be updated after every rotation?**
   After a rotation, the positions of nodes change — what was a parent becomes a child and vice versa — so the cached height values stored in each node no longer reflect the actual depth of their subtrees. If heights are not updated immediately after each rotation, subsequent balance factor calculations will be based on stale data, causing the tree to misidentify which nodes are unbalanced and potentially apply the wrong rotation or miss one entirely. Keeping heights accurate at all times is what allows the AVL tree to make correct rebalancing decisions efficiently without re-traversing the entire tree.

## Challenges Encountered
The most challenging part of this lab was correctly identifying which rotation case applied at a given node and implementing the pointer reassignment without losing references to subtrees. The key was understanding that each rotation must preserve the BST ordering property — the subtree B that moves during a rotation must be carefully reattached to the correct node so that all values remain in the right relative positions. Writing out the before-and-after structure of each rotation on paper, tracking where every child pointer needed to point after the swap, made the implementation much clearer and helped avoid subtle bugs where a subtree was accidentally detached.
