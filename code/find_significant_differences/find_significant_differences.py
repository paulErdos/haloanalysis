##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
##

import os
import sys

if len(sys.argv) != 2:
  print "Usage: $ python program_name.py in.csv"

inputfilename = sys.argv[1]

if not os.path.isfile(inputfilename):
  print "Error: " + inputfilename + " is not a file!"
  exit()

halos = []
with open(inputfilename) as file:
  for line in file:
    halos.append(line.rstrip().split(','))

#column 76 is <id halo is inside wall @ 1 Mpc smoothing>
in_wall = [halo for halo in halos if halo[76] == '1']
not_in_wall = [halo for halo in halos if halo[76] != '1']

print len(in_wall)
print len(not_in_wall)
