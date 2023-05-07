#include <stdio.h>

void print_bits( int val )
{
	// int in C is 32 bits we start on the most relevant bit
	for(int i = 31; i >= 0; i--)
	{
        printf("%d", (val >> i) & 1);
    }
    printf("\n");
}
