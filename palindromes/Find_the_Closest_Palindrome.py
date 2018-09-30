class Solution:
    def nearestPalindromic(self, n):
        if (len(n) <= 1):
            return str(int(n)-1)
        if(int(n)<=11):
            return "9"
        if(int(n)<15):
            return "11"
        else:
            if (len(n) % 2 == 0):
                x = n[0:(len(n) // 2)]

                x1 = self.genForEven(str(int(x) - 1))
                x2 = self.genForEven(str(int(x)))
                x3 = self.genForEven(str(int(x) + 1))

                if(len(str(int(x))) > len(str(int(x) - 1))):
                    x1 = "9"*((len(n) // 2)+1)
                if (len(str(int(x))) < len(str(int(x) + 1))):
                    x3 = self.genForOdd(str(int(x) + 1))


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

                x1 = self.genForOdd(str(int(x) - 1))
                x2 = self.genForOdd(str(int(x)))
                x3 = self.genForOdd(str(int(x) + 1))

                if(len(str(int(x))) > len(str(int(x) - 1))):
                    x1 = "9"*((len(n))-1)
                if (len(str(int(x))) < len(str(int(x) + 1))):
                    p=str(int(x) + 1)
                    x3 = self.genForEven(p[:len(p)-1])
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

    def genForOdd(self, number):
        a=str(number)
        if(len(a)==1):
            return str
        return a[0:len(number)-1] + a[len(number)-1] + a[0:len(number)-1][::-1]

    def genForEven(self, number):
        a=str(number)
        return a+a[::-1]
var=Solution()
print(var.nearestPalindromic("10001"))
