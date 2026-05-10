# Chapter 1 Lab Report: Search Algorithms

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 01/21/2026
- **Course:** COSC 2436

## Algorithm Summary

### Linear Search
Linear search is a basic algorithm that checks every element in a list sequentially from the first to the last. 
- **Time Complexity:** $O(n)$
- **Usage:** Best for small or unsorted datasets where the overhead of sorting for binary search isn't worth the effort.

### Binary Search
Binary search is a "divide and conquer" algorithm. It finds the median of a sorted list and eliminates half of the remaining data in each step.
- **Time Complexity:** $O(\log n)$
- **Usage:** Essential for large datasets. Note that the data **must** be sorted for this algorithm to function correctly.



## Test Results
Running comparison on a sorted list of 128 items:

| Target | Linear Time (s) | Binary Time (s) | Speedup |
| :--- | :--- | :--- | :--- |
| 1 (Start) | 0.00000191 | 0.00000119 | 1.60x |
| 64 (Middle) | 0.00000310 | 0.00000095 | 3.26x |
| 128 (End) | 0.00000405 | 0.00000095 | 4.26x |
| 200 (Missing)| 0.00000405 | 0.00000095 | 4.26x |

**Lab Challenge Answer:**
For a list of 128 items, the maximum steps for binary search is $\log_2(128) = \mathbf{7}$ **steps**.

## Challenges and Solutions
- **Consistency:** Ensuring ISBNs were treated as strings prevented type-matching errors during search.
- **Sorting Requirement:** I learned that Binary Search will fail silently or return `None` if the list is not sorted beforehand.

## Learning Outcomes
I gained a practical understanding of $O(n)$ vs $O(\log n)$. Seeing binary search remain constant at ~0.95 microseconds while linear search increased with the index proved the
