#https://leetcode.com/problems/combination-sum-ii/description/


def FindSum(arrays,target):
    for i in arrays:
        if arrays[i]==target:
            return arrays[i]
        if arrays[i]>target:
            return False

