inputs=[[1,2],[3,5],[6,7],[8,10],[12,16]]


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

l=4
r=9

left=[ i for i in inputs if i[1]<l]
right=[i for i in inputs if i[0]>r]

middle=[[min(l,inputs[len(left)][0]),max(r,inputs[len(inputs)-len(right)-1][1])]]

print(left+middle+right)

