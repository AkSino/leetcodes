import math



def solution(A,E):
        maximum=0
        def total_common(edg, nd, val, k):
            same_val = 0
            for j in range(int(len(edg) / 2)):
                if (k == nd[edg[(2 * j) + 1] - 1] and val == edg[2 * (j)]):
                    same_val =same_val+ 1 + total_common(edg, nd, edg[(2 * j) + 1], k)
            return same_val

        if(len(E)==0 or len(A)==0 or len(A)==0):
            return maximum

        for i in range(len(A)):
            maximum=max(total_common(E,A,i+1,A[i]),maximum)
        return maximum



print(solution([4,4,1,1,3,3,3,3,3,3],[1,2,1,3,3,4,3,5,4,8,6,7,7,9,8,10]))







