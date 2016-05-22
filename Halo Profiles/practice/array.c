#include <stdio.h>

int main(int argc, char ** argv) {
	int array[50];

	int i;
	for(i = 0; i < 10; i++){
		array[i] = i;
	}

	printf("%d\n", sizeof(array)/sizeof(array[0]));
	
	return 0;
}
