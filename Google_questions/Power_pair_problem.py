#Link is https://www.careercup.com/question?id=5736911233613824

####################################----Round4----#############################################

'''Starting from num = 0, add 2^i (where i can be any non-negative integer) to num until num == N.
Print all paths of how num turns from 0 to N.
For example if N = 4,
Paths printed are [0,1,2,3,4], [0,1,2,4], [0,1,3,4], [0,2,4], [0,2,3,4], [0,4].
[0,2,4] is made from 0 + 2^1 + 2^1. [0,1,3,4] from 0 + 2^0 + 2^1 + 2^0'''

def find_max_exp(N):
    for i in range(N):
        if 2**i <= N and 2**(i+1) > N:
            return i
paths_dict= {}

def find_paths(N):
    if N in paths_dict.keys():
        return paths_dict[N]
    if N < 0:
        return None
    if N == 0:
        return [[0]]
    max_exp = find_max_exp(N)
    all_paths = []
    for i in range(0, max_exp+1):
        paths = find_paths(N - 2**i)
        if paths == []:
            continue
        for path in paths:
            all_paths.append(path + [N])
    paths_dict[N] = all_paths
    return all_paths

print (find_paths(25))



