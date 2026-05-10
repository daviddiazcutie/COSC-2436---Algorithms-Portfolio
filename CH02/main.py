"""
Lab 2: Main Program
Demonstrates selection sort and array vs linked list.
"""
import json
import time
from sort import selection_sort, python_builtin_sort
from linked_list import LinkedList


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def time_sort(fn, *args, **kwargs):
    """Run a sort function and return (result, elapsed_seconds)."""
    start = time.perf_counter()
    result = fn(*args, **kwargs)
    return result, time.perf_counter() - start


def print_cities(cities: list, n: int = 5) -> None:
    """Print the first n cities with rank, name, and population."""
    for rank, city in enumerate(cities[:n], 1):
        print(f"  {rank}. {city['name']:<20} {city['population']:>10,}")


def main():
    # Load city data
    cities = load_cities('data/cities.json')
    print(f"Loaded {len(cities)} cities\n")

    pop = lambda c: c['population']   # reusable key

    # =========================================
    # PART 1: Selection Sort
    # =========================================
    print("=" * 52)
    print("PART 1: Selection Sort")
    print("=" * 52)

    # --- Ascending (smallest first) ---
    asc_sel, t_asc = time_sort(selection_sort, cities, key=pop)
    print(f"\nTop 5 smallest cities (selection sort, {t_asc*1e6:.1f} µs):")
    print_cities(asc_sel)

    # --- Descending (largest first) ---
    desc_sel, t_desc = time_sort(selection_sort, cities, key=pop, reverse=True)
    print(f"\nTop 5 largest cities (selection sort, {t_desc*1e6:.1f} µs):")
    print_cities(desc_sel)

    # --- Compare with Python's built-in Timsort ---
    _, t_builtin_asc  = time_sort(python_builtin_sort, cities, key=pop)
    _, t_builtin_desc = time_sort(python_builtin_sort, cities, key=pop, reverse=True)

    print(f"\nSort time comparison ({len(cities)} cities):")
    print(f"  {'Algorithm':<28} {'Asc':>10}  {'Desc':>10}")
    print(f"  {'-'*28} {'-'*10}  {'-'*10}")
    print(f"  {'Selection sort':<28} {t_asc*1e6:>9.1f}µs  {t_desc*1e6:>9.1f}µs")
    print(f"  {'Python built-in (Timsort)':<28} {t_builtin_asc*1e6:>9.1f}µs  {t_builtin_desc*1e6:>9.1f}µs")

    # =========================================
    # PART 2: Array vs Linked List
    # =========================================
    print("\n" + "=" * 52)
    print("PART 2: Array vs Linked List")
    print("=" * 52)

    # --- Array (Python list) operations ---
    print("\n[ Array (Python list) ]")

    city_array = list(cities)   # working copy

    # O(1) index access
    start = time.perf_counter()
    tenth = city_array[9]
    t_access = time.perf_counter() - start
    print(f"  Access city[9]  → {tenth['name']} ({tenth['population']:,})  "
          f"[O(1), {t_access*1e9:.1f} ns]")

    # O(n) insert at beginning — Python must shift every element right
    new_city = {"name": "Waco", "population": 143000}
    start = time.perf_counter()
    city_array.insert(0, new_city)
    t_insert = time.perf_counter() - start
    print(f"  Insert '{new_city['name']}' at index 0  "
          f"[O(n), {t_insert*1e6:.3f} µs, shifted {len(city_array)-1} elements]")

    # --- Linked List operations ---
    print("\n[ Linked List ]")

    ll = LinkedList()
    for city in cities:
        ll.insert_at_tail(city)         # build list in original order
    print(f"  Built linked list with {len(ll)} nodes (insert_at_tail × {len(ll)})")

    # O(1) insert at head
    start = time.perf_counter()
    ll.insert_at_head(new_city)
    t_head = time.perf_counter() - start
    print(f"  Insert '{new_city['name']}' at head  "
          f"[O(1), {t_head*1e9:.1f} ns, no shifting needed]")

    # O(n) search
    target = "Lubbock"
    start = time.perf_counter()
    node = ll.search(target, key=lambda c: c['name'])
    t_search = time.perf_counter() - start
    if node:
        print(f"  Search '{target}'  → found: {node.data['name']} "
              f"({node.data['population']:,})  [O(n), {t_search*1e6:.3f} µs]")
    else:
        print(f"  Search '{target}'  → not found  [O(n), {t_search*1e6:.3f} µs]")

    # =========================================
    # PART 3: Big O Comparison
    # =========================================
    print("\n" + "=" * 52)
    print("PART 3: Big O Summary")
    print("=" * 52)

    print("""
  Sorting Algorithms
  ┌──────────────────────────┬────────────┬────────────┐
  │ Algorithm                │  Average   │  Worst     │
  ├──────────────────────────┼────────────┼────────────┤
  │ Selection Sort           │  O(n²)     │  O(n²)     │
  │ Python Timsort (built-in)│  O(n log n)│  O(n log n)│
  └──────────────────────────┴────────────┴────────────┘

  Array vs Linked List
  ┌──────────────────────────┬────────────┬────────────┐
  │ Operation                │  Array     │ Linked List│
  ├──────────────────────────┼────────────┼────────────┤
  │ Access by index          │  O(1)  ✓   │  O(n)      │
  │ Insert at beginning      │  O(n)      │  O(1)  ✓   │
  │ Insert at end            │  O(1)*     │  O(n)      │
  │ Search (unsorted)        │  O(n)      │  O(n)      │
  │ Delete at head           │  O(n)      │  O(1)  ✓   │
  └──────────────────────────┴────────────┴────────────┘
  * Amortized O(1) — Python lists over-allocate to avoid
    frequent resizing.
""")

    print("Thank you for using the City Data Lab.")


if __name__ == "__main__":
    main()
