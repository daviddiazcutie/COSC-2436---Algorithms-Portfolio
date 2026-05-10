"""
Lab 03: Recursion - Interactive Tutorial & Test Runner
=====================================================
Every recursive function has TWO parts:
1. BASE CASE - When to STOP (no more recursive calls)
2. RECURSIVE CASE - Call yourself with a smaller problem

Think of it like Russian nesting dolls - each doll contains a smaller one,
until you reach the smallest doll (base case).

HOW TO RUN:
-----------
    python main.py           # Run this tutorial
    python -m pytest tests/ -v   # Run the grading tests
"""

from recursion import countdown, fact, recursive_sum, recursive_count, recursive_max


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def demo_countdown() -> None:
    """Demonstrate the countdown function."""
    print_header("PART 1: countdown()")
    
    print("""
    RECURSION PATTERN:
    
    def countdown(i):
        if i <= 0:           # BASE CASE: stop when i is 0 or less
            print("Done!")
            return
        print(i)             # Do something
        countdown(i - 1)     # RECURSIVE CASE: call with smaller number
    
    This is like a for loop, but using recursion!
    
    C++/Java equivalent:
        for (int j = i; j > 0; j--) { cout << j << endl; }
    """)
    
    print("Testing countdown(5):")
    print("-" * 20)
    try:
        countdown(5)
        print("-" * 20)
        print("✅ If you saw 5, 4, 3, 2, 1 printed above, it works!")
    except Exception as e:
        print(f"❌ Error: {e}")


def demo_factorial() -> None:
    """Demonstrate the factorial function."""
    print_header("PART 2: fact() - Factorial")
    
    print("""
    FACTORIAL: n! = n × (n-1) × (n-2) × ... × 1
    
    Examples:
        5! = 5 × 4 × 3 × 2 × 1 = 120
        3! = 3 × 2 × 1 = 6
        1! = 1 (base case)
    
    RECURSIVE THINKING:
        fact(5) = 5 × fact(4)
        fact(4) = 4 × fact(3)
        fact(3) = 3 × fact(2)
        fact(2) = 2 × fact(1)
        fact(1) = 1  ← BASE CASE!
    
    Then it "unwinds":
        fact(2) = 2 × 1 = 2
        fact(3) = 3 × 2 = 6
        fact(4) = 4 × 6 = 24
        fact(5) = 5 × 24 = 120
    """)
    
    test_cases = [(5, 120), (3, 6), (1, 1), (0, 1)]
    
    for n, expected in test_cases:
        print(f"fact({n}):", end=" ")
        try:
            result = fact(n)
            if result == expected:
                print(f"✅ {result}")
            elif result is None:
                print("❌ Returned None - did you forget to return?")
            else:
                print(f"❌ Got {result}, expected {expected}")
        except Exception as e:
            print(f"❌ Error: {e}")


def demo_recursive_sum() -> None:
    """Demonstrate recursive sum."""
    print_header("PART 3: recursive_sum()")
    
    print("""
    SUM AN ARRAY RECURSIVELY:
    
    Base case: empty array → return 0
    Recursive case: first element + sum of rest
    
    Example: recursive_sum([2, 4, 6])
        = 2 + recursive_sum([4, 6])
        = 2 + (4 + recursive_sum([6]))
        = 2 + (4 + (6 + recursive_sum([])))
        = 2 + (4 + (6 + 0))  ← base case!
        = 2 + (4 + 6)
        = 2 + 10
        = 12
    
    PYTHON TIP - Getting first element and rest:
        arr[0]   → first element
        arr[1:]  → rest of array (everything except first)
    """)
    
    test_cases = [
        ([2, 4, 6], 12),
        ([1, 2, 3, 4, 5], 15),
        ([10], 10),
        ([], 0),
    ]
    
    for arr, expected in test_cases:
        print(f"recursive_sum({arr}):", end=" ")
        try:
            result = recursive_sum(arr)
            if result == expected:
                print(f"✅ {result}")
            elif result is None:
                print("❌ Returned None")
            else:
                print(f"❌ Got {result}, expected {expected}")
        except Exception as e:
            print(f"❌ Error: {e}")


