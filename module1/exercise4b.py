
# (b) Realize a cifra do ficheiro alice29.txt (texto em claro) com a chave constante e com chave correspondendo a uma
# sequência aleatória de caracteres. Para ambas as situações determine os histogramas e entropias do texto em claro e do
# texto cifrado. Compare os resultados e comente.

def cypher_file(input_file_name, output_file_name, key):
    with open(input_file_name, 'rb') as input_file, open(output_file_name, 'wb') as output_file:
        while True:
            # read a block of bytes from the input file
            byte_block = input_file.read(len(key))
            # check if the end of the file is reached
            if not byte_block:
                break
            cypher_block = bytes(
                # perform XOR operation with the corresponding key value
                [b ^ k for b, k in zip(byte_block, key)])
            # write the result to the output file
            output_file.write(cypher_block)
