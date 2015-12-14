##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
# Goal:
#   To try to do arrow keys with wasd (',aoe' in Dvorak).
#
##

from subprocess import call

#define directional keys
left_key = 'a'
down_key = 'o'
right_key = 'e'
up_key = ','
exit_string = 'exit'

while True:
 
  #get input 
  input = raw_input("Computer: \"Speak, heathen!\"\n: ")
  
  #handle input cases 
  if input == exit_string:
    print 'Bye!\n'
    exit()
  if input == 'clear':
    call(["clear"])
  elif input == left_key:
    print 'Left!\n'
  elif input == down_key: 
    print 'Down!\n'
  elif input == right_key:
    print 'Right!\n'
  elif input == up_key:
    print 'Up!\n'
  else:
    print 'What?'

  #There is a better way to do this
  output_string = "User: \"" + input + "\""
  
  print output_string
