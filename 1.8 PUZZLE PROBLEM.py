import heapq
print("8 PUZZLE PROBLEM")

print("B.SHRUTHIKA-192110238")
class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = 0
        self.h = 0
        
    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)
def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def heuristic(state, target):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != target[i][j]:
                count += 1
    return count
def get_neighbors(state):
    neighbors = []
    blank_i, blank_j = get_blank_position(state)
    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move_i, move_j in moves:
        new_i, new_j = blank_i + move_i, blank_j + move_j
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            neighbors.append(new_state)
            
    return neighbors
def a_star(initial_state, target_state):
    open_list = []
    closed_set = set()
    
    start_node = PuzzleNode(initial_state)
    start_node.h = heuristic(initial_state, target_state)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.state == target_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        
        closed_set.add(tuple(map(tuple, current_node.state)))
        
        for neighbor_state in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor_state)) not in closed_set:
                neighbor_node = PuzzleNode(neighbor_state, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_state, target_state)
                heapq.heappush(open_list, neighbor_node)
                
    return None
def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(map(str, row)))
        
if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [0, 4, 6],
        [7, 5, 8]
    ]
    
    target_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    solution_path = a_star(initial_state, target_state)
    
    if solution_path:
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            print_puzzle(state)
            print()
    else:
        print("No solution found.")
