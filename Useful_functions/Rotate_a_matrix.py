def rotate(matrix):
    size = len(matrix)
    layer_count = size / 2

    for layer in range(0, int(layer_count)):
        first = layer
        last = size - first - 1
        print ('Layer %d: first: %d, last: %d' % (layer, first, last))

# 5x5 matrix
matrix = [
    [ 0, 1, 2, 3, 4],
    [ 5, 6, 6, 8, 9],
    [10,11,12,13,14],
    [15,16,17,18,19],
    [20,21,22,23,24]
]

rotate(matrix)