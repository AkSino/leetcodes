#Code by Vardan Gupta

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
layer_numbers=int(len(matrix)/2)
for layer in range(0,layer_numbers):
     left,top=0+layer,0+layer
     right,bottom=len(matrix)-1-layer,len(matrix)-1-layer



     for i in range(layer,right):
         last_elem = matrix[top][left+i]
         # Move elements from left to top
         matrix[top][left + i]=matrix[bottom-i][left]
         # Move elements from bottom to left
         matrix[bottom-i][left]=matrix[bottom][right-i]
         # Move elements from right to bottom
         matrix[bottom][right - i]=matrix[top+i][right]
         # Move elements from left to right
         matrix[top + i][right]=last_elem

for layer in matrix:
    print(layer)





