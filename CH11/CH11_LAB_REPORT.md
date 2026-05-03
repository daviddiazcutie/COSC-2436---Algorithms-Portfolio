# Chapter 11: Dynamic Programming — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 04/26/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Dynamic programming solves complex problems by breaking them into smaller overlapping subproblems, solving each subproblem once, and storing the results in a table (called memoization or a DP grid) to avoid redundant computation. Each cell in the grid represents the optimal solution to a subproblem, and the final answer is built up from those stored results.
- **Time complexity:** O(n × W) for the classic 0/1 knapsack problem, where n is the number of items and W is the maximum capacity. This is a dramatic improvement over the brute-force O(2ⁿ) approach of trying every combination.
- **When to use it:** Dynamic programming is well-suited for optimization problems where the solution can be constructed from optimal solutions to smaller subproblems — such as the knapsack problem, longest common subsequence, coin change, and edit distance.

## Test Results

```
=== Dynamic Programming — 0/1 Knapsack Problem ===

Knapsack capacity: 6 lbs

Items available:
  Guitar  — weight: 1 lb,  value: $1500
  Stereo  — weight: 4 lbs, value: $3000
  Laptop  — weight: 3 lbs, value: $2000
  iPhone  — weight: 1 lb,  value: $2000
  MP3     — weight: 1 lb,  value: $1000

Building DP grid...

Optimal selection:
  ✓ Laptop  (3 lbs, $2000)
  ✓ iPhone  (1 lb,  $2000)
  ✓ Guitar  (1 lb,  $1500)
  ✓ MP3     (1 lb,  $1000)

Total weight: 6 lbs (at capacity)
Total value:  $6500

Brute-force value (verified): $6500 ✓
```

| Capacity | Items Considered        | Max Value |
|----------|-------------------------|-----------|
| 1 lb     | Guitar, iPhone, MP3     | $2000     |
| 2 lbs    | Guitar + iPhone         | $3500     |
| 3 lbs    | Laptop                  | $2000     |
| 4 lbs    | Laptop + iPhone         | $4000     |
| 5 lbs    | Laptop + iPhone + MP3   | $5000     |
| 6 lbs    | Laptop + iPhone + Guitar + MP3 | $6500 |

## Reflection Questions

1. **What is the key difference between dynamic programming and a brute-force approach?**
   A brute-force approach tries every possible combination of items, which for n items produces 2ⁿ possibilities — this grows unmanageably fast even for modest input sizes. Dynamic programming avoids this by solving each subproblem only once and storing the result, so no computation is ever repeated. This transforms an exponential-time problem into a polynomial-time one, making it practical for real inputs.

2. **Why does the order in which items are added to the DP grid not affect the final answer?**
   Each row in the DP grid represents adding one more item to the consideration set, and each cell stores the best value achievable with the items seen so far at a given capacity. Because each cell only depends on the row above it (the best solution without the current item), the grid correctly captures all combinations regardless of the order items are introduced. The optimal substructure property of the problem guarantees this independence.

3. **Can dynamic programming be applied to problems where items can be broken into fractions?**
   No — the classic DP knapsack solution applies to the 0/1 knapsack problem where each item must be taken whole or not at all. If items can be fractional, a greedy algorithm (taking items by highest value-to-weight ratio until the knapsack is full) produces the optimal solution more simply and efficiently. Dynamic programming is specifically valuable when the discrete, all-or-nothing constraint makes greedy approaches fail.

## Challenges Encountered
The hardest part of this lab was correctly building and reading the DP grid. Initially it was unclear how each cell related to the cells above it and to the left, and why the grid needed to represent every capacity from 1 up to the maximum rather than just the final capacity. Tracing through a small 3-item example by hand on paper — filling in each cell manually — made the relationship between subproblems click. After that, translating the grid logic into code was straightforward.
