##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
# 
# Goal:
#   The purpose of this program is:
# 1. Gather data
#    * To read in Behroozi's halo catalog
#    * To read in Aragon-Calvo's addition to this
#    * To join them into one list of lines of comma-separated 
#      values
# 2. Create halo objects
#    * To take lines from the list and use them to create new
#      instances of the halo class
#    * To store these in a list
# 3. Nothing more, because this should be saved as a prototype
# 4. But then later this should be extended
#    * To run tests of statistical significance between halo
#      quantities dependent on whether or not they reside in
#      various cosmic web structural features
##

#To use the gigantic halo class definition without needing to
#paste it in here and clutter everything up
from halo_object import Halo

#for handling files
import os

#for handling parameters with which the program is called
import sys

#to use regular expressions
import re

def init():
  """
  Make sure the program is called correctly
  """
  
  if len(sys.argv) != 3:
    print_help()
    exit()

def print_help():
  """
  Display a brief user's guide
  """

  print "Usage: python create_halos.py catalog.list spine.csv"

def read_Behroozi_catalog():
  """
  Read the Behroozi catalog into a list of lines. 
  Neglect lines that start with '#'
  """

  #get filename 
  filename = sys.argv[1]

  #make sure this is a .list file
  if 'list' not in filename.split('.'):
    print "Error: " + filename + " not a .list file."
    print "Quitting!"
    exit()

  #now read
  lines = []
  
  #as long as it's a file
  if os.path.isfile(filename):
    with open(filename) as file:
      for line in file:
        #we want to ignore lines that start with '#'
        if line[0] != '#':
          #then trim off the trailing newline
          line = line.rstrip()
          #and split by separator and add to list
          lines.append(line.split(' '))

  return lines

def read_web_catalog():
  """
  Read the Aragon-Calvo spine catalog into a list of lines.
  """

  #get filename
  filename = sys.argv[2]

  #make sure this is a .csv file
  if 'csv' not in filename.split('.'):
    print "Error: " + filename + " not a .list file."
    print "Quitting!"
    exit()

  #now read
  lines = []

  #as long as it's a file
  if os.path.isfile(filename):
    with open(filename) as file:
      for line in file:
        #we want to ignore lines that start with '#'
        if line[0] != '#':
          #now trim off the trailing newline
          line = line.rstrip()
          #These are csv, and we want to store each datum 
          #(from each file) as a list element so split on
          #commas
          lines.append(line.split(','))

  return lines
      
#Make sure the program is called properly and read in the 
#data we'll be using
init()
h_list = read_Behroozi_catalog()
web_list = read_web_catalog()

#sanity check
if len(h_list) != len(web_list):
  print "Error: files have different number of lines."
  print "Quitting!"
  exit()

#there's probably a better way to do this that involves numpy
#which I should probably be using
#Join the lists at the seam. Join into hlist because that's 
#how this data is intended anyway
for i in xrange(0, len(h_list)):
  h_list[i] = h_list[i] + web_list[i]

#now instantiate halo objects
halo_list = []
for halo_data in h_list:
  #this gives Halo() only two arguments. Probably need to 
  #redefine the halo class. 
  halo_list.append(Halo(halo_data))



