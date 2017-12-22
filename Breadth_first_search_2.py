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
    'Z':{}
}
visited={}
queue=[]
start_root="A"
visited["A"]=0
queue.insert(0,start_root)

while len(queue)!=0:
    current=queue.pop(0)
    for each in distances[current]:
        if each not  in visited:
            visited[each]=True
            queue.insert(0,each)

print(visited)