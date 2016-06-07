#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include <omp.h>

#define TEST_MODE 1
#define MAX_BINS 50
#define NUM_HALOS 1000//7152277
#define PARTICLE_MASS 154966000 // Msun/h

//HaloID ParentID Mass Radius Vmax X Y Z VX VY VZ NP N_Rbins PPBin R0 .. RN
typedef struct {
	int halo_id;
	int parent_id;
	double mass;
	double radius;
	double vmax;
	double x;
	double y;
	double z;
	double vx;
	double vy;
	double vz;
	int np;
	int nb;
	int ppb;
	double edges[MAX_BINS];
	double radii[MAX_BINS];
	double profile[MAX_BINS];
	double best_rs;
	double best_rho_0;
	double best_g;
} Halo;

void die(char * message) {
	printf("Error:\n");
	printf("%s\n", message);
	exit(1);
}

double actual_density(double in_edge, double out_edge, int ppb) {
	//compute mass in shell
	//ppb * PARTICLE_MASS overflows to a negative. Why?
	double particle_mass = PARTICLE_MASS;
	double shell_mass = ppb * particle_mass;
	
	//compute shell volume
	double r0_cubed = pow(in_edge, 3.0);
	double r1_cubed = pow(out_edge, 3.0);
	double shell_volume = (4*M_PI/3)*(r1_cubed - r0_cubed);
	
	//return density
	return shell_mass / shell_volume;
}

void fill_halo(char * line, Halo * h) {
	char * p = NULL;
	int i = 0; int j = 0;
	
	//Fill array with values
	for(p = strtok(line, " "); p != NULL; p = strtok(NULL, " ")) {
		switch(i++) {
			case 0:
				h->halo_id = atoi(p);
				break;
			case 1:	//parent id
				break;
			case 2:	//parse a.aae+0x
				break;
			case 3:	//double
				h->radius = atof(p);
				break;
			case 4:	break;
			case 5:	break;
			case 6:	break;
			case 7:	break;
			case 8:	break;
			case 9:	break;
			case 10: break;	
			case 11: //np
				h->np = atoi(p);
				break;
			case 12: //nb
				h->nb = atoi(p);
				break;
			case 13: //ppb
				h->ppb = atoi(p);
				break;
			default:
				h->edges[j++] = atof(p);
		}
	}
	
	for(i = 0; i < h->nb; i++) { 
		//fill an array with the actual density profile for each 
		//bin. Here we assume spherical symmetry, although I think
		//this is inconsequential.
		h->profile[i] = actual_density(h->edges[i],
						h->edges[i + 1],
						h->ppb);

		//fill radii array with midpoints of each bin
		h->radii[i] = (h->edges[i] + h->edges[i + 1]) / 2;
	}
}

FILE * init(int argc, char ** argv) {

	if(argc != 2) 
		die("Usage: $ program_name input_file_name\n");

	FILE * f = fopen(argv[1], "r");
	if(f == NULL) 
		die("Cannot open file!\n");
	
	return f;
}

void test(Halo * halos) {
	//check that it's printing edges correctly
	int i;
	printf("\nEdges:\n");
	for(i = 0; i < halos[0].nb + 1; i++) {
		printf("%f\n", (halos[0]).edges[i]);
	}

	//check that it's printing the density profile correctly
	printf("\nDensity Profile:\n");
	int j;
	for(j = 0; j < NUM_HALOS; j++) {
		printf("halos[%d], ID: %d\n", j, (halos[j]).halo_id);
		for(i = 0; i < halos[j].nb; i++) {
			printf("%f\n", (halos[j]).profile[i]);
		}
		printf("\n");
	}
}

void create_halos(FILE * f, Halo * halos) {
	//read file, parse text, create halos
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	int i = 0;
	while((read = getline(&line, &len, f)) != -1) {
		if(line[0] != '#') {
			Halo h;
			fill_halo(line, &h);
			halos[i++] = h;
			if(i == (NUM_HALOS - 1)) break;
		}
	}
	free(line);
}

double nfw(double rho_0, double rs, double gamma, double radius) {
	double x = radius / rs;
	return 4*rho_0/(x * pow((1 + x), gamma));
}

//finds dividend % divisor by interpreting divisor as an integer
double non_integer_modulus(double dividend, double divisor) {
	while(dividend > divisor) dividend -= divisor;
	
	//sanity check
	int test = dividend;
	assert((dividend - test) == 0);

	return dividend;
}

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

//We only care about rho and rs right now. Gamma is 2.
void compute_error_volume(double g_start, double g_stop, double g_step, Halo * h) {

	int i, j, k;	
	
	//check gamma. Imagine if g_start were 0, g_step were 5, and 
        //g_stop were 17. We wouldn't get all the requested range, so 
	//we would need to adjust g_stop to 20.
	double remainder, g_dist = g_stop - g_start;
	if(g_step > 1) {
		remainder = non_integer_modulus(g_dist, g_step);
		if(remainder != 0) g_dist += (g_step - remainder);
		assert(non_integer_modulus(g_dist, g_step) == 0.0);
	}
	//now the range fits into an integer number of steps
	int gsteps = g_dist / g_step;
	int rhosteps = h->nb;
	int rssteps = h->nb;

	//so alloc a space for it 
	double *** errvol = alloc_data(rhosteps, rssteps, gsteps);
	
	//we'll need to know the degrees of freedom
	double dof = 2; // because we know we're varying rho_0 and rs
	if(g_step != 0) dof++;
	
	//now we need to scan across the ranges and check NFW against
	//the actual density, take the square of the residual, and
	//keep track of the sum of residuals until we get to the end.
	//then handle dof and return.
	//and then fill it with chi squares

	int trigger = 1;
	double best_rs, best_rho_0, best_g, smallest;
	double g, rho_0, rs, r, chi, residual;
	for(i = 0; i < h->nb; i++) { rs = h->radii[i];
	  for(j = 0; j < h->nb; j++) { rho_0 = h->profile[j];
	    for(g = g_start; g < (g_start + g_dist); g += g_step) {
	      chi = 0;
	      for(k = 0; k < h->nb; k++) { r = h->radii[k];
		//compute the residual (actual density - expected)
		residual = h->profile[i] - nfw(rho_0, rs, g, r);
		//square it
		residual = pow(residual, 2);
		//and throw it on the pile
		chi += residual;
	      }
	      //now we want to store the sum in the error volume
	      chi /= (dof - 1);
	      int g_coord = (g - g_start) / g_step;
              errvol[i][j][g_coord] = chi;

	      //we can save some computation time later by tracking the 
	      //smallest value here
	      //let's take the first value to start off with
  	      if(trigger) {
	  	  trigger = 0;
		  smallest = chi;
	      }
	      if(chi < smallest) {
	  	  smallest = chi;
		  best_rs = rs;
		  best_rho_0 = rho_0;
		  best_g = g;
	      }
	    }
  	  }
        }

	h->best_rs = best_rs;
	h->best_rho_0 = best_rho_0;
	h->best_g = best_g;
}

int main(int argc, char ** argv) 
{
	static Halo halos[NUM_HALOS];
	FILE * f = NULL;
	f = init(argc, argv);
	create_halos(f, halos);

	int i;
	#pragma omp parallel for
	for(i = 0; i < NUM_HALOS; i++) 
		compute_error_volume(0, 1000, 1, &halos[i]);

	fclose(f);

	//write

	return 0;
}
