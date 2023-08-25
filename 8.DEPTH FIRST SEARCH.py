print("DEPTH FIRST SEARCH")
print("B.SHRUTHIKA-192110238")
def dfs(graph, node, visited, traversal_order):
    visited.add(node)
    traversal_order.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal_order)
input_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
visited_nodes = set()
traversal_result = []
dfs(input_graph, start_node, visited_nodes, traversal_result)
print(f"DFS traversal starting from node '{start_node}':")
print(" -> ".join(traversal_result))
