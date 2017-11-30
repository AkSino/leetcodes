#https://leetcode.com/problems/interleaving-string/description/

def findResult(string1,string2,string3):
    if (len(string1)==0 and string2==string3) or (len(string2)==0 and string1==string3):
        return True
    elif (len(string1)==0) or (len(string2)==0):
        return False
    else:
        if string1[0]==string3[0] and findResult(string1[1:len(string1)],string2,string3[1:len(string3)]):
            res1=True
        else:
            res1=False
        if string2[0] == string3[0] and findResult(string1, string2[1:len(string2)], string3[1:len(string3)]):
            res2=True
        else:
            res2=False
        if res1 or res2:
            return True
        else:
            return False

print(findResult("aabcc","dbbca","aadbbbaccc"))