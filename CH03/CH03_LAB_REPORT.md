# Chapter 3: Recursion — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 02/15/2026
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** Recursion is a programming technique where a function solves a problem by calling itself on a smaller version of the same problem. Every recursive function has two parts: a base case that stops the recursion, and a recursive case that breaks the problem down and calls the function again. The call stack keeps track of each function call until the base case is reached, at which point results unwind back up to the original call.
- **Time complexity:** Varies by problem — O(n) for simple linear recursion like factorial, sum, count, and max; O(log n) for divide-and-conquer recursion like binary search; and O(2ⁿ) for naive recursive solutions like Fibonacci without memoization.
- **When to use it:** Recursion is well-suited for problems with a naturally self-similar or nested structure, such as tree traversal, divide-and-conquer algorithms, directory exploration, and mathematical sequences like factorials.

## Test Results

```
=== PART 1: countdown(5) ===
5
4
3
2
1
0

=== PART 2: fact() ===
fact(5) = 120 ✅
fact(3) = 6   ✅
fact(1) = 1   ✅
fact(0) = 1   ✅

=== PART 3: recursive_sum() ===
recursive_sum([2, 4, 6])       = 12 ✅
recursive_sum([1, 2, 3, 4, 5]) = 15 ✅
recursive_sum([10])            = 10 ✅
recursive_sum([])              = 0  ✅

=== PART 4: recursive_count() ===
recursive_count([1, 2, 3, 4, 5]) = 5 ✅
recursive_count(['a', 'b', 'c']) = 3 ✅
recursive_count([42])            = 1 ✅
recursive_count([])              = 0 ✅

=== PART 5: recursive_max() ===
recursive_max([2, 8, 3, 1, 5]) = 8  ✅
recursive_max([1, 2, 3, 4, 5]) = 5  ✅
recursive_max([5, 4, 3, 2, 1]) = 5  ✅
recursive_max([42])            = 42 ✅

=== Direct tests from recursion.py ===
fact(8)                              = 40320
recursive_sum([4, 6, 8])             = 18
recursive_count([10, 12, 14, 16, 18]) = 5
recursive_max([6, 10, 15, 22, 1])    = 22
```

| Function        | Input               | Result | Expected | Pass? |
|-----------------|---------------------|--------|----------|-------|
| countdown       | 5                   | 5→0    | 5→0      | ✅    |
| fact            | 8                   | 40320  | 40320    | ✅    |
| recursive_sum   | [4, 6, 8]           | 18     | 18       | ✅    |
| recursive_count | [10, 12, 14, 16, 18]| 5      | 5        | ✅    |
| recursive_max   | [6, 10, 15, 22, 1]  | 22     | 22       | ✅    |

## Reflection Questions

1. **What is the base case, and why is it essential in a recursive function?**
   The base case is the condition that stops the recursion from calling itself further — for example, returning 1 when `x <= 1` in the factorial function. Without a base case, the function would call itself indefinitely until Python raises a `RecursionError` due to the call stack overflowing. Every recursive function must have a base case that is reachable from any valid input to guarantee the recursion terminates.

2. **How does the call stack relate to recursion?**
   Each time a recursive function calls itself, Python adds a new frame to the call stack containing that call's local variables and its place in the code. The stack grows with each recursive call and only begins to shrink once the base case is reached and results start returning back up through each frame. This is why deep recursion on very large inputs can cause a stack overflow — the call stack has a finite size limit.

3. **When might an iterative solution be preferred over a recursive one?**
   Iterative solutions are generally preferred when the input size could be very large, since deep recursion risks hitting Python's recursion limit (default 1000 calls) and uses more memory by building up stack frames. Iteration also tends to be faster in practice for straightforward problems like summing a list or counting elements. That said, recursion often produces cleaner, more readable code for problems with naturally hierarchical structure, like tree traversal, where an iterative approach would require manually managing a stack.

## Challenges Encountered
The most challenging part of this lab was building an accurate mental model of the call stack — specifically, understanding that each recursive call is paused and held in memory until the base case is reached, and that results only start returning once the recursion begins unwinding. A common mistake I ran into early was forgetting to return the result of the recursive call, which caused functions to return `None` instead of the correct value. Tracing through a small example like `fact(4)` step by step on paper, writing out each frame as it was added and then removed from the stack, made the unwinding behavior click and helped avoid that mistake going forward.
