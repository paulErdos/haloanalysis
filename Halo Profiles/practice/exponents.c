#include <stdio.h>
#include <math.h>

int main(int argc, char ** argv) 
{
	double e = 2.17;
	double pi = 3.14;

	double pi_to_the_e = pow(pi, e);

	printf("pi^e ~ %f\n", pi_to_the_e);

	return 1010101;
}
