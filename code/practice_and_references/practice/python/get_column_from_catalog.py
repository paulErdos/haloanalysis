#for using regex
import re 

#for handling files
import os

#for handling parameters
import sys


#check for proper usage
if len(sys.argv) != 4:
	print("\nUsage: $ python this_program.py " 
	"inputfile outputfil column_number\n")
	exit()

#check to see if file exists already
if os.path.isfile(sys.argv[2]):
  print "Error: outputfilename \'", sys.argv[2], "' exists!"
  exit()


#now is the time os sprockets when we dance
inputfilename = sys.argv[1]
outputfilename = sys.argv[2].split('.')[0] #remove trailing extn if they added any
column_number = int(sys.argv[3]) #columns are 0-indexed

columnvalues = [];
#read but only hold on to the colum we want
if os.path.isfile(inputfilename):
	with open(inputfilename) as file:

		#get column title for which to name the outputfile
		line = file.readline().split();
		outputfilename = outputfilename + "_" + line[column_number] + ".col"
	
		#now read the lines
		for line in file:
			#ignore the comments
			if(line[0] is not '#'):
				#split the line on spaces
				splits = line.split();
				#and add the column_number-th one to the list
				columnvalues.append(splits[column_number] + "\n")

#check to see if file exists already
if os.path.isfile(outputfilename):
  print "Error: outputfilename \'", outputfilename, "' exists!"
  exit()

#write it
with open(outputfilename, 'w') as file2:
  for item in columnvalues:
    file2.write(item) 
