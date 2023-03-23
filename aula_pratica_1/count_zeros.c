count_zeros( int val )
{
	int count = 0;

	while (val!=0)
	{
		count += (val & 1) == 0;
		val >>= 1;
	}

	return (count);
}
