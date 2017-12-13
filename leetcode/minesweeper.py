def Minesweeper(matrix,click):
    directions=((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
    height=len(matrix)
    breadth=len(matrix[1])
    x=click[0]
    y=click[1]

    