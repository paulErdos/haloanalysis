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

if len(sys.argv) != 3:
  print "Usage: $ python first_few_lines.py in.csv out.csv"

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

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
      if index == 100:
        exit()
      output.write(line)
      index = index + 1
