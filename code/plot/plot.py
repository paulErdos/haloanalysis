import os
import sys
from itertools import izip

if len(sys.argv) != 2:
  print "Usage: $ python plot.py file.csv"
  exit()

filename = sys.argv[1]
masses = []
radii = []

#for progress tracking
line_count = 0

if os.path.isfile(filename):
  with open(filename) as file:
    for line in file:
      values = line.rstrip().split(',')
    
      #virial mass is in column 10
      masses.append(float(values[10]))

      #virial radius is in column 11
      radii.append(float(values[11]))

      line_count = line_count + 1
      if line_count % 1000000 == 0:
        print line_count

#compute and print mean
total_mass = 0
for mass in masses:
  total_mass = total_mass + int(mass)
n = len(masses)

total_radius = 0
for radius in radii:
  total_radius = total_radius + int(radius)
m = len(radii)

print "mean mass: ", total_mass / n
print "mean radius: ", total_radius / m
