print("BREADTH FIRST SEARCH")
print("B.SHRUTHIKA-192110238")
from collections import defaultdict, deque
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(graph[node])
    return traversal_order
input_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
traversal_result = bfs(input_graph, start_node)
print(f"BFS traversal starting from node '{start_node}':")
print(" -> ".join(traversal_result))
