#For finding the minimum height tree, firstly create dictionaries(order) which store the neighbours of the nodes.
# Also, create an array which store the number of neighbours of all the nodes. Now, its time to find the leaves of graph,
# by finding all the nodes with neighbour==1. Now we will start removing them one by one, also, we will keep decreasing the neighbours
# order value by one because we are removing the nodes. After this, after all the leaves are removed from current iteration,
# we will move on to next itearation of finding the leaves. This way we will keep going on unless we are left with two or
# less nodes in the graph. These will be the answer.


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        degree = {k:0 for k in range(n)}
        graph = {k:set([]) for k in range(n)}
        for edge in edges:
            u,v = edge[0], edge[1]
            degree[u], degree[v] = degree[u]+1, degree[v]+1
            graph[u].add(v)
            graph[v].add(u)
        leaves = [k for k,v in degree.items() if v == 1]
        while leaves and len(graph) > 2:
            for leaf in leaves:
                v = graph[leaf].pop()
                del graph[leaf]
                del degree[leaf]
                degree[v] -= 1
                graph[v].remove(leaf)
            leaves = [k for k,v in degree.items() if v == 1]
        return list(graph.keys())


var=Solution()
var.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])