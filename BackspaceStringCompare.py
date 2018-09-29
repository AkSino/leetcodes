class Solution(object):
    def backspaceCompare(self, S, T):
        a = len(S) - 1
        b = len(T) - 1
        count_a=0
        count_b=0
        while (a>=0 or b>=0):

            if(a>=0 and S[a]=="#"):
                count_a+=1
                a-=1
                if(b<0 and a>=0):
                    while ((count_a>0 or S[a]=="#") and (a>=0)):
                        if(S[a]=="#"):
                            count_a+=1
                            a-=1
                        else:
                            a-=1
                else:
                    while(a >= 0 and S[a]=="#"):
                        count_a+=1
                        a-=1
                    while(count_a>0):
                        a-=1
                        count_a-=1

            if(b>=0 and T[b]=="#"):
                count_b+=1
                b-=1

                if(a<0 and b>=0):
                    while ((count_b>0 or T[b]=="#") and b>=0):
                        if(T[b]=="#"):
                            count_b+=1
                            b-=1
                        else:
                            b-=1
                else:
                    while(b >= 0 and T[b]=="#"):
                        count_b+=1
                        b-=1
                    while(count_b>0):
                        b-=1
                        count_b-=1
            if(a>=0 and b>=0):
                if(S[a]==T[b]):
                    a-=1
                    b-=1
                    continue
                else:
                    return False

        if (b < 0 and a < 0):
            return True
        elif ((a >= 0 and b < 0) or (a < 0 and b >= 0)):
            return False
        return True


var=Solution()
print(var.backspaceCompare("bxj##tw","bxo#j##tw"))

