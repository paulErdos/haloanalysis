import numpy
import matplotlib.pyplot as pyp

#For manipulating command-line arguments                                
import sys                                                              
                                                                        
#For handling files                                                      
import os 
                                                              
#For using regular expressions                                          
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
 
