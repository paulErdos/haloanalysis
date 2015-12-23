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
          lines.append(line)

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
          lines.append(line)

  return lines
      
init()
h_list = read_Behroozi_catalog()
web_list = read_web_catalog()

for line in web_list:
  print line
