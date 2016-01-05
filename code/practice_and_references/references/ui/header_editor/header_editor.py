##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
# 
# Goal:
#   The header region of the .list files contains two 
# sections of interest preceeded by '#'. 
#   The first section is a single line of whitespace-separated
# label-integer pairs, with the integer assigning the label to
# a column, columns being numbered with increasing integers
# from left to right.
#   The second section is a multiline block, each line 
# containing a description of a unique label from the previous
# section. 
#   
#  It would be convenient to read this section and produce 
# the basis for an abstract data type containing halos, with
# each quantity stored as a member variable, and with get/set
# methods written, and with the whole thing commented nicely. 
#  However, two problems exist.
#
#  The first problem is that the labels are not free of 
# reserved characters, so we can't just use them as variable
# names. 
#  The second is that some single lines in the second block 
# map to multiple labels in the first block (a surjection?).
#
#  It would be handy to have a utility that allows one to 
# scroll through the label-integer pairs in the first block 
# along with the descriptions in the second block. This would
# allow a user to spot inconsistencies and conveniently edit
# a copy of the header file.
#
## 

#so we can clear the terminal
from subprocess import call 

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

#define directional keys
up_key = ','
down_key = 'o'

#give an exit signal
exit_string = 'exit'

#we'll need an index in a moment
n = 0

#this will also be handy
length_of_smaller_list = min(len(block1), len(block2))

#let the user run as long as they need
while True:
 #-1. Clear
  call(["clear"]) 

  #0. Apply a loop constant to n
  n = n % length_of_smaller_list

  #1. Print nth list elements
  print block1[n]
  print block2[n] 

  #2. Get input
  print "\nScroll u/d with ,/o. 'exit' to exit."
  input = raw_input("Enter command and press return: ")

  #3. Respond to input
  if input == "exit":
    print "\'Bye!\n"
    call(["clear"])
    exit()
  elif input == ',':
    if n == 0:
      n = (length_of_smaller_list - 1)
    else:
      n = n - 1
  elif input == 'o':
    n = n + 1
  else:
    print 'what\n'


