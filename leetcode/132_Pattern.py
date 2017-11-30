#https://leetcode.com/problems/132-pattern/description/

arr=[1, 2, 3, 4]

def Check_132(array):
    mini=100
    maxi=-100
    mid=1000
    i=0
    if len(array)<3:
        return False
    else:
        while i<len(array):
            mini=min(mini,array[i])
            