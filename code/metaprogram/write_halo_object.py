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
 
  #get filename
  filename = sys.argv[len(sys.argv) - 1]

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

  #3. Split first block on whitespace
  labels = re.split(' ', first_block)

  #4. Return blocks
  return [labels, second_block]

def min(a, b):
  if a > b: 
    return b
  else:
    return a

#so we have each block
[block1, block2] = read()

for thing in block1:
  print thing
