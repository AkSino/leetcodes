a=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

x_high=len(a)
y_high=len(a[0])
x_low=0
y_low=0

while x_low<x_high and y_low<y_high:
    for i in range(y_low,y_high):
        if x_low < x_high and y_low < y_high:
            print(a[x_low][i])
    x_low+=1
    for i in range(x_low,x_high):
        if x_low < x_high and y_low < y_high:
            print(a[i][y_high-1])
    y_high-=1
    for i in range(y_high-1,y_low-1,-1):
        if x_low < x_high and y_low < y_high:
            print(a[x_high-1][i])
    x_high-=1
    for i in range(x_high-1,x_low-1,-1):
        if x_low < x_high and y_low < y_high:
            print(a[i][y_low])
    y_low+=1


