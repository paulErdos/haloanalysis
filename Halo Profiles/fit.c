#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

#define MAX_BINS 50
#define NUM_HALOS 100 //7152277
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

//We only care about rho and rs right now. Gamma is 2.
void compute_error_volume(double rho_start, double rho_stop, double rho_step, 
			  double rs_start, double rs_stop, double rs_step,
			  double gamma, Halo * h) {
	int i;	
	double rhodist = rho_stop - rho_start;
	double rsdist = rs_stop - rs_start;
//	double gdist = g_stop - g_start;

	

	//check if the range we're looking across fits into an integral
	//number of steps, and adjust as necessary
	double remainder;
	if(rho_step > 1) {	
		//check rho
		remainder = non_integer_modulus(rhodist, rho_step);
		if(remainder != 0) rhodist += (rho_step - remainder);
	}
	if(rs_step > 1) {
	//check rs
		remainder = non_integer_modulus(rsdist, rs_step);
		if(remainder != 0) rsdist += (rs_step - remainder);
	}
	//check gamma
//	remainder = non_integer_modulus(gdist, g_step);
//	if(remainder != 0) gdist += (g_step - remainder);
	//now the range fits into an integer number of steps

	
	//so now we declare the volume
	int rhosteps = rhodist / rho_step;
	int rssteps = rsdist / rs_step;
// 	int gsteps = gdist / g_step;

	
	//allocate memory for this giant thing
	//first the rows
	double ** errvol;
	if((errvol = malloc(sizeof(double) * rhosteps)) == NULL) 
		die("Unable to allocate memory for error surface / volume.\n");		
	//then the columns
	for(i = 0; i < rhosteps; i++) 
		if((errvol[i] = malloc(sizeof(double) * rssteps)) == NULL)
			die("Unable to allocate memory for error surface / volume.\n");		
	
	//we'll also need to know the degrees of freedom later
	double dof = 0;
	if(rho_step != 0) dof++;
	if(rs_step != 0) dof++;
//	if(g_step != 0) dof++;
	
	//now we need to scan across the ranges and check NFW against
	//the actual density, take the square of the residual, and
	//keep track of the sum of residuals until we get to the end.
	//then handle dof and return.
	//and then fill it with chi squares
	
	double activitymarker = 0;
	double rh, rs, r, residual, chi_sq;
	//scan across rho range
	for(rh = rho_start; rh < (rho_start + rhodist); rh += rho_step) {
	  //scan across rs range
	  printf("\r%f %% complete! Steps taken: %.0f", 100*activitymarker/rhosteps, activitymarker);
	  activitymarker++;
	  for(rs = rs_start; rs < (rs_start + rsdist); rs += rs_step) {
	    //scan across gamma range
//	    for(g = g_start; g < (g_start + gdist); g += g_step) {
	      //Now for these values of rho, rs, and gamma, we can find
	      //the nfw profile.
	      //From this, we compute chi sq between the actual and the 
	      //expected, then store the result in the error volume
	      chi_sq = 0;
	      for(i = 0; i < h->nb; i++) {
		//find average radius in current bin
		r = (h->edges[i] + h->edges[i + 1]) / 2;
		//compute the residual
		residual = h->profile[i] - nfw(rh, rs, gamma, r);
		
		//square it
		residual = pow(residual, 2);
		//and throw it on the pile
		chi_sq += residual;
	      }
              //now we scale the chi squared value by degrees of freedom
	      //minus one
	      chi_sq *= (dof - 1);
	      //and store it in the error volume
	      //so we convert coords to ints
	      int rhcoord = (rh - rho_start) / rho_step;
	      int rscoord = (rs - rs_start) / rs_step;
	      errvol[rhcoord][rscoord] = chi_sq;
	  }
	
	}

	//Now that we havethe error volume we want to find the 
	//coordinates of the min. 
	// just want the coordinates of the mininmum vaule.
	int j; double min = errvol[0][0];
	int rhocoord, rscoord;
	for(i = 0; i < rhosteps; i++) {
		for(j = 0; j < rssteps; j++) {
			if(errvol[i][j] < min && errvol[i][j] != 0) {
				min = errvol[i][j];
				rhocoord = i;
				rscoord = j;
			}
		}
	}

	double best_rho = rho_start + rhocoord * rho_step;
	double best_rs = rs_start + rscoord * rs_step;
	
	printf("Bam. Done.\n");
	printf("nbins: %d\n", h->nb);	
	printf("best chi squared: %f\n", min);
	printf("best rho: %f\nbest_rs: %f\n\n",best_rho, best_rs);
	printf("Actual\tExpected\n");
	for(i = 0; i < h->nb; i++) {
		//find average radius in current bin
		r = (h->edges[i] + h->edges[i + 1]) / 2;
		//compute the residual
		printf("%f\t%f\n", h->profile[i], nfw(best_rho, best_rs, gamma, r));
	} printf("\n\n");

	//now print it to make sure this works at all
	//we'll go horiz axis is rs
/*
	for(i = 0; i < rhosteps; i++) {
		//print out a line of rho
//		printf("rho = %.0f\t: ", i * rho_step + rho_start);
		for(j = 0; j < rssteps; j++) {
			printf("%14.7f ", errvol[i][j]);
		} printf("\n");
	}
*/
}

int main(int argc, char ** argv) 
{
	static Halo halos[NUM_HALOS];
	FILE * f = NULL;

	f = init(argc, argv);
	create_halos(f, halos);

	//test that halo is formed correctly
	int i;
	for(i = 0; i < halos[8].nb; i++)
		printf("density: %f, radius: %f\n", halos[8].profile[i], halos[8].radii[i]);

//	int i;
//	for(i = 0; i < NUM_HALOS; i++){
//		if(halos[i].nb < 30) continue;
//		compute_error_volume(500, 5000, 1, 10000, 20000, 1, 750, &halos[8]);
//	}

	fclose(f);
	return 0;
}
