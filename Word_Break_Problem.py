#http://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/

dict=["he","ran"]

def wordBreak(string):
    if len(string)==0:
        return True
    for i in range(len(string)):
        if string[0:i+1] in dict and wordBreak(string[i+1:len(string)]):
            print(string[0:i+1])
            return True
    return False

test_string=wordBreak("heran")
print(test_string)