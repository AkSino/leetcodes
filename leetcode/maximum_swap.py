#https://leetcode.com/problems/maximum-swap/description/

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        left_index = right_index = max_index = len(digits) - 1
        for i in range(len(digits)-2, -1, -1):
            c = digits[i]
            if c < digits[max_index]:
                left_index, right_index = i, max_index
            elif c > digits[max_index]:
                max_index = i
        digits[left_index], digits[right_index] = digits[right_index], digits[left_index]
        return int(''.join(digits))

var=Solution()
print(var.maximumSwap(311112))