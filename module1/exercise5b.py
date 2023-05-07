def block_interleaver(input_data, block_size):
    """
    Interleaves a block of data using a simple block interleaving technique.

    Args:
        input_data (list): a list of data to be interleaved.
        block_size (int): the size of the blocks to be interleaved.

    Returns:
        list: the interleaved data.
    """
    interleaved_data = []
    num_blocks = len(input_data) // block_size
    for i in range(block_size):
        for j in range(num_blocks):
            interleaved_data.append(input_data[j * block_size + i])
    return interleaved_data