#so regular expressions
#read the file
#we'll start with the catalog
#cut it up on a regular expression
#it what?
#the first line. It contains the meanings of the numbers in each line/halo
#okay now what
#we want this program to spit out a skeleton of a big object so I don't have to retype all of this stuff
#so we'll want a get and a set for each to read and create each halo object
#i don't know how many parameters there are, and I'm too lazy to count, and there will be more
#so... dictionary?
#that might work
#then let's do something with each of these descriptions
#put them in a docstring in the get/set functions? 
#why not? Let's put them in set, and go set/get/set/get for each thing
#so, formatting
#we have an object
#that object contains a dictionary
#and then an unbounded number of get/set functions, one each for each thing in the dictionary
#so prep
#get the keys
#cut up the first line. Ignore the first #, then cut on [open paren, at least one digit, close paren, space], and append everything you get onto a list
#then take the next two lines and put them in b list
#then start with the first line that goes '#S'
#strip off the #s and append the rest of each line to c list
#i think this is everything we need
#so then build it
#build what?
#just the object? The whole file? imports?
#let's just do the object. the point is to save typing and that doesn't save anything if this happens only once. 
#so
#print the first bit of the object
#docstring? yeah, let's have it contain everything from b list
#then grab a thing from a list
#these names contain nonstring characters. 
#so, what do they contain? 
#list: ?, 'A[<single alpha character>]', 'T/|U|', *, and that's it. 
#so we'll need to replace some of these
#mmp? --> 1/0 most massive progenitor or not --> 'mmp_flag' --> notated in catalog as 1 or 0... which means which? Probably 1:yes
#A[x],A[y],A[z]: Largest shape ellipsoid axis (kpc/h comoving) 
#discovery: |alist| != |clist|
#'T/|U|': kinetic_to_magnitude_of_potential --> ratio_T_to_mag_U
#* --> 'times'