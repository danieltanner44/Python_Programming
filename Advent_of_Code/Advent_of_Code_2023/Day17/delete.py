import numpy as np
from heapq import heappush, heappop

def dijkstra(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    distances = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
    distances[start] = matrix[start[0]][start[1]]
    predecessors = {}
    queue = [(distances[start], start)]

    while queue:
        current_distance, current_node = heappop(queue)

        if current_node == end:
            return distances[end], predecessors

        visited.add(current_node)

        for neighbor in neighbors(current_node, rows, cols):
            if neighbor not in visited:
                distance = current_distance + matrix[neighbor[0]][neighbor[1]]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heappush(queue, (distance, neighbor))

    return float('inf'), None

def neighbors(node, rows, cols):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    result = []
    for dx, dy in directions:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < rows and 0 <= y < cols:
            result.append((x, y))
    return result

def reconstruct_path(predecessors, start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.append(start)
    path.reverse()
    return path

matrix = np.array([[2, 4, 1, 3, 4, 3, 2, 3, 1, 1, 3, 2, 3],
                   [3, 2, 1, 5, 4, 5, 3, 5, 3, 5, 6, 2, 3],
                   [3, 2, 5, 5, 2, 4, 5, 6, 5, 4, 2, 5, 4],
                   [3, 4, 4, 6, 5, 8, 5, 8, 4, 5, 4, 5, 2],
                   [4, 5, 4, 6, 6, 5, 7, 8, 6, 7, 5, 3, 6],
                   [1, 4, 3, 8, 5, 9, 8, 7, 9, 8, 4, 5, 4],
                   [4, 4, 5, 7, 8, 7, 6, 9, 8, 7, 7, 6, 6],
                   [3, 6, 3, 7, 8, 7, 7, 9, 7, 9, 6, 5, 3],
                   [4, 6, 5, 4, 9, 6, 7, 9, 8, 6, 8, 8, 7],
                   [4, 5, 6, 4, 6, 7, 9, 9, 8, 6, 4, 5, 3],
                   [1, 2, 2, 4, 6, 8, 6, 8, 6, 5, 5, 6, 3],
                   [2, 5, 4, 6, 5, 4, 8, 8, 8, 7, 7, 3, 5],
                   [4, 3, 2, 2, 6, 7, 4, 6, 5, 5, 5, 3, 3]])

start = (0, 0)
end = (12, 12)

shortest_path_length, predecessors = dijkstra(matrix, start, end)
if predecessors is not None:
    shortest_path = reconstruct_path(predecessors, start, end)
    print("Shortest path length:", shortest_path_length)
    print("Shortest path:", shortest_path)
else:
    print("No path found from start to end.")
