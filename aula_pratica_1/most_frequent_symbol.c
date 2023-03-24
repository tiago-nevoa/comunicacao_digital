#include <stdio.h>
#include <stdlib.h>

#define NUM_CHARS 256

char most_frequent_symbol(char *file_name) {
    FILE *fp;
    int count[NUM_CHARS] = {0};
    int max_count = 0;
    char max_char = '\0';
    int c;

    fp = fopen(file_name, "r");
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

    return max_char;
}
