#include <stdio.h>

int count_ones( int val );
void print_bits( int val );
int count_zeros( int val );
char most_frequent_symbol(char *file_name);

int main (void)
{
	int value = 12345;

	print_bits(value);
	printf("We have %dx 1's \n",count_ones(value));
	printf("We have %dx 0's \n",count_zeros(value));
    printf("The most frequent symbol in the file is '%c'\n", most_frequent_symbol("ListaPalavrasEN.txt"));

	return (0);
}
