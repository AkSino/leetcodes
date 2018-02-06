class Solution(object):
    def helper(self, s, k):
        if len(s) < k:
            return 0
        ch = min(set(s), key=s.count)
        if s.count(ch) >= k:
            return len(s)
        return max(self.helper(t, k) for t in s.split(ch))

    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.helper(s, k)

var=Solution()
print(var.longestSubstring("aaabbb",3))