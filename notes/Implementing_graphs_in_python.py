def find_path(graph, start, end, path=[]):
    path = path + [start]
    #path.append(start)
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
print(find_path(graph, 'A', 'D'))