class Solution:
    def canFinish(self, numCourses, prerequisites):
        prerequisites=self.createGraph(prerequisites)
        return  not self.findLoop(prerequisites)

    def dfs(self,graph, visited, root):
        for each in graph[root]:
            if each in visited:
                return True
            else:
                if each in graph:
                    visited[each] = True
                    if self.dfs(graph, visited, each):
                        return True

    def findLoop(self,graph):
        for each in graph:
            visited = {}
            visited[each] = True
            if self.dfs(graph, visited, each):
                return True
        return False


    def createGraph(self,prereq):
        graph={}
        for each in prereq:
            if each[0] in graph:
                graph[each[0]].append(each[1])
            else:
                graph[each[0]]=[each[1]]
        return graph



var=Solution()
print(var.canFinish(2, [[1,2],[2,3],[3,4],[5,1]]))