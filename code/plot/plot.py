import os
import sys
from itertools import izip

if len(sys.argv) != 2:
  print "Usage: $ python plot.py file.csv"
  exit()

filename = sys.argv[1]
masses = []
radii = []

#for tracking progress
lines_seen = 0

if os.path.isfile(filename):
  with open(filename) as file:
    for line in file:
      values = line.rstrip().split(',')
    
      #virial mass is in column 10
      masses.append(values[10])

      #virial radius is in column 11
      radii.append(values[11])

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
