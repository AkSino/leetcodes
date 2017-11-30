class Solution:
    def letterCombinations(number):
        dict={'1':'1',
            '0':'0',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}

        if len(number)==0:
            return []

        a=[""]
        b=[]

        for i in number:
            for j in dict[i]:
                for res in a:
                    b.append(res+j)
            a=b
            b=[]
        return a

Var=Solution
print(Var.letterCombinations("10"))
