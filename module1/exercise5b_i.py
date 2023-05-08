# dimension -> dimension of the square matrix
# data -> list of input data to be interleaved
# returns a square matrix with interleaved input data
def interleaving(dimension, data):
    if pow(dimension, 2) < len(data): return "Must provide a bigger matrix dimension"
    matrix = [[0 for i in range(dimension)] for j in range(dimension)]
    num = 0
    for i in range(dimension):
        for j in range(dimension):
            if (i + j) % 2 == 0 and num < len(data):
                matrix[i][j] = data[num]
                num += 1
    while num < len(data):
        for i in range(dimension):
            for j in range(dimension):
                if matrix[i][j] == 0 and num < len(data):
                    matrix[i][j] = data[num]
                    num += 1
    return matrix

# The interleaving technique is used to spread out or distribute a sequence of elements in a matrix or other data structure. It is commonly used in communication systems to prevent data loss due to burst errors, where several bits of data are lost in a row. By interleaving the data, the bits are spread out over multiple blocks of data, reducing the likelihood of losing all the bits in a burst error.

# The function fills the interleaved matrix with the elements in the input list in row-major order, and any remaining elements are filled in the empty cells of the matrix in the same order. This ensures that all the elements in the input list are used and the output matrix has the same number of cells as the input matrix.