
maximum=0
def findLargest(string):
    global maximum
    if len(string)<=1:
        return True
    else:
        if string[0]==string[len(string)-1] and findLargest(string[1:len(string)-1]):
            maximum=max(maximum,len(string))
        else:
            (findLargest(string[0:len(string)-1]) or findLargest(string[1:len(string)]))
    return maximum
print(findLargest("VAPNAMANQAV"))
