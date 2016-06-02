//based on http://stackoverflow.com/questions/2306172/malloc-a-3-dimensional-array-in-c
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <time.h>

void free_data(double *** data, int xlen, int ylen)
{
	size_t i, j;

	for (i = 0; i < xlen; i++) {
		if(data[i] != NULL) {
			for (j = 0; j < ylen; j++)
				free(data[i][j]);
			free(data[i]);
		}
	}
}

double *** alloc_data(size_t xlen, size_t ylen, size_t zlen) 
{
	double ***p;
	size_t i, j;

	if((p = malloc(xlen * sizeof(*p))) == NULL) {
		perror("malloc 1");
		return NULL;
	}

	for(i = 0; i < xlen; i++) 
		p[i] = NULL;

	for(i = 0; i < xlen; i++) 
		if((p[i] = malloc(ylen * sizeof(*p[i]))) == NULL) {
			perror("Malloc 2");
			free_data(p, xlen, ylen);
			return NULL;
		}

	for(i = 0; i < xlen; i++) {
		for(j = 0; j < ylen; j++) {
			p[i][j] = NULL;
		}
	}
	
	for(i = 0; i < xlen; i++) 
		for(j = 0; j < ylen; j++) 
			if((p[i][j] = malloc(zlen * sizeof(*p[i][j]))) == NULL) {
				perror("malloc 3");
				return NULL;
			}

	return p;


}

int main(int argc, char ** argv)
{
	double *** data;
	size_t xlen, ylen, zlen, i, j, k;
	xlen = 10;
	ylen = 100;
	zlen = 300;

	srand((unsigned int)time(NULL));
	if ((data = alloc_data(xlen, ylen, zlen)) == NULL)
		return EXIT_FAILURE;	

	for (i=0; i < xlen; ++i)
		for (j=0; j < ylen; ++j)
			for (k=0; k < zlen; ++k)
				data[i][j][k] = rand();

	printf("%f\n", data[1][2][1]);
	free_data(data, xlen, ylen);
	return EXIT_SUCCESS;
}	
