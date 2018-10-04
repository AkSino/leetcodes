import fileinput
from sys import stderr
f = fileinput.input()
def input():
    return f.readline()

testCase=input()
literal = []

for i in range(int(testCase)):
    houses=input()
    ranges=input().strip().split(" ")
    cities=int(input())
    a=[]
    finalAns=[]
    for i in range(cities):
        a.append(int(input()))

    start=[]
    end=[]
    for i in range(len(ranges)):
        if(i%2==0):
            start.append(int(ranges[i]))
        else:
            end.append(int(ranges[i]))

    for each in a:
        count=0
        for i in range(len(start)):
            if(each>=start[i] and each<=end[i]):
                count+=1
        finalAns.append(count)
    literal.append(finalAns)
    skip=input()


for i in range(1, int(testCase)+1):
    print("Case #" + str(i) + ":", end="")
    for each in literal[i-1]:
        print(" " + str(each), end="")
    print()

