#https://leetcode.com/problems/string-compression/description/
class Solution(object):
    def compress(self, chars):
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left

varsi=Solution()
print(varsi.compress(["q","q","a","a","n","n","n"]))

# public int integerBreak(int n) {
# if (n == 2)
#
#
# return 1;
# else if (n == 3)
#     return 2;
# else if (n % 3 == 0)
# return (int)
# Math.pow(3, n / 3);
# else if (n % 3 == 1)
#     return 2 * 2 * (int)
#     Math.pow(3, (n - 4) / 3);
# else
#     return 2 * (int)
#     Math.pow(3, n / 3);
# }
#
# }

#https://leetcode.com/problems/integer-break/discuss/80785/O(log(n))-Time-solution-with-explanation