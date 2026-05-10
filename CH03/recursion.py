"""
Lab 03: Recursion
Implement recursive functions from Chapter 3.

Every recursive function has two cases:
1. Base case - when the function doesn't call itself
2. Recursive case - when the function calls itself
"""
from typing import List


def countdown(i: int) -> None:
    """
    Print countdown from i to 0.
    
    From Chapter 3 (page 45):
    Base case: i <= 0
    Recursive case: print i, then countdown(i-1)
    """
    if i <= 0:
        print(0)
        return
    
    print(i)
    countdown(i - 1)


def fact(x: int) -> int:
    """
    Calculate factorial of x recursively.
    
    From Chapter 3 (page 49):
    fact(5) = 5 * 4 * 3 * 2 * 1 = 120
    
    Base case: x == 1, return 1
    Recursive case: x * fact(x-1)
    """
    if x <= 1:
        return 1
    
    return x * fact(x - 1)


def recursive_sum(arr: List[int]) -> int:
    """
    Sum all elements in array recursively.
    
    Base case: empty array, return 0
    Recursive case: first element + sum of rest
    
    Example:
        >>> recursive_sum([2, 4, 6])
        12
    """
    if not arr:  
        return 0
    
    return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr: List) -> int:
    """
    Count elements in array recursively.
    
    Base case: empty array, return 0
    Recursive case: 1 + count of rest
    """
    if not arr:
        return 0
    
    return 1 + recursive_count(arr[1:])


def recursive_max(arr: List[int]) -> int:
    """
    Find maximum element recursively.
    
    Base case: single element, return it
    Recursive case: max of (first, max of rest)
    """
 
    if len(arr) == 1:
        return arr[0]
    

    rest_max = recursive_max(arr[1:])
    return arr[0] if arr[0] > rest_max else rest_max


# Test functions
if __name__ == "__main__":
    print("Testing countdown:")
    countdown(7)
    
    print("\nTesting factorial:")
    print(f"fact(8) = {fact(8)}")  
    
    print("\nTesting recursive_sum:")
    print(f"recursive_sum([4, 6, 8]) = {recursive_sum([4, 6, 8])}")  
    
    print("\nTesting recursive_count:")
    print(f"recursive_count([10, 12, 14, 16, 18]) = {recursive_count([10, 12, 14, 16, 18])}")  
    
    print("\nTesting recursive_max:")
    print(f"recursive_max([6, 10, 15, 22, 1]) = {recursive_max([6, 10, 15, 22, 1])}")  