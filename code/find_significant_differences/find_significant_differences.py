##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
##

import os
import sys
from scipy import stats
import numpy as np

if len(sys.argv) != 3:
  print "Usage: $ python program_name.py in.csv, out.what"
  exit()

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

if not os.path.isfile(inputfilename):
  print "Error: " + inputfilename + " is not a file!"
  exit()

#if os.path.isfile(outputfilename):
#  print "Error: " + outputfilename + " exists!"
#  exit()

catalog = []
with open(inputfilename) as file:
  for line in file:
    catalog.append(line.rstrip().split(','))

#now that it's built, convert type
halos = [[float(y) for y in x] for x in catalog]

#column 76 is <id halo is inside wall @ 1 Mpc smoothing>
halos_in_wall = [halo for halo in halos if halo[76] == 1]
halos_not_in_wall = [halo for halo in halos if halo[76] != 1]

in_wall = np.array(halos_in_wall)
not_in_wall = np.array(halos_not_in_wall)

print len(in_wall[1,:])
print len(in_wall)
print len(not_in_wall)

results = []
for i in xrange(0, len(in_wall[0,:])):
  results.append(\
    stats.ttest_ind(in_wall[:,i], not_in_wall[:,i]))

for line in results:
  print line[0], "\t", line[1]
