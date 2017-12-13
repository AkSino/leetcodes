def solution(A,E):
    graph={}
    for i in range(0,len(E),2):
        if E[i] in graph:
            graph[E[i]]=graph[E[i]]+[E[i+1]]
        else:
            graph[E[i]] = [E[i + 1]]
    print(graph)
    check(graph,A,E[0])


def check(graph,A,node):
    for each_item in graph[node]:
        if((A[node]-1)==A[each_item-1]):
            print(A[node]-1,A[each_item-1])

solution([4,4,4,4,4,4,4,4],[1,2,1,3,2,6,3,4,3,5,4,8,6,7,7,9,8,10])