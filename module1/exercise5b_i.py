# rows -> dimension of the rows of the matrix
# cols -> dimension of the columns of the matrix
# data -> list of input data to be interleaved
# returns a square matrix with interleaved input data
def interleave(input_data, rows, cols):
    # Split input_data into rows and store them in input_matrix
    input_matrix = []
    for i in range(0, len(input_data), cols):
        row = input_data[i:i + cols]
        input_matrix.append(row)

    # Initialize output_data as an empty string
    output_data = ''

    # Iterate through the columns and rows of the input_matrix
    for col in range(cols):
        for row in range(rows):
            # Check if the current position is within the bounds of the row
            if col < len(input_matrix[row]):
                # Append the character at the current position to output_data
                output_data += input_matrix[row][col]

    # Return the interleaved output_data
    return output_data

def deinterleave(input_data, rows, cols):
    # Initialize an empty input_matrix with the given dimensions
    input_matrix = []
    for _ in range(rows):
        row = [''] * cols
        input_matrix.append(row)

    # Fill the input_matrix with the input_data
    index = 0
    for col in range(cols):
        for row in range(rows):
            if index < len(input_data):
                input_matrix[row][col] = input_data[index]
                index += 1