import math
import matplotlib.pyplot


def createCircle(x1,y1,rad):
    #(x-x1)^2+(y-y1)^2=r^2
    array=[]
    array1=[]
    for x in range(x1-rad,x1+rad+1):
        y1=math.ceil(x1+math.sqrt(rad**2-(x-x1)**2))
        y2=math.ceil(x1-math.sqrt(rad**2-(x-x1)**2))
        array.append(x)
        array1.append(y1)
        array.append(x)
        array1.append(y2)

    print(array)
    matplotlib.pyplot.interactive(False)
    matplotlib.pyplot(array,array1)

createCircle(10,10,10)


