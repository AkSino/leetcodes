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
        to_return=-9999999
        for each in self.graph[node]:
            net_weighht=0
            if each not in visited:
                net_weighht+=self.findWeight2(each,visited)
                to_return = max(net_weighht, to_return)
        return to_return
    def findWeight2(self,node,visited):
        visited[node]=True
        result=node
        for each in self.graph[node]:
            if each not in visited:
                result+=self.findWeight2(each,visited)
        return result



var=Graph()
var.addEdge(1,2)
var.addEdge(2,3)
var.addEdge(3,6)
var.addEdge(2,8)
print(var.findWeight(2,{}))