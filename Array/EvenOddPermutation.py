# Given a number n, print all the permutations of all the numbers till n such that permutations should be of form even odd even odd // odd even odd even

def evenOddPermutation(n):
    array = [i for i in range(1, n + 1)]
    ans=[]
    helperFunction(array, 0, ans)
    return ans


def helperFunction(array, start, ans):
    if (start == len(array)-1):
        ans.append(list(array))

    for i in range(start, len(array)):
        array[start], array[i] = array[i], array[start]

        helperFunction(array, start + 1, ans)
        array[start], array[i] = array[i], array[start]

print(sorted(evenOddPermutation(4)))
