##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
# 
#  The purpose of this program is to take a sample from the 
# unweildily-large unified catalog and write it to a file 
# for use in testing other code.
# 
# What it does:
# 1. Reads some lines (e.g., some relatively small number)
# 2. Writes those lines to a file
#
##

import os
import sys

if len(sys.argv) != 4:
  print "Usage: $ python program_name.py <# of lines> in out"
  exit()

number_of_lines = int(sys.argv[1])
inputfilename = sys.argv[2]
outputfilename = sys.argv[3]

if not os.path.isfile(inputfilename):
  print "Error: " + inputfilename + " is not a file!"
  exit()

if os.path.isfile(outputfilename):
  print "Error: " + outputfilename + " already exists!"
  exit()

#there must be a way to do this with an indexed for loop
index = 0
with open(inputfilename) as input:
  with open(outputfilename, 'w') as output:
    for line in input:
      if index == number_of_lines:
        exit()
      output.write(line)
      index = index + 1
      if index % 100 == 0: print index
