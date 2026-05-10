# ===========================================================================
# Knapsack Problem — Dynamic Programming
# ===========================================================================


# ---------------------------------------------------------------------------
# PART 1 — helper function
# ---------------------------------------------------------------------------
def calculate_total_value(solution, items):
    # TODO 1
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
    return total


# ---------------------------------------------------------------------------
# PART 2 — fill the DP grid
# ---------------------------------------------------------------------------
def knapsack(items, capacity):
    n = len(items)
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                # TODO 2 — item too heavy: copy cell directly above
                grid[i][w] = grid[i - 1][w]
            else:
                # TODO 3 — build the two candidate solution lists
                include_solution = grid[i - 1][w - weight] + [item_name]
                exclude_solution = grid[i - 1][w]

                # TODO 4 — compute each candidate's dollar value
                include_value = calculate_total_value(include_solution, items)
                exclude_value = calculate_total_value(exclude_solution, items)

                # TODO 5 — store whichever solution has the higher value
                if include_value > exclude_value:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution

    return grid


# ---------------------------------------------------------------------------
# PART 3 — pretty-print the grid
# ---------------------------------------------------------------------------
def display_grid(grid, items):
    n = len(items)
    cell_width = 12

    # TODO 6 — header row of capacity numbers, right-aligned
    header = "".join(str(w).rjust(cell_width) for w in range(1, len(grid[0])))
    print(" " * cell_width + header)

    for i in range(1, n + 1):
        # TODO 7 — start each row with item name, left-aligned
        row = items[i - 1][0].ljust(cell_width)

        for cell in grid[i][1:]:
            if cell:
                # TODO 8 — format as "$VALUE(INITIALS)", right-aligned
                val = calculate_total_value(cell, items)
                initials = "".join(name[0] for name in cell)
                row += f"${val}({initials})".rjust(cell_width)
            else:
                # TODO 9 — blank space for empty cells
                row += " " * cell_width

        print(row)


# ---------------------------------------------------------------------------
# PART 4 — run it
# ---------------------------------------------------------------------------
items = [
    ("GUITAR",   1, 1500),
    ("STEREO",   4, 3000),
    ("LAPTOP",   3, 2000),
    ("iPHONE",   1, 2000),
    ("BOOK",     2,  100),
    ("GOLD BAR", 1, 30000),
]

capacity = 6

# TODO 10 — call knapsack and store result
grid = knapsack(items, capacity)

# TODO 11 — display the grid
display_grid(grid, items)
