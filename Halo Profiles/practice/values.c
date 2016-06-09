#include <stdio.h>

void foo(double d) {	
	printf("d = %10.100f\n", d);
}

int main(int argc, char ** argv) {
	double d = 0;
	
	if(d > 0) 
		printf("double d = 0; --> actually greater than zero.\n");
	else
		printf("double d = 0; --> actually zero.\n");

	printf("d = %10.100f\n", d);

	foo(d);

	return 666;
}
