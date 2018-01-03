nodes = ('A', 'B', 'D', 'E', )
distances = {
    'B': {'E': 10, 'A':12},
    'A': {'B': 12, 'D': 3},
    'D': {'E': 15, 'A': 3},
    'E': {'D': 15, 'B': 10}}

visited={}
unvisited={}
print(unvisited)
starting='B'
curDis=0
for i in distances:
    unvisited[i]=None
for i in distances:
    visited[i]=None
unvisited[starting]=0
visited[starting]=0
while unvisited:
    for neinbours,distanceTo in distances[starting].items():

        if visited[neinbours] is None:
            visited[neinbours]=curDis+distanceTo
            unvisited[neinbours]=visited[neinbours]
        elif(visited[neinbours]>curDis+distanceTo ):
            visited[neinbours]=curDis+distanceTo
            unvisited[neinbours]=visited[neinbours]
    del unvisited[starting]
    min=10000000000000000
    min_ver=""
    for mini in unvisited:
        if unvisited[mini] is not None:
            if unvisited[mini]<min:
                min=unvisited[mini]
                min_ver=mini
    starting=min_ver
    curDis=min

print(visited)







