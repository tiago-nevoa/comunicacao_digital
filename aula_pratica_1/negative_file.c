#include <stdio.h>

void negative_file(char *input_file_name, char *output_file_name) {
    FILE *input_file = fopen(input_file_name, "rb"); // abre arquivo de entrada em modo binário
    FILE *output_file = fopen(output_file_name, "wb"); // abre arquivo de saída em modo binário

    if (input_file == NULL || output_file == NULL) {
        printf("Erro ao abrir arquivos!\n");
        return;
    }

    int byte;
    while ((byte = fgetc(input_file)) != EOF) { // lê cada byte do arquivo de entrada
        byte = ~byte; // realiza a negação de cada bit do byte
        fputc(byte, output_file); // escreve o byte negado no arquivo de saída
    }

    fclose(input_file); // fecha o arquivo de entrada
    fclose(output_file); // fecha o arquivo de saída
}
