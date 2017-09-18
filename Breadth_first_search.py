
distances = {
    'A': {'B':12,'C':12},
    'B': {'E':32,'D':232},
    'C': {'F': 15,'G':32},
    'D': {'H': 15,'I':32},
    'E': {'J': 15,'K':32},
    'F': {'L': 15,'M':32},
    'G': {'N': 15,'O':32},
    'H': {},
    'I': {},
    'J': {},
    'K': {},
    'L': {},
    'M': {},
    'N': {},
    'O': {},
}
visited_nodes=set()
starting_node='A'
temp_set=set()

def find_connection(input_graph, starting_node):
    for current_node_in_loop in distances[starting_node]:
        if current_node_in_loop in visited_nodes:
            break
        visited_nodes.add(current_node_in_loop)
        temp_set.add(current_node_in_loop)
    for item in temp_set:
        find_connection(input_graph,item)
    temp_set.clear()
    return visited_nodes


print(find_connection(distances,starting_node))