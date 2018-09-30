from collections import defaultdict


class Solution:
    def wordSubsets(self, A, B):
        letterCount = {}
        substring = ''
        ans = []

        # The improvement that we can do in this algo is that rather than comparing the Values in each of the B, we can create a parent set of
        # all the chars that need to be required in a word. In this way lets say if we have char 'c' two times in all of the B's, we will need
        # to compare it just once with all the other patters in A.

        for string in B:
            for letter in string:
                if letter not in letterCount:
                    letterCount[letter] = 1
                else:
                    letterCount[letter] = max(letterCount[letter], string.count(letter))
                if letter not in substring:
                    substring += letter

        for word in A:
            check = 0
            for letter in substring:
                if word.count(letter) >= letterCount[letter]:
                    check += 1
            if check == len(substring):
                ans.append(word)

        return ans


var=Solution()
print(var.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))