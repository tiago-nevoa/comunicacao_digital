#include <stdio.h>

int count_ones( int val );
void print_bits( int val );
int count_zeros( int val );

int main (void)
{
	int value = 123456;

	print_bits(value);
	printf("We have %dx 0's \n",count_ones(value));
	printf("We have %dx 1's \n",count_zeros(value));
	return (0);
}
