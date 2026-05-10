import time
import math
import timeit

def linear_search(arr, item):
    """
    Performs linear search on an array.
    Returns the index if found, None otherwise.
    """
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return None

def binary_search(arr, item):
    """
    Performs binary search on a sorted array.
    Returns the index if found, None otherwise.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def count_linear_steps(arr, item):
    """Returns the number of comparisons linear search makes."""
    for i in range(len(arr)):
        if arr[i] == item:
            return i + 1
    return len(arr)  # Full traversal if not found

def count_binary_steps(arr, item):
    """Returns the number of comparisons binary search makes."""
    low, high, steps = 0, len(arr) - 1, 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return steps
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return steps  # Item not found

def time_search_comparison(arr, target, repetitions=10_000):
    """
    Times both algorithms averaged over many repetitions for stable results.
    Returns (linear_time, binary_time, linear_result, binary_result).
    """
    linear_result = linear_search(arr, target)
    binary_result = binary_search(arr, target)

    # timeit disables garbage collection and repeats the call, giving
    # a much more stable reading than a single time.perf_counter() pair.
    linear_time = timeit.timeit(lambda: linear_search(arr, target),
                                number=repetitions) / repetitions
    binary_time  = timeit.timeit(lambda: binary_search(arr, target),
                                 number=repetitions) / repetitions

    return linear_time, binary_time, linear_result, binary_result

if __name__ == "__main__":
    sorted_names = list(range(1, 129))           # [1, 2, ..., 128]
    test_items   = [1, 64, 128, 50, 100, 25, 75, 10, 90, 200]

    print("Binary Search vs Linear Search — Time Comparison")
    print("=" * 52)
    print(f"Dataset: sorted list of {len(sorted_names)} numbers")
    print(f"Each timing averaged over 10,000 runs\n")

    for item in test_items:
        lin_time, bin_time, lin_result, bin_result = time_search_comparison(sorted_names, item)

        lin_steps = count_linear_steps(sorted_names, item)
        bin_steps = count_binary_steps(sorted_names, item)

        found_at   = f"index {lin_result}" if lin_result is not None else "not found"
        speedup    = f"{lin_time / bin_time:.2f}x faster" if bin_time > 0 else "n/a"

        print(f"Target: {item} ({found_at})")
        print(f"  Linear  — {lin_time * 1e6:7.3f} µs   {lin_steps:3d} steps")
        print(f"  Binary  — {bin_time * 1e6:7.3f} µs   {bin_steps:3d} steps  ({speedup})")
        print()

    print("Lab Challenge Answer")
    print("-" * 30)
    max_steps = math.ceil(math.log2(len(sorted_names)))
    print(f"log₂(128) = {max_steps} steps maximum for binary search")
    print(f"Worst-case linear search: {len(sorted_names)} steps")
    print(f"Theoretical max speedup:  {len(sorted_names)}/{max_steps} = "
          f"{len(sorted_names)/max_steps:.1f}x")
