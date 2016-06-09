CC = cc
CFLAGS=-Wall -g -fopenmp

all: 
	$(CC) $(CFLAGS) fit.c -lm -o fit

coupled:
	$(CC) $(CFLAGS) fit_parallel_rs_rho0_coupled.c -lm -o paralell_coupled

parallel:
	$(CC) $(CFLAGS) fit_parallel.c -lm -o fit_parallel
	
serial:
	$(CC) $(CFLAGS) fit_serial.c -lm -o fit_serial

clean: 
	rm -rf fit
