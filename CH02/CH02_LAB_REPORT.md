# Chapter 2: Selection Sort — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 02/08/2026
- **Course:** COSC 2436

## Algorithm Analysis

### Selection Sort
- **Time Complexity:** O(n²)
- **How it works:** Selection sort works by repeatedly scanning the unsorted portion of the list to find the smallest element and swapping it into its correct position. It starts at index 0, finds the minimum of the entire list and places it first, then finds the minimum of the remaining elements and places it second, continuing until the list is fully sorted.

### Arrays vs Linked Lists

| Operation | Array | Linked List | Why?                                                                                          |
|-----------|-------|-------------|-----------------------------------------------------------------------------------------------|
| Read      | O(1)  | O(n)        | Arrays store elements in contiguous memory, so any index is directly addressable. Linked lists must follow pointers from the head to reach a given position. |
| Insert    | O(n)  | O(1)        | Inserting into an array requires shifting all subsequent elements to make room. A linked list insert only updates a couple of pointers. |
| Delete    | O(n)  | O(1)        | Arrays must shift all elements after the deleted position. Linked lists simply re-link the surrounding nodes. |

## Test Results

```
=== PART 1: Selection Sort ===

Top 5 Smallest Cities by Population:
1. Lochbuie, CO        — population:  13,047
2. Mead, CO            — population:  14,081
3. Windsor, CO         — population:  31,765
4. Brighton, CO        — population:  38,700
5. Northglenn, CO      — population:  40,343

Top 5 Largest Cities by Population:
1. New York, NY        — population: 8,336,817
2. Los Angeles, CA     — population: 3,979,576
3. Chicago, IL         — population: 2,693,976
4. Houston, TX         — population: 2,304,580
5. Phoenix, AZ         — population: 1,608,139

=== PART 2: Array vs Linked List ===

Array access by index [0]:    0.000001s  — O(1)
Array insert at beginning:    0.000012s  — O(n) (elements shifted)

Linked list insert at head:   0.000001s  — O(1) (pointer update only)
Linked list search "Houston": 0.000018s  — O(n) (traversed from head)

=== PART 3: Big O Summary ===

| Algorithm         | Time Complexity |
|-------------------|-----------------|
| Selection Sort    | O(n²)           |
| Python Timsort    | O(n log n)      |
```

## Reflection Questions

1. **Why is selection sort O(n²)?**
   For each of the n elements in the list, the algorithm must scan all remaining unsorted elements to find the minimum — that inner scan itself runs up to n times. This nested structure (a loop inside a loop) produces n × n total operations in the worst case, which simplifies to O(n²). Even when the list is already sorted, selection sort still performs all the same comparisons because it has no mechanism to detect early termination.

2. **When would you choose a linked list over an array?**
   A linked list is preferable when your program performs frequent insertions or deletions, especially at the beginning or middle of the collection, since those operations are O(1) compared to O(n) for arrays. A good real-world example is implementing a queue or a playlist where items are constantly being added and removed. Arrays are the better choice when you need fast random access by index, since linked lists require traversing from the head each time.

## Challenges Encountered
The trickiest part of this lab was implementing `find_smallest_index` correctly and then integrating it cleanly into `selection_sort` without duplicating the inner loop logic. Initially the inner scan was written twice — once inside `find_smallest_index` and again inline inside `selection_sort` — which was redundant. Refactoring `selection_sort` to call `find_smallest_index` for the ascending case eliminated the duplication and made the code easier to follow. Adding empty-list guards to both functions was also a small but important detail to prevent index errors on edge-case inputs.
