print("MAP COLORING TO IMPLEMENT CSP")
print("B.SHRUTHIKA-192110238")
def is_valid(region, color, assignment, map):
    for neighbor in map[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtrack(assignment, map, regions, colors):
    if len(assignment) == len(regions):
        return assignment
    unassigned = [region for region in regions if region not in assignment]
    region = unassigned[0]
    for color in colors:
        if is_valid(region, color, assignment, map):
            assignment[region] = color
            result = backtrack(assignment, map, regions, colors)
            if result is not None:
                return result
            assignment.pop(region)
    return None
def map_coloring(map, colors):
    regions = list(map.keys())
    assignment = {}
    solution = backtrack(assignment, map, regions, colors)
    return solution
if __name__ == "__main__":
    map = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }
    colors = ['Red', 'Green', 'Blue']
    solution = map_coloring(map, colors)
    if solution:
        print("Map Coloring Solution:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")
