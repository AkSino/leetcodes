
distances = {
    'B': {'A':12,'C':12},
    'A': {'E':32,'F':232},
    'D': {'B': 15},
    'C': {'D': 15},
    'E': {},
    'F': {}
}
visited_nodes=set()
starting_node='B'

def find_connection(input_graph, starting_node):
    for current_node_in_loop in distances[starting_node]:
        if current_node_in_loop in visited_nodes:
            break
        if current_node_in_loop not in visited_nodes:
            visited_nodes.add(current_node_in_loop)
            find_connection(input_graph, current_node_in_loop)
    return visited_nodes

print(find_connection(distances,'A'))

