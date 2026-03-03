# Day 45 - Graph Traversal (BFS & DFS)

from collections import deque

# Graph as adjacency list
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}


# 1️⃣ BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# 2️⃣ DFS (Recursive)
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# -------- Testing --------

print("BFS:")
bfs(graph, 2)

print("\nDFS:")
dfs(graph, 2, set())
