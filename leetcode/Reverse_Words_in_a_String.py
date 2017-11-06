class Solution(object):
    def reverseWords(self, s):
        self.input_string = s
        input_string = self.input_string.split(" ")
        result = ""
        for i in range(len(input_string) - 1, -1, -1):
            if input_string[i] != "":
                result = result + (input_string[i] + " ")
        return (result.strip())

vardan=Solution()
print(vardan.reverseWords("a"))
