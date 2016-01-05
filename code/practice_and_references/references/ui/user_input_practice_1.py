##
# Author: Vincent Steffens
# Email: vincesteffens@gmail.com
#
# Goal: 
#   To print every typed character.
#
##

#raw_input is built-in, so we needn't import

#put inside a function just for the practice
def get_and_print_input():

  #get input
  input = raw_input('Speak, heathen!\n: ')

  #print input
  print input

#oh god isn't this busy waiting oh nooooooo how do I do this
#properly???
#remember that reserved logical quantifiers are capitalized
while True:
  get_and_print_input()
