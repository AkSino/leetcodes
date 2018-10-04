class Node():
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

def huffmanDecoder():
    root=Node(None)
    testCases=int(input())
    for z in range(testCases):
        mem=root
        t=input()
        array=t.split(",")
        key=array[0]
        value=array[1]
        ans=""

        for i in range(len(value)):
            if(value[i]=="0"):
                if(i==len(value)-1):
                    mem.left=Node(key)
                else:
                    if(not mem.left):
                        mem.left=Node(None)
                    mem=mem.left
            else:
                if(i==len(value)-1):
                    mem.right=Node(key)
                else:
                    if(not mem.right):
                        mem.right=Node(None)
                    mem=mem.right

    inputString=input()

    mem=root
    i=0
    while i<len(inputString):
        flag=True
        mem=root
        while(flag):
            if inputString[i]=="0":
                if(mem.left.val):
                    ans+=mem.left.val
                    print(ans)
                    flag=False
                    i+=1
                    break
                else:
                    mem=mem.left
                    i+=1
            else:
                if(mem.right.val):
                    ans+=mem.right.val
                    print(ans)
                    flag=False
                    i+=1
                    break
                else:
                    mem=mem.right
                    i+=1
    print(ans)

huffmanDecoder()






