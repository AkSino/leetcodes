def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]
    if vertex not  in graph:
        return path
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path


adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: [],
                    8: [3,12]}

print(dfs_recursive(adjacency_matrix, 8))