class Solution:
    def minimumTotal(self, triangle):
        add = 0
        return self.helperFunction(triangle, 0, 0, add)

    def helperFunction(self, triangle, i, j, add):
        if (i == len(triangle) - 1):
            return add + triangle[i][j]
        add = add + triangle[i][j]
        return min(self.helperFunction(triangle, i + 1, j, add), self.helperFunction(triangle, i + 1, j + 1, add))

x=[  [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

var=Solution()
print(var.minimumTotal(x))