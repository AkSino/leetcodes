class Solution():
    def acMultiply(self,big,num2):
        carry=0
        result=""
        for i in range(len(big)):
            result+=str((int(num2)*int(big[i])%10)+carry)
            carry=((int(num2)*int(big[i])%10)+carry)//10
        return result

    def assNumbers(self,num1,num2):
        carry=0
        result=""
        num1=''.join(reversed(num1))
        num2 = ''.join(reversed(num2))
        for i in range(max(len(num1),len(num2))):
            if i==len(num1):
                num1+="0"
            if i==len(num2):
                num2+="0"
            result+=str((int(num1[i])+int(num2[i])+carry)%10)
            carry=(int(num1[i])+int(num2[i])+carry)//10
        if carry!=0:
            result+=str(carry)

        return (''.join(reversed(result)))
    def multiply(self,num1,num2):
        x=len(num1)
        y=len(num2)
        if x>y:
            shNum=num2
            laNum=num1
        else:
            shNum=num1
            laNum=num2
        for i,val in enumerate(shNum):
            answer=self.acMultiply(laNum,val)+"0"*i


var=Solution()
print(var.acMultiply("23","2"))
print(var.assNumbers("99","98"))


