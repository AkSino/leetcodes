from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def findWeight(self,node,visited):
        visited[node]=True
        net_weighht=0
        for each in self.graph[node]:
            if each not in visited:
                net_weighht+=each
                net_weighht+=self.findWeight(each,visited)
        return net_weighht


var=Graph()
var.addEdge(1,2)
var.addEdge(2,3)
var.addEdge(3,6)
var.addEdge(2,8)
var.addEdge(1,8)
print(var.findWeight(2,{}))