print("A* ALGORITHM")
print("B.SHRUTHIKA-192110238")
import heapq
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
def astar(graph, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    while open_list:
        current_f, current_node = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            path.insert(0, start)
            return path
        for neighbor in graph[current_node]:
            tentative_g = g_score[current_node] + 1
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    return None
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2), (1, 1)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
    (1, 2): [(0, 2), (1, 1), (2, 2)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(1, 1), (2, 0), (2, 2)],
    (2, 2): [(1, 2), (2, 1)]
}
start_node = (0, 0)
goal_node = (2, 2)
path = astar(graph, start_node, goal_node)
if path:
    print("A* Path:")
    for node in path:
        print(node)
else:
    print("No path found.")
