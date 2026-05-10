# Chapter 10: Greedy Algorithms (Truck Packing) — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 04/19/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** The greedy truck-packing algorithm sorts all boxes by volume in descending order and then iterates through them one by one, adding each box to the truck if it fits within the remaining capacity. It always picks the largest available box first, making the locally optimal choice at each step without reconsidering previous decisions.
- **Time complexity:** O(n log n) — dominated by the initial sort. The packing loop itself runs in O(n), but sorting the boxes by volume first is the most expensive step.
- **When to use it:** Greedy algorithms are well-suited for optimization problems where a locally optimal choice at each step leads to a globally good solution. The truck-packing problem is a practical example of a bin-packing variant where a fast, approximate solution is more valuable than an exhaustive search of every possible combination.

## Test Results

```
Welcome to the Truck Cargo Calculator
This program helps you calculate how to pack your cargo efficiently
using a greedy algorithm.

Truck volume: 480.00 cubic units

--- Packing Results ---
Packed 5 of 5 box(es):
  • Box A: 64.00 cubic units
  • Box D: 50.00 cubic units
  • Box B: 27.00 cubic units
  • Box C:  8.00 cubic units
  • Box E:  1.00 cubic units

Volume used : 150.00 / 480.00 cubic units
Utilization : 31.2%

Thank you for using the Truck Cargo Calculator.
```

| Box   | Dimensions (L×W×H) | Volume (cu) | Packed? | Notes                        |
|-------|--------------------|-------------|---------|------------------------------|
| Box A | 4 × 4 × 4          | 64.00       | ✅      | Largest — packed first       |
| Box D | 5 × 5 × 2          | 50.00       | ✅      | Second largest               |
| Box B | 3 × 3 × 3          | 27.00       | ✅      | Third largest                |
| Box C | 2 × 2 × 2          | 8.00        | ✅      | Fourth                       |
| Box E | 1 × 1 × 1          | 1.00        | ✅      | Smallest — packed last       |

## Reflection Questions

1. **Why is the greedy approach not always guaranteed to produce the optimal solution?**
   The greedy algorithm makes the best local choice at each step — always picking the largest box — but it never backtracks or reconsiders earlier decisions. This means it can miss combinations of smaller boxes that would collectively fill the truck more efficiently than leading with one large box. For the general bin-packing problem, finding the true optimal solution requires evaluating all possible combinations, which is NP-hard and impractical for large inputs.

2. **How does sorting by volume descending improve the greedy strategy?**
   Placing the largest boxes first maximizes the chance that the most space-consuming items fit before the truck fills up with smaller ones. If we sorted in ascending order instead, we might pack many small boxes early and then be unable to fit a large box that would have contributed far more volume. Sorting descending does not guarantee an optimal packing, but it consistently produces better utilization than random or ascending order.

3. **What is the difference between a greedy algorithm and dynamic programming for a packing problem?**
   A greedy algorithm makes one pass through the sorted items and commits to each decision immediately, running in O(n log n) but potentially missing the optimal solution. Dynamic programming considers all possible combinations of items by building up a table of optimal sub-solutions, guaranteeing the best answer but at a cost of O(n × W) time and space where W is the capacity. For large real-world packing problems, the greedy approach is preferred when speed matters and a near-optimal solution is acceptable.

## Challenges Encountered
The most challenging part of this lab was understanding why the greedy strategy does not always produce the optimal packing. It is intuitive to assume that always picking the biggest box first fills the truck best, but constructing a counterexample — a set of boxes where two medium boxes together would outperform one large box — made it clear that greedy optimizes locally, not globally. Implementing the `pack_truck` function itself was straightforward once the sorting logic was in place, but thinking carefully about the lambda key function and the `reverse=True` argument to get descending order took a bit of attention to get right.
