import numpy
import matplotlib.pyplot as pyp
import sys
import os 
import re

filesize = []
scalefactor = []

filename = sys.argv[len(sys.argv) - 1]
if os.path.isfile(filename):
  with open(filename) as f:
    line = f.readline().split(',')
    for line in f:
      line = line.split(',')
      filesize.append(line[0])
      scalefactor.append(line[1].rstrip('\n'))

print scalefactor
print filesize
 
