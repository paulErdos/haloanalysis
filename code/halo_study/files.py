#for handling files
import os

#for handling parameters
import sys

#so we can iterate over both files at once using izip
import itertools

filename1 = sys.argv[1]
filename2 = sys.argv[2]

if os.path.isfile(filename1) and os.path.isfile(filename2):
  with open(filename1) as file1:
    with open(filename2) as file2:
      for thing1, thing2 in itertools.izip(file1, file2):
        print thing1, thing2
