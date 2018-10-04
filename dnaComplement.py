def dnaComplement(s):
    if (s == None):
        return None

    ans=""
    array=list(s)
    for val in reversed(array):
        ans=ans + getComplement(val)

    return ans


def getComplement(c):
    dic={
        "T": "A",
        "A": "T",
        "G": "C",
        "C":"G"
    }
    return dic.get(c, "A")

print(dnaComplement("ACCGGGTTTT"))