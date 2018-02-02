from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)
#Firstly I append child to the list. List is stored against the parent.
    def addEdge(self,u,v):
        self.graph[u].append(v)

#Findparent recursively finds for the parent of the child from parentList list which further stores the parent of the corresponding vertice.
#If any value is -1 in parentList then it means that there is no parent of that vertex and that vertex is its own parent
    def findParent(self,parentList,element):
        if parentList[element]==-1:
            return element
        else:
            return self.findParent(parentList,parentList[element])

#Union finds for the parent of both the elements and makes one of the parent child of other.
    def doUnion(self,parentList,elem1,elem2):
        parElem1=self.findParent(parentList,elem1)
        parElem2=self.findParent(parentList,elem2)
        parentList[parElem2]=parElem1

#It uses all the above functions to find for cycle. If the algorithm below finds any two key value pairs which has same parents, then it means that there
# is a cycle in the graph.
    def findCycle(self):
        parentList=[-1]*self.vertices
        for i in self.graph:
            for j in self.graph[i]:
                par1=self.findParent(parentList,i)
                par2=self.findParent(parentList,j)
                if par1==par2:
                    return True
                parentList[j] = i

                #self.doUnion(parentList,i,j)

g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(1, 4)
g1.addEdge(2, 3)
g1.addEdge(3, 4)

#g1.addEdge(3, 0)

print(g1.findCycle())