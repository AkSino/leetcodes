from collections import defaultdict

class Solution(object):
    def buddyStrings(self, A, B):
        if(len(A)!=len(B)):
            return False

        hash=defaultdict(int)
        g=False
        arr=[]
        for i in range(len(A)):
            hash[A[i]]+=1
            if(hash[A[i]]==2):
                g=True
            if(A[i]!=B[i]):
                arr.append(i)

        if(len(arr)>2 or len(arr)==1):
            return False


        if(len(arr)==0):
            return g
        a=arr[0]
        b=arr[1]

        if(A[a]==B[b] and A[b]==B[a]):
            return True
        else:
            return False



var=Solution()

print(var.buddyStrings("ab", "ca"))