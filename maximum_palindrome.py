def findPalin(string,start,end):
    if (string[start]==string[end]) and 0<=end-start<=1:
        return True
    else:
        if string[start]==string[end]:
            if findPalin(string,start+1,end-1):
                return string[start:end+1]
        if string[start]!=string[end]:
            if findPalin(string,start+1,end):
                return string[start+1:end+1]
            if findPalin(string,start,end-1):
                return string[start+1:end]
