#to use regular expressions
import re

#to call shell commands (to clear the screen)
from subprocess import call

exit_string = "exit"

while True:
  
  #clear the terminal
  call(["clear"]) 

  #prompt user for input
  input = raw_input("Please type a sentence, or say \"exit\" to exit:\n")

  #see if the command is to quit
  if input == exit_string:
    print "Quitting!"
    exit()

  #split the input on variable-length whitespace
  words = re.split('[ ]*', input)

  #respond
  print "You said:\n"
  for word in words:
    print word

  #wait for user to move forward
  input = raw_input("Press return to continue")

