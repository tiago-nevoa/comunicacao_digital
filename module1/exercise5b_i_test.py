from exercise5b_i import interleaving

print(interleaving(4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

## -> [[1, 9, 2, 10], [0, 3, 0, 4], [5, 0, 6, 0], [0, 7, 0, 8]]

# This returns a 4x4 matrix with the input data [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] interleaved. The function interleaves all the input data up to the maximum capacity of the matrix. In this case, the matrix can hold a maximum of 16 elements, so the function interleaves the first 10 items of the input data and leaves the remaining 6 elements as 0.