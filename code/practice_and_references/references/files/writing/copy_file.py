import os

import sys

import itertools

#check for proper usage
if len(sys.argv) != 3:
  print "Usage: $ python copy_file.py infilename outfilename"
  exit()

filename1 = sys.argv[1]
filename2 = sys.argv[2]

#check to see if file exists already
if os.path.isfile(filename2):
  print "Error: outputfilename \'", filename2, "' exists!"

file1lines = []
if os.path.isfile(filename1):
  with open(filename1) as file1:
   for line in file1:
     file1lines.append(line)

with open(filename2, 'w') as file2:
  for line in file1lines:
    file2.write(line) 
