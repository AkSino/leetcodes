

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def findCycle(graph):
    white_set=set()
    black_set=set()
    for each in graph:
        white_set.add(each)
    a=[1,2,3]
    while a:
        dfs()
def dfs(white_set,black_set):
    current=white_set.pop()
    for each in current:
        dfs()
    black_set.add(current)
findCycle(graph)
