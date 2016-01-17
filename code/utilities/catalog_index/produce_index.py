##
#
# Author: Vincent Steffens
# Email:  vincesteffens@gmail.com
# 
# Goal: 
#  The purpose of this program is to produce a list of lines
# of the form:
# <text> = <number>
# 
# where <text> is a column label and <number is a column 
# number. These are to be written to an output file and used 
# later in other code for ease-of-use in coding and labeling 
# output. 
#
##

import os
import sys
import re

#program name, inputfile, outputfile
if len(sys.argv) != 3:
  print "Usage: $ python program_name.py inputfile outputfile"
  exit()

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

if not os.path.isfile(inputfilename):
  print "Error: " + inputfilename + " is not a file!"
  exit()

if os.path.isfile(outputfilename):
  print "Error: " + outputfilename + " exists!"

#read first line and store items in list
with open(inputfilename) as file:
  first_line = file.readline().rstrip()[1:].split(' ')

labels = []
for item in first_line:
  labels.append(re.sub(r"\(\d+\)", r"", item))

list_string = 'labels = ['
#do all but the last to avoid a trailing comma
for i in xrange(0, len(labels) - 1):
  list_string = list_string + '\'' + labels[i] + '\', '
#add the last one and close
list_string = list_string + '\'' + labels[-1] + '\']'

with open(outputfilename, 'w') as out:
  out.write(list_string)
