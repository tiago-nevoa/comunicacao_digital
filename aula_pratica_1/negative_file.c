#include <stdio.h>
#include <stdlib.h>

#define NUM_CHARS 256

void negative_file( char *input_file_name, char *output_file_name){

    FILE *fp;
    int count[NUM_CHARS] = {0};
    int max_count = 0;
    char max_char = '\0';
    int c;

    fp = fopen(input_file_name, "r");
    if (fp == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    while ((c = fgetc(fp)) != EOF) {
        if (c >= 0 && c < NUM_CHARS) {
            count[c]++;
            if (count[c] > max_count) {
                max_count = count[c];
                max_char = c;
            }
        }
    }

    fclose(fp);

	/*	Change the code to read and write with the conditions:
		a qual transforma o ficheiro de entrada input_file_name no ficheiro de saída output_file_name.
		O ficheiro de saída é produzido a partir do ficheiro de entrada através na negação de cada bit do mesmo.
	*/
}
