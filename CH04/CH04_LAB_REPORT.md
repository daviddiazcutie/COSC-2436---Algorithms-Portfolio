# Chapter 4: Quicksort — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 02/22/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Quicksort is a divide-and-conquer sorting algorithm that selects a pivot element, partitions the remaining elements into two groups (those less than or equal to the pivot and those greater), and then recursively sorts each group. The sorted result is assembled by combining the sorted left group, the pivot, and the sorted right group.
- **Time complexity:** O(n log n) on average and in the best case; O(n²) in the worst case when the pivot consistently produces unbalanced partitions.
- **When to use it:** Quicksort is well-suited for large datasets where average-case performance matters and memory usage should be kept low. It is one of the fastest general-purpose sorting algorithms in practice and is widely used in standard libraries.

## Quicksort Concepts

### Divide and Conquer
Quicksort breaks the sorting problem into smaller subproblems by choosing a pivot and splitting the array around it. Instead of sorting the entire array at once, it sorts two smaller arrays — one with elements smaller than the pivot and one with elements larger — and trusts that combining those sorted halves with the pivot in the middle produces a fully sorted result. This is divide and conquer: divide the problem, conquer the pieces recursively, combine the results.

### The Three Steps
1. **Choose pivot:** Select one element from the array to act as the reference point. In this implementation, the first element is always chosen as the pivot.
2. **Partition:** Scan the rest of the array (`array[1:]`) and split elements into two lists — `less` for elements ≤ pivot, and `greater` for elements > pivot.
3. **Recurse and combine:** Recursively apply quicksort to both `less` and `greater`, then concatenate: `quicksort(less) + [pivot] + quicksort(greater)`.

## Tracing Quicksort

### Trace: `quicksort([3, 5, 2, 1, 4])`

```
quicksort([3, 5, 2, 1, 4])
  pivot = 3
  less    = [2, 1]
  greater = [5, 4]
  → quicksort([2, 1]) + [3] + quicksort([5, 4])

    quicksort([2, 1])
      pivot = 2
      less    = [1]
      greater = []
      → quicksort([1]) + [2] + quicksort([])
          quicksort([1]) → [1]   ← base case
          quicksort([])  → []    ← base case
      → [1, 2]

    quicksort([5, 4])
      pivot = 5
      less    = [4]
      greater = []
      → quicksort([4]) + [5] + quicksort([])
          quicksort([4]) → [4]   ← base case
          quicksort([])  → []    ← base case
      → [4, 5]

Final: [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]
```

## Complexity Analysis

| Case    | Time Complexity | Why?                                                                                                                         |
|---------|-----------------|------------------------------------------------------------------------------------------------------------------------------|
| Best    | O(n log n)      | The pivot splits the array into two equal halves every time, producing log n levels of recursion each scanning n elements.   |
| Average | O(n log n)      | On random data, the pivot tends to produce reasonably balanced partitions, keeping the recursion depth close to log n levels. |
| Worst   | O(n²)           | If the pivot is always the smallest or largest element (e.g., sorted input with first-element pivot), one partition is always empty and the other has n−1 elements, producing n levels of recursion. |

## Test Results

```
$ python3 quicksort.py

quicksort([10, 5, 2, 3])         → [2, 3, 5, 10]
quicksort([33, 15, 10])          → [10, 15, 33]
quicksort([3, 5, 2, 1, 4])       → [1, 2, 3, 4, 5]
quicksort([1])                   → [1]
quicksort([])                    → []
quicksort([8, 7, 6, 5, 4, 3, 2, 1]) → [1, 2, 3, 4, 5, 6, 7, 8]
```

| Input                     | Output                    | Pass? |
|---------------------------|---------------------------|-------|
| [10, 5, 2, 3]             | [2, 3, 5, 10]             | ✅    |
| [33, 15, 10]              | [10, 15, 33]              | ✅    |
| [3, 5, 2, 1, 4]           | [1, 2, 3, 4, 5]           | ✅    |
| [1]                       | [1]                       | ✅    |
| []                        | []                        | ✅    |
| [8, 7, 6, 5, 4, 3, 2, 1]  | [1, 2, 3, 4, 5, 6, 7, 8]  | ✅    |

## Reflection Questions

1. **What happens if the array is already sorted and you always pick the first element as pivot?**
   When the array is already sorted and the first element is always chosen as the pivot, the partition is maximally unbalanced — `less` is empty and `greater` contains all remaining elements. This causes the recursion to go n levels deep instead of log n, and each level still scans all remaining elements, producing O(n²) total work. This is the worst case for this pivot strategy, and it is a common real-world scenario that naive quicksort handles poorly.

2. **How could you improve pivot selection to avoid worst-case performance?**
   A common improvement is the "median-of-three" strategy, which selects the median of the first, middle, and last elements as the pivot. This makes it much less likely to consistently pick the smallest or largest element, keeping partitions more balanced on sorted or nearly-sorted input. Another approach is to choose the pivot randomly, which makes worst-case behavior extremely unlikely regardless of the input's initial order.

3. **How does quicksort compare to other sorting algorithms you know (e.g., selection sort, merge sort)?**
   Selection sort runs in O(n²) in all cases, making it significantly slower than quicksort for large inputs. Merge sort also runs in O(n log n) in all cases including the worst, which gives it a more reliable performance guarantee than quicksort. However, quicksort tends to be faster in practice than merge sort because it sorts in place (in optimized implementations) and has better cache performance, which is why it is commonly used in standard library implementations despite its O(n²) worst case.

4. **Why do we use `array[1:]` instead of `array` when building the less and greater lists?**
   The pivot is `array[0]`, so if we used the full `array` when building `less` and `greater`, the pivot itself would be included in one of the partitions and sorted again. Using `array[1:]` excludes the pivot from both lists, ensuring it is placed exactly once in its correct position in the final result. Without this, the algorithm would not only produce incorrect output but could also loop infinitely since the problem size would never shrink.

## Challenges Encountered
The trickiest part of this lab was understanding why the base case is `len(array) < 2` rather than checking for an empty array. An array with one element is already sorted by definition, so returning it immediately without any partitioning is correct — and necessary, since trying to select a pivot from a single-element array would still work but recurse unnecessarily. Tracing through `quicksort([3, 5, 2, 1, 4])` step by step on paper, tracking the pivot, `less`, and `greater` at every level, made the recursion structure clear and helped confirm the implementation was correct before running it.
