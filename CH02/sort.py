from typing import List, Any, Callable


def find_smallest_index(arr: List[Any], key: Callable = lambda x: x, start: int = 0) -> int:
    """
    Find the index of the smallest element starting from 'start' position.
    
    Args:
        arr: List to search
        key: Function to extract comparison value
        start: Starting index
    
    Returns:
        Index of smallest element
    """
    smallest_index = start
    smallest_value = key(arr[start])
    
    for i in range(start + 1, len(arr)):
        if key(arr[i]) < smallest_value:
            smallest_index = i
            smallest_value = key(arr[i])
    
    return smallest_index


def selection_sort(arr: List[Any], key: Callable = lambda x: x, reverse: bool = False) -> List[Any]:
    """
    Sort list using selection sort algorithm.
    
    Args:
        arr: List to sort
        key: Function to extract comparison value
        reverse: If True, sort descending
    
    Returns:
        New sorted list (does not modify original)
    """
    result = list(arr)  # Create copy
    n = len(result)
    
    for i in range(n):
        # Find extreme element (min or max depending on reverse)
        extreme_idx = i
        extreme_val = key(result[i])
        
        for j in range(i + 1, n):
            current_val = key(result[j])
            if reverse:
                if current_val > extreme_val:
                    extreme_idx = j
                    extreme_val = current_val
            else:
                if current_val < extreme_val:
                    extreme_idx = j
                    extreme_val = current_val
        
        # Swap
        if extreme_idx != i:
            result[i], result[extreme_idx] = result[extreme_idx], result[i]
    
    return result


def python_builtin_sort(arr: List[Any], key: Callable = lambda x: x, reverse: bool = False) -> List[Any]:
    """
    Sort using Python's built-in sorted() for comparison.
    
    Args:
        arr: List to sort
        key: Function to extract comparison value
        reverse: If True, sort descending
    
    Returns:
        New sorted list
    """
    return sorted(arr, key=key, reverse=reverse)
