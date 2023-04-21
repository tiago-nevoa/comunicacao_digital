#include <stdio.h>

int count_ones( int val );
void print_bits( int val );
int count_zeros( int val );
char most_frequent_symbol(char *file_name);
void negative_file(char *input_file_name, char *output_file_name);

int main (void)
{
	int value = 12345;
	char my_first_file[] = "ListaPalavrasEN.txt";
	char my_second_file[] = "ListaPalavrasPT.txt";
	char my_first_encryption[] = "ListaPalavrasENencrypted.txt";
	char my_first_decryption[] = "ListaPalavrasENdecrypted.txt";

	print_bits(value);
	printf("We have %dx 1's \n",count_ones(value));
	printf("We have %dx 0's \n",count_zeros(value));
    printf("The most frequent symbol in the file %s is '%c'\n", my_first_file, most_frequent_symbol(my_first_file));
	printf("The most frequent symbol in the file %s is '%c'\n", my_second_file, most_frequent_symbol(my_second_file));

	negative_file(my_first_file,my_first_encryption);
	negative_file(my_first_encryption,my_first_decryption);

	return (0);
}
