##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
# Goal:
#   The purpose of this program is to take the hlist header 
# region and write the definition of a Python class containing
# a variable for each halo-associated datum in the halo 
# catalogs, as well as get/set methods for each, and docstrings
# for each method.
#   The program is intended to be extensible, and is planned 
# for later development to include Dr. Miguel Aragon-Calvo's 
# cosmic web data.
#
##

#for handling files
import os

#for handling parameters with which the program is called
import sys

#to use regular expressions
import re

def print_help():
  print "Usage: python write_halo_object.py [input file]"

def read():
  """
  1. Read file
  2. Split into blocks
  3. Split first block on whitespace
  4. Return blocks
  """

  #1. Read file 
  #create someplace to remember what the file says
  lines = []
  
  #create a list to hold blocks that are themselves lists
  blocks = []

  #get filename as long as the program is called correctly
  if len(sys.argv) == 2:
    filename = sys.argv[len(sys.argv) - 1]
  else:
    print_help() 
    exit(0)

  #then as long as it's actually a file
  if os.path.isfile(filename):
    
    #with makes sure anything it's called with gets handled, 
    #like if the code crashes before the file gets closed
    with open(filename) as f:
      
      #see if we're good so far by trying to print lines
      for line in f:
        lines.append(line)

  #2. Split into blocks
  #the first block is the first line
  #but we want to trim off the leading '#'
  first_block = lines[0][1:]
  second_block = lines[1:-1]

  #3. Replace reserved characters and split first block on 
  #   whitespace and trim off trailing ')'
  first_block = re.sub('\(', '_', first_block)
  #but neglect the added newline
  labels = re.split('\) ', first_block)
 
  #3.5 Remove trailing newlines in block2
  for i in xrange(0, len(second_block)):
    second_block[i] = second_block[i].rstrip()
 
  #4. Return blocks
  return [labels, second_block]

def min(a, b):
  if a > b: 
    return b
  else:
    return a

#so we have each block
[block1, block2] = read()

#sanity check
if len(block1) != len(block2):
  print "Error: Blocks have different sizes:"
  print "Block 1 size: " + str(len(block1))
  print "Block 2 size: " + str(len(block2))
  print "Quitting!\n"
  exit()

#begin to write the class
print "class Halo:"

#now define the init function
init_head = "  def __init__(self, "

#Now we need to list all the variables. There are 76 in all.
#So we need a string to store them in
init_body = ', '.join(block1)

#rstrip it to remove the trailing newline added by join
init_body = init_body.rstrip()

#now select all but the trailing comma 
init_body = init_body[0:-1]

#now close it
init_tail = '):'

#and join them
def_init_string = init_head + init_body + init_tail

#now print and add a newline so it looks nice
print def_init_string + '\n'

#now we need to print
#'    #description'
#'    self.whatever = whatever'
#over and over again
for index in xrange(0, len(block1)):
  print "    " + block2[index]
  print "    self." + block1[index] + " = " + block1[index]
  print
