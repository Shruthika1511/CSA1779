print("VACUUM CLEANER PROBLEM")
print("B.SHRUTHIKA-192110238")
def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()
def clean(grid, x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 'D':
        grid[x][y] = 'C'
        return True
    return False
def vacuum_cleaner(grid):
    print("Initial grid:")
    print_grid(grid)
    total_cleaned = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if clean(grid, i, j):
                total_cleaned += 1
                print(f"Cleaned cell at ({i}, {j})")
                print_grid(grid)
    print(f"Total cells cleaned: {total_cleaned}")
    print("Final grid:")
    print_grid(grid)
input_grid = [
    ['D', 'C', 'D', 'C'],
    ['C', 'D', 'C', 'D'],
    ['D', 'D', 'C', 'C'],
]

vacuum_cleaner(input_grid)
