def interleave(data, rows, cols):

    matrix = []

    for i in range(0, len(data), cols):
        row = data[i:i + cols]
        matrix.append(row)

    interleaved_data = ''

    for col in range(cols):
        for row in range(rows):

            if col < len(matrix[row]):
                interleaved_data += matrix[row][col]

    return interleaved_data





def deinterleave(data, rows, cols):
    
    matrix = []

    for _ in range(rows):
        row = [''] * cols
        matrix.append(row)

    index = 0
    for col in range(cols):
        for row in range(rows):
            if index < len(data):
                matrix[row][col] = data[index]
                index += 1

    deinterleaved_data = ''
    for row in range(rows):
        for col in range(cols):
            deinterleaved_data += matrix[row][col]

    return deinterleaved_data