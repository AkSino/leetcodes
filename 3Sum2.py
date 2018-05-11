class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            first = nums[i]
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if first + nums[left] + nums[right] == 0:
                    ans.append([first, nums[left], nums[right]])
                    while left  < right:
                        if nums[left + 1] == nums[left]:
                            left += 1
                            continue
                        else:
                            left += 1
                            break
                elif first + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ans


var = Solution()
print(var.threeSum([0, 0, 0, 0]))