def demo_recursive_count() -> None:
    """Demonstrate recursive count."""
    print_header("PART 4: recursive_count()")
    
    print("""
    COUNT ELEMENTS RECURSIVELY:
    
    Base case: empty array → return 0
    Recursive case: 1 + count of rest
    
    This is like len() but implemented with recursion!
    """)
    
    test_cases = [
        ([1, 2, 3, 4, 5], 5),
        (["a", "b", "c"], 3),
        ([42], 1),
        ([], 0),
    ]
    
    for arr, expected in test_cases:
        print(f"recursive_count({arr}):", end=" ")
        try:
            result = recursive_count(arr)
            if result == expected:
                print(f"✅ {result}")
            elif result is None:
                print("❌ Returned None")
            else:
                print(f"❌ Got {result}, expected {expected}")
        except Exception as e:
            print(f"❌ Error: {e}")


def demo_recursive_max() -> None:
    """Demonstrate recursive max."""
    print_header("PART 5: recursive_max()")
    
    print("""
    FIND MAXIMUM RECURSIVELY:
    
    Base case: single element → return it
    Recursive case: max(first element, max of rest)
    
    Example: recursive_max([2, 8, 3])
        = max(2, recursive_max([8, 3]))
        = max(2, max(8, recursive_max([3])))
        = max(2, max(8, 3))  ← base case!
        = max(2, 8)
        = 8
    
    PYTHON TIP:
        max(a, b) returns the larger of two values
    """)
    
    test_cases = [
        ([2, 8, 3, 1, 5], 8),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 5),
        ([42], 42),
    ]
    
    for arr, expected in test_cases:
        print(f"recursive_max({arr}):", end=" ")
        try:
            result = recursive_max(arr)
            if result == expected:
                print(f"✅ {result}")
            elif result is None:
                print("❌ Returned None")
            else:
                print(f"❌ Got {result}, expected {expected}")
        except Exception as e:
            print(f"❌ Error: {e}")


def recursion_tips() -> None:
    """Show recursion tips."""
    print_header("RECURSION TIPS")
    
    print("""
    🔑 KEY CONCEPTS:
    
    1. ALWAYS define your base case first!
       - What's the simplest input? (empty list, 0, 1, etc.)
       - What should you return for that input?
    
    2. Trust the recursion!
       - Assume your function works for smaller inputs
       - Just handle the current step + recursive call
    
    3. Make progress toward base case
       - Each recursive call should have a "smaller" problem
       - arr[1:] is smaller than arr
       - n-1 is smaller than n
    
    ⚠️ COMMON MISTAKES:
    
    1. Forgetting the base case → infinite recursion → stack overflow!
    2. Not returning the result of recursive call
       WRONG:  recursive_sum(arr[1:])
       RIGHT:  return arr[0] + recursive_sum(arr[1:])
    
    3. Not making progress toward base case
       WRONG:  return fact(n)      # calls itself with same n!
       RIGHT:  return n * fact(n-1)  # n-1 is smaller
    
    💡 DEBUGGING:
    
    Add print statements to trace execution:
        def fact(n):
            print(f"fact({n}) called")
            if n <= 1:
                print(f"  Base case! Returning 1")
                return 1
            result = n * fact(n - 1)
            print(f"  fact({n}) returning {result}")
            return result
    """)


def main():
    """Main entry point."""
    print("\n" + "🔄" * 30)
    print("   LAB 03: RECURSION")
    print("   Functions that call themselves!")
    print("🔄" * 30)
    
    print("""
    📋 YOUR TASKS:
    1. Open recursion.py
    2. Implement all 5 functions:
       - countdown()
       - fact()
       - recursive_sum()
       - recursive_count()
       - recursive_max()
    3. Run this file to test: python main.py
    4. Run pytest when ready: python -m pytest tests/ -v
    """)
    
    demo_countdown()
    demo_factorial()
    demo_recursive_sum()
    demo_recursive_count()
    demo_recursive_max()
    recursion_tips()
    
    print_header("NEXT STEPS")
    print("""
    When all tests pass here, run: python -m pytest tests/ -v
    Then complete the Lab Report in README.md
    """)


if __name__ == "__main__":
    main()
