##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
# Goal: 
#  This is a subtask of a supertask. The supertask is to 
#  write a program that prints a python file with an object 
#  describing halos in terms of their properties described 
#  in various data files, e.g., Peter Behroozi's halo catalog 
#  and Miguel Aragon-Calvo's web data. 
#  The program produced by the supertask is intended to be 
#  arbitrarily-extensible as new data occurs in various 
#  formats. 
# 
#  Background:
#    The halo catalog is led by a block of lines each 
#  preceeded by a hash ('#'), this block hereafter being
#  referred to as the 'header region'.
# 
#    Beyond this lies a block of lines not preceeded by hash 
#  marks. Each of these lines contains data uniquely associated
#  with a specific halo. These data are stored as numbers and 
#  are separated by whitespace. Hereafter, this latter region
#  shall be referred to as the 'data region'. 
#
#    The header region contains two subregions: its first line,
#  and the rest of the region. This first line contains a 
#  whitespace-separated list of:
#  
#  Example:
#    name_of_quantifiable_thing(column_number)
#
#  These contain a few reserved characters, and so are merely
#  almost-usable as a set of variable names. By mapping 
#  unfavorable substrings to ones bereft of reserved 
#  characters, we can form from this first line a set of 
#  variable names. 
# 
#    The header region's latter component, that is, all 
#  beyond the first line, contains a null-subregion that I've
#  thrown out for the time being (containing parameters 
#  common to [i think] the entire simulation. I'll re-add 
#  them and deal with them later. 
#
#    The rest of the lines in the header region contain 
#  short, single-line descriptions of the 
#  name_of_quantifiable_things. There exists a rough  
#  line_number-column_number correspondence. This, however, 
#  is merely rough, with, e.g., one line containing a 
#  description of multiple similarly-formatted variables.
#
#  Purpose of this program:
#    To produce a utilitily useful for fixing the line-by-line
#  correspondence issue between the items in the first line
#  of the header region and the comments in the latter section,
#  and also to automatically handle remapping of reserved 
#  characters. Automatically? By-interface? By-interface is 
#  probably more safe in general, but costs more time, 
#  whereas automatic is vulnerable to overlooking problems but 
#  saves time. I guess it would be best to implement both. 
#  As a tool-designer, how can you know how useful a tool is 
#  before you use it?
#
## 

#so regular expressions
import re

#we also need os for handling files
import os

#we need to manipulate command-line arguments 
import sys

#so we want to read in the catalog file
#as what
#as a list of strings, one for each line
def read():

  #so we make an array to hold the lines
  lines = []
  
  #and try to open the file for reading
  filename = sys.argv[len(sys.argv) -1]

  #now we use os to handle opening the file
  if os.path.isfile(filename):
   
    #with makes sure the responsibilities of what follows
    #are handled even if it fails, e.g., closing the file. 
    #open returns a file object 
    with open(filename) as f:

      #so now we'll read all the lines and remember them
      for line in f:
        lines.append(line)

  #prepare for return
  #also learn how to do this better
  returnlist = []
  returnlist.append(lines[0])
  returnlist.append(lines[1:-1])

  return returnlist

list_of_header_sections = read()

qualities = list_of_header_sections[0]
print qualities




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
