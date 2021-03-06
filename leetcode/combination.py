def combinationSum( candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res


def dfs( nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        dfs(nums, target - nums[i], i, path + [nums[i]], res)

for each in (combinationSum([1,2,4,8,16,32],4)):
    print(each)