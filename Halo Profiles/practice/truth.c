#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv) {
	int i;
	for(i = 0; argv[i] != '\0'; i++) 
		printf("argv[%d]: %s\n", i, argv[i]);

	if(atoi(argv[1])) 
		printf("True!\n");
	else if(!atoi(argv[1]))
		printf("False!\n");
	else
		printf("Neither!\n");
	
	return 0;
}
