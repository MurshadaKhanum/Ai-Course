graph = {}
n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = input(f"Neighbors of {node} (space separated): ").split()


def dfs(start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            stack.extend(reversed(graph[node]))

start = input("Start node: ")
dfs(start)