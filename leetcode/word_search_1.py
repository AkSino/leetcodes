class Solution:
    def exist(self, board, word):
        dictionary={}
        for each in board:
            for elem in each:
                if elem in dictionary:
                    dictionary[elem]+=1
                else:
                    dictionary[elem] =1

        for char in word:
            if char not in dictionary:
                return False
            else:
                dictionary[char]-=1
                if dictionary[char]<0:
                    return False
        return True

