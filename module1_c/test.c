#include <stdio.h>

int count_ones( int val );
void print_bits( int val );
int count_zeros( int val );
char most_frequent_symbol(char *file_name);
void negative_file(char *input_file_name, char *output_file_name);

int main (void)
{
	int value = 12345;
	char my_first_file[] = "input_files/ListaPalavrasEN.txt";
	char my_second_file[] = "input_files/ListaPalavrasPT.txt";
	char my_first_encryption[] = "output_files/ListaPalavrasENencrypted.txt";
	char my_first_decryption[] = "output_files/ListaPalavrasENdecrypted.txt";
	char my_second_encryption[] = "output_files/ListaPalavrasPTencrypted.txt";
	char my_second_decryption[] = "output_files/ListaPalavrasPTdecrypted.txt";

	print_bits(value);
	printf("We have %dx 1's \n",count_ones(value));
	printf("We have %dx 0's \n",count_zeros(value));
    printf("The most frequent symbol in the file %s is '%c'\n", my_first_file, most_frequent_symbol(my_first_file));
	printf("The most frequent symbol in the file %s is '%c'\n", my_second_file, most_frequent_symbol(my_second_file));

	negative_file(my_first_file,my_first_encryption);
	negative_file(my_first_encryption,my_first_decryption);
	negative_file(my_second_file,my_second_encryption);
	negative_file(my_second_encryption,my_second_decryption);

	return (0);
}
