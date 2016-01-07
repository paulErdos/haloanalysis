#for handling files
import os

#for handling arguments
import sys

if len(sys.argv) != 2:
  print "Usage: python remove_header.py file"
  exit()

filename = sys.argv[-1]

if os.path.isfile(filename):
  with open(filename) as file:
    for line in file: 
      if line[0] == '#': 
        continue
      sys.stdout.write(line)
