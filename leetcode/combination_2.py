# https://leetcode.com/problems/combination-sum-ii/description/

def combinationSum2(candidates, target):
    candidates.sort()
    return dfs(candidates, 0, [], [], target)


def dfs( candidates, start, res, ans, target):
    if target < 0:
        return
    if target == 0:
        res.append(ans)
        return
    for i in range(start, len(candidates)):
        if i != start and candidates[i] == candidates[i - 1]:
            continue
        dfs(candidates, i+1, res, ans + [candidates[i]], target - candidates[i])
    return res


print(combinationSum2([1,3,6,7,1], 7))
