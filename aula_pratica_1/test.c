#include <stdio.h>

int count_ones( int val );
void print_bits( int val );
int count_zeros( int val );

int main (void)
{
	int value = 0;

	print_bits(value);
	printf("We have %dx 0's",count_ones(value));
	printf("\n");
	printf("We have %dx 1's",count_zeros(value));
	return (0);
}
