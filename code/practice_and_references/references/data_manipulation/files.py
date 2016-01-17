#for handling files
import os

#for handling parameters
import sys

#so we can iterate over both files at once using izip
import itertools

if len(sys.argv) != 3:
  print "Usage: $ python program.py input1 input2"
  exit()

for i in [1,2]:
  if not os.path.isfile(sys.argv[i]):
    print "Error: problem with " + sys.argv[i] + "."
    exit()
 
filename1 = sys.argv[1]
filename2 = sys.argv[2]

if os.path.isfile(filename1) and os.path.isfile(filename2):
  with open(filename1) as file1:
    with open(filename2) as file2:
      for thing1, thing2 in itertools.izip(file1, file2):
        print thing1, thing2
