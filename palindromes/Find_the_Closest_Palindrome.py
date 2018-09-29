class Solution:
    def nearestPalindromic(self, n):
        if (len(n) <= 1):
            return str(int(n)-1)
        if(int(n)<15):
            return "9"
        else:
            if (len(n) % 2 == 0):
                x = n[0:(len(n) // 2)]
                x1 = str(int(n[0:(len(n) // 2)]) - 1) + str(int(n[0:(len(n) // 2)]) - 1 )[::-1]
                x2 = str(int(n[0:(len(n) // 2)])) + str(int(n[0:(len(n) // 2)]))[::-1]
                x3 = str(int(n[0:(len(n) // 2)]) + 1) + str(int(n[0:(len(n) // 2)]) + 1)[::-1]
                min=1000000000000000
                if(abs(int(n) - int(x1)) < min):
                    min=int(n) - int(x1)
                    result=x1
                if(abs(int(n) - int(x2)) < min and x2 != n):
                    min=int(n) - int(x2)
                    result=x2
                if(abs(int(n) - int(x3)) < min):
                    min=int(n) - int(x3)
                    result=x3
                return result
            else:
                x = n[0:(len(n) // 2) + 1]
                x1 = n[0:(len(n) // 2)] + str(int(n[0:(len(n) // 2) + 1]) - 1)[::-1]
                x2 = n[0:(len(n) // 2)] + str(int(n[0:(len(n) // 2) + 1]))[::-1]
                x3 = n[0:(len(n) // 2)] + str(int(n[0:(len(n) // 2) + 1]) + 1)[::-1]
                min=1000000000000000
                if(abs(int(n) - int(x1)) < min):
                    min=int(n) - int(x1)
                    result=x1
                if(abs(int(n) - int(x2)) < min and x2 != n):
                    min=int(n) - int(x2)
                    result=x2
                if(abs(int(n) - int(x3)) < min):
                    min=int(n) - int(x3)
                    result=x3
                return result


var=Solution()
print(var.nearestPalindromic("100"))
