class graphs():
    def __init__(self):
        self.graph={}
    def addEdge(self,a,b):
        if a in self.graph:
            self.graph[a].append(b)
        else:
            self.graph[a]=[b]
        if b not in self.graph:
            self.graph[b]=[]

def dfs(current,grey,black,graph):
    global white
    if current in white:
        white.remove(current)
    grey.add(current)
    for each in graph[current]:
        if each in black:
            continue
        if each in grey:
            return True
        if dfs(each,grey,black,graph):
            return True
    grey.remove(current)
    black.add(current)
    return False
def findCycle(graph):
    global white
    white=set()
    grey=set()
    black=set()

    for each in graph:
        white.add(each)

    while white:
        current=white.pop()
        if dfs(current,grey,black,graph):
            return True
    return False
var=graphs()
var.addEdge(1, 2)
var.addEdge(1, 3)
var.addEdge(2, 3)
var.addEdge(4, 1)
var.addEdge(4, 5)
var.addEdge(5, 6)
var.addEdge(6, 7)

graph=var.graph

print(findCycle(graph))
