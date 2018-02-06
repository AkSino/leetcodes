from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self,node,visited):
        stack=[node]

        while stack:
            elem=stack.pop()
            print(elem)
            visited[elem]=True
            for each in self.graph[elem]:
                if each not in visited:
                    stack.append(each)
var=Graph()
var.addEdge(1,2)
var.addEdge(1,3)
var.addEdge(2,4)
var.addEdge(3,5)
var.addEdge(5,6)
var.addEdge(6,7)

var.bfs(7,{})