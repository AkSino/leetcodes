import math

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

def findDistance(p1,p2):
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def squarePoints(p1,p2,p3,p4):
    p1p2=findDistance(p1,p2)
    p1p3=findDistance(p1,p3)
    p1p4=findDistance(p1,p4)

    if p1p2==p1p3:
        if round(p1p4,6)==round(math.sqrt(2)*p1p2,6):
            return True
    elif p1p2==p1p4:
        if p1p3==math.sqrt(2)*p1p2:
            return True
    elif p1p3==p1p4:
        if p1p2==math.sqrt(2)*p1p3:
            return True
    else:
        return False

p1=Point(1,2)
p2=Point(4,2)
p3=Point(1,5)
p4=Point(4,5)

print(squarePoints(p1,p2,p3,p4))
