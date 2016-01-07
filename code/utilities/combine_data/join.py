#for using regex
import re 

#for handling files
import os

#for handling parameters
import sys

#so we can iterate over both files at once using izip
import itertools

#print userguide if misused
if len(sys.argv) != 4:
  print "Usage: $ python join.py left.csv right.csv out.csv"

#store the names
filenames = []
for name in sys.argv:
  filenames.append(name)

#make sure the first two arguments are files
for name in filenames[1:3]:
  if not os.path.isfile(name):
    print "Error:", name, "does not appear to be a file!"
    exit()

#make sure the given outputfilename is not a file
if os.path.isfile(filenames[-1]):
  print "Error: outputfilename \"" + filenames[-1] + "\" exists!"
  exit()

with open(filenames[1]) as left: 
  with open(filenames[2]) as right:
    with open(filenames[3], 'w') as out:
      for line_left, line_right in itertools.izip(left, right):
        l = re.split('[ ]*', line_left.rstrip())
        r = line_right.rstrip().split(',')
        out.write(','.join(l + r))

