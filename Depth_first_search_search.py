def dfs(graph,vertex,search,visited):
    visited.append(vertex)

    for item in graph[vertex]:
        if item==search:
            return True
        else:
            if item not  in visited and item in graph:
                return  dfs(graph,item,search,visited)
    return False

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: [],
                    8: [3,12]}

print(dfs(adjacency_matrix,8,1,[]))