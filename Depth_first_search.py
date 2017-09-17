
distances = {
    'B': {'A':12,'C':12},
    'A': {'E':32,'F':232},
    'D': {'B': 15},
    'C': {'D': 15},
    'E': {},
    'F': {}
}
starting_node='A'
visited_nodes=[]
def depth_first_search(distances,starting_node):
    for current_node in distances[starting_node]:
        if current_node in visited_nodes:
            break
        visited_nodes.append(current_node)
        depth_first_search(distances,current_node)
    return visited_nodes

print(depth_first_search(distances,starting_node))
