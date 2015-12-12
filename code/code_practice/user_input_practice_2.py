##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
# Goal:
#   To do user input more efficiently, and
#   to do user input better, and
#   to add a way to exit the program, and
#   to see if I can figure out how to execute external 
#   shell commands, specifically to call the unix 'clear'
#   utility.
#
##

##
#  We use call from subprocess to execute external commands 
#  like this:
#
#  Example:
#    call(["ls", "-l"])
#
##
from subprocess import call

#What is the difference between " and '?
exit_string = 'Exit'

while True:
 
  #use call to tell bash to clear the terminal
  call(["clear"])

  #get input 
  input = raw_input("Computer: \"Speak, heathen!\"\n: ")
  
  #I hope these are the same type
  if input == exit_string:
    print "See ye!"
    exit()

  #There is a better way to do this
  output_string = "User: \"" + input + "\""
  
  print output_string
